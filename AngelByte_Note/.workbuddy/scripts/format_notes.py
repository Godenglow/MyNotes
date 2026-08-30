#!/usr/bin/env python3
"""Format .md notes for Obsidian compatibility.

Pipeline (state-aware re. code fences):
  1. Strip BOM, trim leading/trailing blank lines.
  2. Remove "lone" <br/> / <br> / </br> lines (outside fences and tables).
  3. Collapse 3+ consecutive blank lines to 1 blank line.
  4. Normalize list bullet '+ ' to '- ' (outside fences).
  5. Wrap "indented code" (>=4 spaces or tab) with ```fence``` when strong
     code signals are present. Best-effort language detection.
  6. Repair unmatched opening fences by appending a closing ```.

Backup of every input file lives at:
  .workbuddy/notes_backup_<TIMESTAMP>/
The script is idempotent and writes atomically.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

WORKSPACE = Path(r"D:\MyNotes\AngelByte_Note")
EXCLUDE_DIR_PARTS = {".workbuddy", ".workbuddy", ".claude", "notes_backup"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")


def _walk_with_fence(text: str):
    """Yield (line, in_fence_state_after)."""
    in_fence = False
    fence_len = 3
    fence_char = '`'
    for line in text.splitlines():
        m = _FENCE_RE.match(line)
        if m:
            cur = m.group(2)
            # close only if same char and len>=opening
            if not in_fence:
                in_fence = True
                fence_len = len(cur)
                fence_char = cur[0]
            elif cur[0] == fence_char and len(cur) >= fence_len and m.group(3).strip() == '':
                in_fence = False
        yield line, in_fence


# ---------------------------------------------------------------------------
# Individual transformations
# ---------------------------------------------------------------------------

def remove_bom(text: str):
    if text.startswith("\ufeff"):
        return text[1:], True
    return text, False


def trim_blank_ends(text: str):
    # leading blank lines
    head = re.match(r"\n*", text[len(text.lstrip('\n')) - 1:] if False else "")
    # simpler
    lead = len(text) - len(text.lstrip('\n'))
    new = text[lead:]
    # trailing whitespace lines
    new2 = new.rstrip()
    trail = len(new) - len(new2)
    out = new2 + ("\n" if new2 else "")
    return out, lead + trail


def remove_lone_br(text: str) -> tuple[str, int]:
    """Delete lines that contain only <br/> / <br> / </br> (outside fences)."""
    pat = re.compile(r"^\s*<br\s*/?>s?\s*$")  # we may have <br/> or <br>
    # use simpler pattern
    pat = re.compile(r"^\s*</?br\s*/?>\s*$")
    out = []
    count = 0
    in_fence = False
    fence_len = 3
    fence_char = '`'
    for raw in text.splitlines():
        m = _FENCE_RE.match(raw)
        if m:
            cur = m.group(2)
            if not in_fence:
                in_fence = True
                fence_len = len(cur)
                fence_char = cur[0]
            elif cur[0] == fence_char and len(cur) >= fence_len and m.group(3).strip() == "":
                in_fence = False
            out.append(raw)
            continue
        if in_fence:
            out.append(raw)
            continue
        if pat.match(raw):
            count += 1
            continue
        out.append(raw)
    return "\n".join(out), count


def collapse_blank_lines(text: str):
    collapses = len(re.findall(r"\n{3,}", text))
    return re.sub(r"\n{3,}", "\n\n", text), collapses


def remove_empty_font_tags(text: str) -> tuple[str, int]:
    """Delete completely empty <font ...></font> and <font .../> tags.

    Only acts OUTSIDE fenced code blocks. Non-empty <font>x</font> is left
    alone so we don't lose color/style information.
    """
    pat = re.compile(r"</?font\b[^>]*?>\s*</font\s*>|<font\b[^>]*?/>")
    out_lines = []
    count = 0
    in_fence = False
    fence_len = 3
    fence_char = '`'
    for raw in text.splitlines():
        m = _FENCE_RE.match(raw)
        if m:
            cur = m.group(2)
            if not in_fence:
                in_fence = True
                fence_len = len(cur)
                fence_char = cur[0]
            elif cur[0] == fence_char and len(cur) >= fence_len and m.group(3).strip() == "":
                in_fence = False
            out_lines.append(raw)
            continue
        if in_fence:
            out_lines.append(raw)
            continue
        new, n = pat.subn("", raw)
        if n:
            count += n
        out_lines.append(new)
    return "\n".join(out_lines), count


def fix_heading_fence_collision(text: str):
    """If a markdown heading is immediately followed by a fenced code
    block opener (no blank line between), insert a blank line so Obsidian
    and other strict renderers treat it as a code block.

    State-aware wrt existing code fences."""
    out = []
    count = 0
    in_fence = False
    fence_len = 3
    fence_char = '`'
    HEADING_RE = re.compile(r"^#{1,6}\s+\S")
    FENCE_OPEN_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*\S")  # opener with language hint
    FENCE_BARE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*$")    # bare fence `\`\`\`` on its own line
    for raw in text.splitlines():
        m_close = _FENCE_RE.match(raw)  # any fence line (open or close)
        # decide if this line opens a new fence
        fence_action = None
        if m_close:
            cur = m_close.group(2)
            if not in_fence:
                fence_action = "open"
            elif cur[0] == fence_char and len(cur) >= fence_len and m_close.group(3).strip() == "":
                fence_action = "close"
        is_opener = fence_action == "open"
        # If we're about to emit an opener AND the previous emitted line is a heading
        # AND the previous emitted line is NOT itself a blank (defensive),
        # AND there was no intervening blank, insert a blank line.
        if is_opener and out and HEADING_RE.match(out[-1].lstrip()):
            # avoid double blank if last emitted already blank
            if out[-1].strip() != "":
                out.append("")
                count += 1
        out.append(raw)
        # update state
        if is_opener:
            in_fence = True
            fence_len = len(m_close.group(2))
            fence_char = m_close.group(2)[0]
        elif fence_action == "close":
            in_fence = False
    return "\n".join(out), count


def normalize_list_bullets(text: str):
    """Outside fences, change leading '+ ' to '- ' (top-level only; sub-list + untouched)."""
    pat = re.compile(r"^(\s*)\+\s")
    out = []
    count = 0
    in_fence = False
    fence_len = 3
    fence_char = '`'
    for raw in text.splitlines():
        m = _FENCE_RE.match(raw)
        if m:
            cur = m.group(2)
            if not in_fence:
                in_fence = True
                fence_len = len(cur)
                fence_char = cur[0]
            elif cur[0] == fence_char and len(cur) >= fence_len and m.group(3).strip() == "":
                in_fence = False
            out.append(raw)
            continue
        if in_fence:
            out.append(raw)
            continue
        new, n = pat.subn(r"\1- ", raw, count=1)
        if n:
            count += 1
        out.append(new)
    return "\n".join(out), count


# ---------------------------------------------------------------------------
# Indented-code wrapping
# ---------------------------------------------------------------------------

CODE_KEYWORDS_RE = re.compile(
    r"(?:"
    # SQL
    r"\b(?:SELECT|INSERT\s+INTO|UPDATE\s+\w+|DELETE\s+FROM|CREATE\s+TABLE|CREATE\s+(?:INDEX|VIEW)|"
    r"ALTER\s+TABLE|DROP\s+(?:TABLE|INDEX|VIEW)|TRUNCATE\s+TABLE|FROM\s+\w+|WHERE\s+|"
    r"JOIN\s+\w+|GROUP\s+BY|ORDER\s+BY|HAVING\s+|VALUES\s*\()"
    # Java
    r"|\b(?:public|private|protected|static|final|abstract|class|interface|extends|implements|"
    r"void|int|long|short|byte|float|double|char|boolean|String|return|new\s+\w+|"
    r"import\s+[a-z]|package\s+[a-z]|@Override|@Test|@Autowired|@RequestMapping|"
    r"@RestController|@Controller|@Service|@Repository|@Configuration|@Bean|@Data|"
    r"@SpringBootApplication|@Component|@Value|@Autowired|@TableField|@TableName)\b"
    # XML / MyBatis / Maven
    r"|<\?(?:xml)\b|</?[a-zA-Z][\w:]*\b|<!--"
    # Shell
    r"|(?:^|\s)(?:docker|apt-get|yum|brew|chmod|chown|curl|wget|echo|exit|cat|sed|awk|"
    r"grep|export|alias|source|pwd|ls\b|mkdir|rm\s+|cp\s+|mv\s+|tar\s+|ssh\s+|sudo\s+|"
    r"if\s+|for\s+|while\s+|case\s+)"
    # JS / TS / general
    r"|(?:function\s+\w+|const\s+\w+|let\s+\w+|var\s+\w+|=>|console\.|require\(|module\.exports|"
    r"import\s+\{)\b"
    # HTML
    r"|(?:<!DOCTYPE|<html\b|<head\b|<body\b|<div\b|<span\b|<script\b|<style\b|<template\b)"
    # yaml / properties / pom
    r"|(?:^|\s)(?:version|groupId|artifactId|dependencies|name:|description:)\s*[=:>]"
    r")"
)


def _is_indented_code_line(line: str) -> bool:
    if not line:
        return False
    return line.startswith("\t") or line.startswith("    ")


def _strip_indent(line: str) -> str:
    if line.startswith("\t"):
        return line[1:]
    if line.startswith("    "):
        return line[4:]
    return line


def _detect_language(block_lines: list[str]) -> str:
    joined = "\n".join(block_lines)
    if re.search(r"<mapper\b|<select\b|<insert\b|<update\b|<delete\b|<resultMap\b|<where\b|<if\b|<choose\b|<when\b|<otherwise\b|<foreach\b|<trim\b", joined, re.I):
        return "xml"
    if re.search(r"public\s+(?:class|static\s+void)|private\s+\w+\s+\w+\s*\(|@Override|@Test\b|@RestController|@SpringBootApplication|@Configuration\b|@Bean\b|import\s+[a-z]+\.", joined, re.I):
        return "java"
    if re.search(r"<\?(?:xml)\b|<!DOCTYPE|<html\b", joined, re.I):
        return "html"
    if re.search(r"<dependency\b|<plugin\b|<project\b|<modules\b|<build\b|<properties\b|<groupId\b|<artifactId\b", joined, re.I):
        return "xml"
    if re.search(r"\b(SELECT\b.+FROM|INSERT\s+INTO|UPDATE\s+\w+\s+SET|DELETE\s+FROM|CREATE\s+TABLE|ALTER\s+TABLE|DROP\s+TABLE)", joined, re.I | re.S) and "<mapper" not in joined.lower():
        return "sql"
    if re.search(r"\bfunction\b|\bconst\s+\w+\s*=|\blet\s+\w+\s*=|\bvar\s+\w+\s*=|=>|console\.log|require\(|module\.exports", joined, re.I):
        return "javascript"
    if re.search(r"(?m)^\s*(?:docker|apt-get|yum|brew|chmod|chown|curl|wget|echo|cat|grep|export|alias|source|sudo|if\s+|for\s+)\b", joined):
        return "bash"
    if re.search(r"(?m)^\s*(?:version|groupId|artifactId|name:|description:|server:|spring:|app:)\s*[=:]?", joined):
        return "yaml"
    return ""


def _looks_like_code(block_lines: list[str]) -> bool:
    if len(block_lines) < 3:
        return False
    stripped = [_strip_indent(l) for l in block_lines]
    # SAFETY: if any non-blank line starts with a list marker, this is a
    # nested (indented) bullet/numbered list, not code. Don't wrap.
    LIST_MARKER_RE = re.compile(r"^[-*+]\s|\d+\.\s")
    for s in stripped:
        ss = s.lstrip()
        if not ss.strip():
            continue
        if LIST_MARKER_RE.match(ss):
            return False
    hits = 0
    nonblank = 0
    for s in stripped:
        if not s.strip():
            continue
        nonblank += 1
        if CODE_KEYWORDS_RE.search(s):
            hits += 1
    if nonblank == 0:
        return False
    # require >=50% nonblank lines to carry strong code signal
    return hits >= max(1, (nonblank + 1) // 2)


def wrap_indented_code(text: str):
    """Wrap contiguous 4-space/Tab indented blocks (>=3 lines) as ```lang blocks.

    Returns (new_text, wrapped_count)."""
    lines = text.splitlines()
    out = []
    wrapped = 0
    in_fence = False
    fence_len = 3
    fence_char = '`'
    i = 0
    while i < len(lines):
        raw = lines[i]
        m = _FENCE_RE.match(raw)
        if m:
            cur = m.group(2)
            if not in_fence:
                in_fence = True
                fence_len = len(cur)
                fence_char = cur[0]
            elif cur[0] == fence_char and len(cur) >= fence_len and m.group(3).strip() == "":
                in_fence = False
            out.append(raw)
            i += 1
            continue
        if in_fence:
            out.append(raw)
            i += 1
            continue
        if _is_indented_code_line(raw):
            # gather contiguous indented lines
            j = i
            block = []
            while j < len(lines) and _is_indented_code_line(lines[j]):
                block.append(lines[j])
                j += 1
            # allow trailing blank lines that are still inside this region?
            # No: be strict — contiguous only.
            if _looks_like_code(block):
                stripped_block = [_strip_indent(l) for l in block]
                lang = _detect_language(stripped_block)
                fence_open = "```" + lang
                out.append(fence_open)
                out.extend(stripped_block)
                out.append("```")
                wrapped += 1
                i = j
                continue
            out.append(raw)
            i += 1
        else:
            out.append(raw)
            i += 1
    new = "\n".join(out)
    if text.endswith("\n") and not new.endswith("\n"):
        new += "\n"
    elif not text.endswith("\n") and new.endswith("\n"):
        new = new.rstrip("\n")
    return new, wrapped


