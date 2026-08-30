"""Comprehensive verification scan across all .md notes.

Re-checks issues already fixed by format_notes.py + scans for new issues
the script intentionally didn't touch."""
import re
from pathlib import Path
from collections import Counter

md_files = sorted(
    p for p in Path('.').rglob('*.md')
    if not any(part.startswith('.') for part in p.parts) and '.workbuddy' not in p.parts
)

issues = {
    'plus_bullet': [],
    'triple_blank': [],
    'lone_br_outside_fence': [],
    'empty_font_remaining': [],
    'heading_fence_collision': [],
    'heading_level_skip': [],
    'unclosed_fence': [],
    'bom_remaining': [],
    'leading_blank_lines': [],
    'trailing_blank_lines': [],
    'mixed_img_path_sep': [],
    'orphan_asterisk': [],
    'empty_fence_only_line': [],
    'table_with_br_only_cells': [],
}
stats = Counter()

FENCE_RE = re.compile(r'^(\s*)(`{3,}|~{3,})(.*)$')
HEADING_RE = re.compile(r'^(#{1,6})\s+(\S.*)?$')
HEADING_FENCE_NEXT_RE = re.compile(r'^\s*`')
LONE_BR_RE = re.compile(r'^\s*<br\s*/?>?\s*$')
EMPTY_FONT_RE = re.compile(r'<font\b[^>]*?>\s*</font>|<font\b[^>]*?/>')
TRIPLE_BLANK_RE = re.compile(r'\n\n\n\n+')

for p in md_files:
    raw = p.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'):
        issues['bom_remaining'].append(p)
    text = raw.decode('utf-8', errors='replace')
    lines = text.splitlines()
    n_lines = len(lines)
    stats['total_lines'] += n_lines

    # leading/trailing blanks
    if lines and lines[0].strip() == '':
        issues['leading_blank_lines'].append(p)
    if lines and lines[-1].strip() == '':
        issues['trailing_blank_lines'].append(p)

    in_fence = False; flen = 3; fch = '`'
    last_heading_level = 0
    for i, l in enumerate(lines):
        m = FENCE_RE.match(l)
        if m:
            cur = m.group(2)
            if not in_fence:
                in_fence = True; flen = len(cur); fch = cur[0]
            elif cur[0] == fch and len(cur) >= flen and m.group(3).strip() == '':
                in_fence = False
            continue
        if in_fence:
            continue
        # plus bullet (top-level)
        if re.match(r'^\+\s', l):
            issues['plus_bullet'].append((p, i+1, l[:60]))
        # heading
        h = HEADING_RE.match(l)
        if h:
            lvl = len(h.group(1))
            if last_heading_level and lvl > last_heading_level + 1:
                issues['heading_level_skip'].append((p, i+1, last_heading_level, lvl, l[:50]))
            last_heading_level = lvl
            if i + 1 < len(lines) and HEADING_FENCE_NEXT_RE.match(lines[i+1]):
                issues['heading_fence_collision'].append((p, i+1, l[:50], lines[i+1][:30]))
        # lone br
        if LONE_BR_RE.match(l):
            issues['lone_br_outside_fence'].append((p, i+1))
        # empty font
        if EMPTY_FONT_RE.search(l):
            issues['empty_font_remaining'].append((p, i+1, l[:60]))
        # orphan asterisk (a ' *' line that's alone — often a glitched bullet)
        if re.match(r'^\s*\*\s*$', l):
            issues['orphan_asterisk'].append((p, i+1))
        # bare ``` on a line by itself (i.e. ``` that doesn't open/close because it's followed by text on same line)
        if re.fullmatch(r'\s*`{3,}\s*', l) and not in_fence:
            # may be intentional (close then re-open) — flag for review
            issues['empty_fence_only_line'].append((p, i+1))

    # triple blank
    for mm in TRIPLE_BLANK_RE.finditer(text):
        issues['triple_blank'].append((p, mm.start()))
    # unclosed fence parity
    in_fence2 = False; flen2 = 3; fch2 = '`'
    for l in text.splitlines():
        m = FENCE_RE.match(l)
        if m:
            cur = m.group(2)
            if not in_fence2:
                in_fence2 = True; flen2 = len(cur); fch2 = cur[0]
            elif cur[0] == fch2 and len(cur) >= flen2 and m.group(3).strip() == '':
                in_fence2 = False
    if in_fence2:
        issues['unclosed_fence'].append(p)
    # mixed image path separators (markdown links/images)
    backslash = len(re.findall(r'!\[[^\]]*\]\([^)]*\\+[^)]*\)', text))
    slash = len(re.findall(r'!\[[^\]]*\]\([^)]*/[^)]*\)', text))
    if backslash and slash:
        issues['mixed_img_path_sep'].append((p, backslash, slash))

print('=== REGRESSION CHECKS (script should have killed all of these) ===')
for k in ['plus_bullet', 'triple_blank', 'lone_br_outside_fence',
          'empty_font_remaining', 'heading_fence_collision', 'unclosed_fence',
          'bom_remaining', 'leading_blank_lines', 'trailing_blank_lines']:
    n = len(issues[k])
    print(f'  {k:32s}: {n}')
    if 0 < n < 6:
        for r in issues[k][:5]:
            print(f'      {r}')

print()
print('=== NEW SCANS (issues the script did not target) ===')
for k in ['heading_level_skip', 'mixed_img_path_sep', 'orphan_asterisk', 'empty_fence_only_line']:
    n = len(issues[k])
    print(f'  {k:32s}: {n}')
    if 0 < n < 10:
        for r in issues[k][:10]:
            print(f'      {r}')

print()
print(f'  total .md files scanned: {len(md_files)}')
print(f'  total lines scanned:     {stats["total_lines"]:,}')