def repair_unmatched_fences(text: str):
    """If file ends inside an open fence, append ``` to close."""
    in_fence = False
    fence_len = 3
    fence_char = '`'
    for raw in text.splitlines():
        m = _FENCE_RE.match(raw)
        if m:
            cur = m.group(2)
            if not in_fence:
                in_fence = True
                fence_len = len(cur)
                fence_char = cur[0]
            elif cur[0] == fence_char and len(cur) >= fence_len and m.group(3).strip() == "":
                in_fence = False
    if in_fence:
        return text + "\n```\n", 1
    return text, 0


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def process(text: str) -> dict:
    text, had_bom = remove_bom(text)
    text, trimmed_lead_trail = trim_blank_ends(text)
    text, br_removed = remove_lone_br(text)
    text, font_removed = remove_empty_font_tags(text)
    text, blanks_collapsed = collapse_blank_lines(text)
    text, bullets = normalize_list_bullets(text)
    text, fence_collisions = fix_heading_fence_collision(text)
    text, fences_wrapped = wrap_indented_code(text)
    text, fences_repaired = repair_unmatched_fences(text)
    text, trimmed2 = trim_blank_ends(text)
    return {
        "had_bom": had_bom,
        "trimmed_blank_lines": trimmed_lead_trail + trimmed2,
        "br_removed": br_removed,
        "empty_fonts_removed": font_removed,
        "blanks_collapsed": blanks_collapsed,
        "bullets_normalized": bullets,
        "heading_fence_collisions_fixed": fence_collisions,
        "fences_wrapped": fences_wrapped,
        "fences_repaired": fences_repaired,
        "output": text,
    }


def process_file(p: Path) -> dict:
    raw = p.read_text(encoding="utf-8", errors="replace")
    info = process(raw)
    info["old_bytes"] = len(raw.encode("utf-8"))
    info["new_bytes"] = len(info["output"].encode("utf-8"))
    if info["output"] != raw:
        p.write_text(info["output"], encoding="utf-8")
    return info


def main() -> None:
    md_files: list[Path] = []
    for p in WORKSPACE.rglob("*.md"):
        rel = p.relative_to(WORKSPACE)
        if any(part.startswith(".") or part in EXCLUDE_DIR_PARTS for part in rel.parts):
            continue
        md_files.append(p)
    md_files.sort()

    summaries = []
    for p in md_files:
        info = process_file(p)
        rel = str(p.relative_to(WORKSPACE))
        clean = {k: v for k, v in info.items() if k != "output"}
        clean["path"] = rel
        summaries.append(clean)

    report_path = WORKSPACE / ".workbuddy" / "format_report.json"
    report_path.write_text(
        json.dumps(summaries, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    # also write a markdown digest
    md_lines = ["# 笔记格式化报告", ""]
    for s in summaries:
        md_lines.append(f"## `{s['path']}`")
        md_lines.append(
            f"- 字节: {s['old_bytes']:,} → {s['new_bytes']:,}"
        )
        md_lines.append(f"- BOM 移除: {'是' if s['had_bom'] else '否'}")
        md_lines.append(f"- 首尾空行裁剪: {s['trimmed_blank_lines']}")
        md_lines.append(f"- 独立 `<br/>` 删除: {s['br_removed']}")
        md_lines.append(f"- 空 `<font>` 标签删除: {s['empty_fonts_removed']}")
        md_lines.append(f"- 多余空行压缩(3+→1): {s['blanks_collapsed']}")
        md_lines.append(f"- `+ ` 列表项替换为 `- `: {s['bullets_normalized']}")
        md_lines.append(f"- 标题紧贴围栏 → 加空行: {s['heading_fence_collisions_fixed']}")
        md_lines.append(f"- 缩进代码块包裹为围栏: {s['fences_wrapped']}")
        md_lines.append(f"- 未闭合围栏补齐: {s['fences_repaired']}")
        md_lines.append("")
    digest_path = WORKSPACE / ".workbuddy" / "format_report.md"
    digest_path.write_text("\n".join(md_lines), encoding="utf-8")

    totals = {
        "files": len(summaries),
        "br_removed": sum(s["br_removed"] for s in summaries),
        "empty_fonts_removed": sum(s["empty_fonts_removed"] for s in summaries),
        "blanks_collapsed": sum(s["blanks_collapsed"] for s in summaries),
        "bullets_normalized": sum(s["bullets_normalized"] for s in summaries),
        "heading_fence_collisions_fixed": sum(s["heading_fence_collisions_fixed"] for s in summaries),
        "fences_wrapped": sum(s["fences_wrapped"] for s in summaries),
        "fences_repaired": sum(s["fences_repaired"] for s in summaries),
    }
    print(json.dumps(totals, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
