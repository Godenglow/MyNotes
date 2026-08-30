"""Build a unified JavaSE.md from the document/ folder.

Sources:
  - 02-第一章 ... .md          -> chapter 1 (already markdown)
  - 03-第二章 ... .pptx ... 13-第十二章 ... .pptx -> chapters 2..12 (extract from PPTX)
  - 14-第十三章 ... .md ... 16-第十五章 ... .md -> chapters 13..15 (already markdown)

Output:
  D:\\MyNotes\\AngelByte_Note\\00-JavaSE.md
"""
import re
import zipfile
import shutil
from pathlib import Path
import sys

SRC = Path(r"D:\BaiduNetdiskDownload\document")
DST = Path(r"D:\MyNotes\AngelByte_Note\00-JavaSE.md")

# --------------------------------------------------------------------------
# PPTX extraction
# --------------------------------------------------------------------------

ENTITIES = {
    '&quot;': '"', '&apos;': "'", '&amp;': '&',
    '&lt;': '<', '&gt;': '>', '&nbsp;': ' ',
}
INLINE_TAG_RE = re.compile(r'<[^>]+>')
XML_ENT_RE = re.compile(r'&(?:quot|apos|amp|lt|gt|nbsp);')
TEXT_NODE_RE = re.compile(r'<a:t[^>]*>(.*?)</a:t>', re.S)
PARA_RE = re.compile(r'<a:p\b[^>]*>(.*?)</a:p>', re.S)
SLIDE_FILENAME_RE = re.compile(r'ppt/slides/slide(\d+)\.xml$')


def extract_slide_text(xml: str) -> list[str]:
    """Extract text from a PPTX slide.

    Strategy: split by <a:p> (paragraph = visual line), join runs within a
    paragraph with TAB so column-aligned data is preserved (e.g. tables,
    parameter lists). Each output fragment is one paragraph.
    """
    out = []
    for m in PARA_RE.finditer(xml):
        para_xml = m.group(1)
        cells = []
        for tm in TEXT_NODE_RE.finditer(para_xml):
            raw = tm.group(1)
            cleaned = INLINE_TAG_RE.sub('', raw)
            cleaned = XML_ENT_RE.sub(lambda mo: ENTITIES[mo.group(0)], cleaned)
            cleaned = cleaned.strip()
            if cleaned:
                cells.append(cleaned)
        if cells:
            out.append('\t'.join(cells))
    return out


def extract_pptx(pptx_path: Path) -> list[tuple[int, list[str]]]:
    with zipfile.ZipFile(pptx_path) as z:
        slide_names = sorted(
            [n for n in z.namelist() if SLIDE_FILENAME_RE.match(n)],
            key=lambda n: int(SLIDE_FILENAME_RE.match(n).group(1)),
        )
        out = []
        for sn in slide_names:
            with z.open(sn) as f:
                xml = f.read().decode('utf-8', errors='replace')
            n = int(SLIDE_FILENAME_RE.match(sn).group(1))
            out.append((n, extract_slide_text(xml)))
    return out


def is_toc_slide(fragments: list[str]) -> bool:
    """A slide is a table of contents if it contains '目录' + 'CONTENTS' or short-numbered items."""
    joined = ' '.join(fragments)
    return ('目录' in joined and 'CONTENTS' in joined) or \
           ('CONTENTS' in joined) or \
           (sum(1 for f in fragments if re.fullmatch(r'\d{2}', f)) >= 3)


def is_cover_slide(slide_num: int, fragments: list[str]) -> bool:
    """Cover = slide 1 with short fragment count."""
    return slide_num == 1 and len(fragments) <= 10


# ---------------------------------------------------------------------------
# Visual-differentiation heuristics
# ---------------------------------------------------------------------------

JAVA_KEYWORDS = {
    'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch',
    'char', 'class', 'const', 'continue', 'default', 'do', 'double', 'else',
    'enum', 'extends', 'final', 'finally', 'float', 'for', 'goto', 'if',
    'implements', 'import', 'instanceof', 'int', 'interface', 'long',
    'native', 'new', 'package', 'private', 'protected', 'public',
    'return', 'short', 'static', 'strictfp', 'super', 'switch',
    'synchronized', 'this', 'throw', 'throws', 'transient', 'try',
    'void', 'volatile', 'while', 'true', 'false', 'null',
}


def is_java_keywords_list(s: str) -> bool:
    """True if a line is dominated by Java keywords separated by , / 、.

    e.g. 'abstract, assert, boolean, break, byte, case, ...'
    """
    if not (',' in s or '、' in s):
        return False
    # split into tokens
    toks = [t for t in re.split(r'[,，、\s]+', s.strip()) if t]
    if len(toks) < 5:
        return False
    kw = sum(1 for t in toks if t.lower() in JAVA_KEYWORDS)
    return kw >= 5 and kw / len(toks) >= 0.7


def is_java_code_line(s: str) -> bool:
    """Heuristic: does this line look like Java source (not prose)?

    Stricter than before — we now require either:
      - a class/method/control-flow declaration pattern, OR
      - a System.out./System.in. line with little surrounding Chinese, OR
      - a clean identifier declaration (e.g. `int i = 100;`) without long
        Chinese prose crammed onto the same line, OR
      - a multi-statement line with 2+ semicolons.
    Lines that look like code followed by a long Chinese comment are NOT
    treated as code (they are explanations of the example).
    """
    # Strong disqualifier: line starts with Chinese character — this is a
    # prose explanation that happens to mention Java keywords
    if re.match(r'^[\u4e00-\u9fff]', s):
        return False
    # Java type-keyword declaration: 'int x = 1;' / 'short s;' / 'byte b1, b2;'
    # Also accepts access modifiers (public/private/protected/static/final).
    if re.match(r'^\s*(?:(?:public|private|protected|static|final)\s+)*(?:int|long|short|byte|char|float|double|boolean|String|void)\s+[A-Za-z_]\w*\s*(?:=[^;]+|[,(])', s):
        return True
    # Method/field signature with modifiers
    if re.search(r'\b(public|private|protected|static)\s+(static\s+)?(void|int|long|String|boolean|class|float|double|char|byte|short)\b\s+\w', s):
        return True
    # System.out / System.in prints — but only if not mixed with 8+ Chinese
    # chars (those are usually a prose explanation line that happens to
    # mention System.out.println)
    if ('System.out.' in s or 'System.in.' in s) and len(re.findall(r'[\u4e00-\u9fff]', s)) < 8:
        return True
    # Multi-statement code: 2+ semicolons AND not too much Chinese prose
    if s.count(';') >= 2 and len(re.findall(r'[\u4e00-\u9fff]{4,}', s)) < 3:
        return True
    # Single declaration like 'int i;' / 'short x;' / 'byte b1 = 11;'
    if re.match(r'^\s*(?:int|long|short|byte|char|float|double|boolean|String)\s+[A-Za-z_]\w*\s*[=;,(]', s) \
            and len(re.findall(r'[\u4e00-\u9fff]', s)) <= 4:
        return True
    # Java control flow keywords: 'if(  布尔表达式 ){' / '}else{' / 'switch('
    # Short-ish line, dominated by ASCII punctuation, mostly not Chinese.
    if re.search(r'\b(if|else if|else|switch|for|while|do|try|catch|finally)\b', s) and \
       len(re.findall(r'[\u4e00-\u9fff]', s)) < 6 and \
       ('(' in s or ')' in s or '{' in s or '}' in s) and \
       len(s.strip()) <= 60:
        return True
    # Brace-only lines: '{' or '}' alone / '}else{' / '}catch(' — common
    # continuation of multi-line Java code that got split per text frame.
    if re.match(r'^\s*[{}]\s*$', s):
        return True
    if re.match(r'^\s*[}]\s*(else|else if|catch|finally)\b\s*[{(]?', s):
        return True
    return False


def is_qa_slide_title(title: str) -> bool:
    return bool(title) and ('什么是' in title or title.endswith('是什么') or '是什么' in title[:6])


def is_exercise_slide_title(title: str) -> bool:
    return '练习' in title or '练习题' in title or '思考' in title or '课后' in title


def pptx_to_markdown(pptx_path: Path) -> str:
    """Smart PPTX -> Markdown with visual differentiation.

    Output style:
      - ### sub-heading when the slide title is a clear topic sentence
      - Tab-separated aligned rows -> markdown table
      - Code blocks (```java) for Java keyword lists and code-looking lines
      - > blockquote with **答:** prefix when the title asks "什么是 X"
      - > blockquote with 📝 prefix for exercise slides
      - bullet lists for everything else
    """
    slides = extract_pptx(pptx_path)
    out = []
    PAGE_NUM_RE = re.compile(r'^\d{1,3}$')
    # Footer patterns: page-number prefixes (e.g. '02\t关键字' or '08 数据类型 - 浮点型详解').
    FOOTER_RE = re.compile(r'^\d{1,3}[\t\s]\S.{0,18}$')

    def looks_like_heading(s: str) -> bool:
        if not s or len(s) > 20:
            return False
        if PAGE_NUM_RE.match(s):
            return False
        topic_signals = ('什么是', '如何', '定义', '分类', '规则', '区别', '特点',
                         '原理', '作用', '关键字', '语法', '结构', '继承', '实现',
                         '类型', '声明', '成员', '异常', '接口', '常用', '构造',
                         '方法', '案例', '注意', '总结', '应用', '示例',
                         '使用', '格式', '形式', '概述', '简介', '入门', '基础')
        if any(s.startswith(kw) or kw in s for kw in topic_signals):
            return True
        if re.search(r'[一二三四五六七八九十]$', s) or re.search(r'(概述|简介|入门|基础)$', s):
            return True
        if re.match(r'^Java\d+', s):
            return True
        return False

    def is_footer(line: str) -> bool:
        # Strip per-slide footer like '08 数据类型 - 浮点型详解'
        # Pattern: short number + section name + '-' + sub-section
        return bool(FOOTER_RE.match(line)) and len(line) <= 25

    def looks_like_table(rows: list[str]) -> bool:
        """3+ consecutive lines, all containing tabs, suggesting a tab-aligned table.

        Strict version: rejects three common PPT text-fragmentation patterns that
        LOOK tabular but are really prose:
          - prose paragraphs where tabs were just used for indenting ('单词\t\t单词')
          - code blocks where tabs separate tokens ('if(' + '布尔表达式' + '){')
          - long descriptive slides where each line has 6+ tab-separated cells
            but each cell is a continuation of the previous (e.g. '单行注释' 'ctrl+/'
            '别松手，鼠标移动到对应的类名下方...' — IDEA shortcuts).
        """
        if len(rows) < 2:
            return False
        if not all('\t' in r for r in rows):
            return False

        # Compute the column count per row (number of meaningful cells).
        JUNK = {'、', ',', '，', '.', '。', ':', '：', ';', '；', '', ' '}
        def cells(r):
            cs = [c for c in r.split('\t') if c.strip() and c.strip() not in JUNK]
            return cs
        col_counts = [len(cells(r)) for r in rows]
        if not col_counts or max(col_counts) < 2:
            return False
        # Reject: rows with wildly different cell counts (one row has 2, next has 6)
        avg = sum(col_counts) / len(col_counts)
        if max(col_counts) - min(col_counts) >= 3:
            return False
        # Reject: too many columns — looks like PPT multi-column body text, not a table
        if avg >= 6 or max(col_counts) >= 6:
            return False
        # Reject: if any cell looks like a Java code keyword (control flow / brace)
        CODE_BITS = {'if(', 'else', 'else if', 'else if(', 'switch', 'for', 'while',
                     'do while', 'do{', '{', '}', ';', 'public ', 'class '}
        for r in rows:
            stripped = r.replace('\t', ' ').strip()
            if any(b in stripped[:20] for b in ['if(', 'else', 'else if', 'switch(', 'for (', 'while (']):
                return False
            # Reject: row reads like a code line (mostly ASCII punct + balanced braces)
            ascii_punct = sum(stripped.count(c) for c in '(){};[]')
            if ascii_punct >= 3 and len(stripped) < 60:
                return False
        # Reject: if the joined rows look like prose (one long paragraph would have
        # 30+ consecutive Chinese chars and cell counts very close to 1 after collapse)
        joined = ''.join(rows).replace('\t', '')
        cn_chars = sum(1 for c in joined if '\u4e00' <= c <= '\u9fff')
        if cn_chars > 0 and len(rows) >= 3 and avg >= 3:
            # Looks like a multi-column PPT body, not a real table
            return False
        return True

    def render_table(rows: list[str]) -> str:
        """Convert tab-aligned rows to a markdown table.

        First row is the header; pad short rows to the column count of the header.
        Filters out 'junk' cells that are 1 character or just punctuation so the
        table doesn't explode into dozens of columns.
        """
        JUNK = {'、', ',', '，', '.', '。', ':', '：', ';', '；', ' ', ''}
        # split on tab and filter junk cells per row
        cells_raw = []
        for r in rows:
            row_cells = r.split('\t')
            row_cells = [c for c in row_cells if c.strip() not in JUNK]
            cells_raw.append(row_cells)
        if not any(cells_raw):
            return ''
        # Drop pseudo-tables where rows have just 1 real content cell
        # (e.g. '封装（\tEncapsulation\t）' has 1 real cell + 2 bare chars)
        real_counts = [sum(1 for c in row if len(c.strip()) >= 2 and c.strip() not in JUNK) for row in cells_raw]
        if max(real_counts) < 2:
            return ''
        # 2-row "tables" are almost always misaligned prose (the kind of
        # 'Java\t保留字\...' / '加号运算符\t+' that we want as bullet instead).
        # Require >=3 rows to commit to a table.
        if len(rows) < 3:
            return ''
        # Reject short 'label: value' pattern rows (each row ≤25 chars AND has
        # Chinese text). These almost always look like 3 prose fragments rather
        # than a real table.
        if all(len(r.replace('\t', '')) <= 30 for r in rows):
            joined_clean = ''.join(rows).replace('\t', '')
            cn_chars = sum(1 for c in joined_clean if '\u4e00' <= c <= '\u9fff')
            if cn_chars > 10:
                return ''
        ncols = max(real_counts)
        # Reject: small tables (≤3 columns AND ≤5 rows) where the longest cell
        # is a long prose description (>25 chars). These are usually
        # 'label + short token + lengthy description' arrangements, not data.
        if ncols <= 3 and len(rows) <= 5:
            max_cell = max((len(c) for row in cells_raw for c in row), default=0)
            if max_cell > 25:
                return ''

        if ncols < 2:
            return ''
        cells = [[c for c in row if len(c.strip()) >= 2 and c.strip() not in JUNK] for row in cells_raw]
        # Pad each row to ncols
        cells = [c + [''] * (ncols - len(c)) for c in cells]
        header = [c.strip() for c in cells[0]]
        sep = ['---'] * ncols
        body = [[c.strip() for c in row] for row in cells[1:]]
        out = []
        out.append('| ' + ' | '.join(header) + ' |')
        out.append('| ' + ' | '.join(sep) + ' |')
        for row in body:
            out.append('| ' + ' | '.join(row) + ' |')
        return '\n'.join(out)

    for n, frags in slides:
        if is_cover_slide(n, frags):
            continue
        if is_toc_slide(frags):
            continue
        # strip page numbers + footer lines from body
        body = [f for f in frags[1:] if not PAGE_NUM_RE.match(f) and not is_footer(f)]
        title = frags[0] if frags else ''

        use_heading = (
            looks_like_heading(title)
            and len(body) >= 2
            and title not in ('谢谢观看', 'Thanks', '谢谢')
        )

        is_qa = is_qa_slide_title(title)
        is_exercise = is_exercise_slide_title(title)
        # Detect "作业题"-style slides by content (footer or page label)
        body_joined = '\n'.join(body)
        if not is_exercise:
            if '作业题' in body_joined or '面试题' in body_joined:
                is_exercise = True

        if use_heading:
            out.append(f"### {title}\n")

        # --- Pass 1: collect contiguous tab-aligned lines into a table block ---
        i = 0
        new_body: list[str] = []
        while i < len(body):
            # collect runs of lines containing tabs
            tab_run = []
            j = i
            while j < len(body) and '\t' in body[j]:
                tab_run.append(body[j])
                j += 1
            if not tab_run:
                # non-tab line — keep in body for Pass 2
                new_body.append(body[i])
                i += 1
                continue
            # Tab-run found at i. prefix = non-tab lines just before it that were
            # already added to new_body. Now decide for tab_run.
            if looks_like_table(tab_run):
                # Output the table to `out`, do NOT forward to Pass 2.
                out.append(render_table(tab_run))
                out.append("")
                i = j
                continue
            # Tab-aligned but not a real table: strip tabs and re-inject into body
            # so Pass 2 can classify them normally (code / bullet / etc.).
            for tr in tab_run:
                cleaned = re.sub(r'\t+', ' ', tr).strip()
                new_body.append(cleaned)
            i = j
            continue
        # Use the cleaned body for Pass 2.
        body = new_body

        # --- Pass 2: process remaining body lines (no tabs) ---
        remaining = body[:]

        # Do NOT merge short fragments — keep each as its own bullet / line.
        # The previous aggressive merge glued unrelated PPT frames together
        # ("02 关键字" with "Java 关键字有哪些" with "Java关键字 都是小写的。").
        # The render pipeline below is robust enough to handle short lines.
        merged = [ln for ln in remaining if len(ln) > 1]

        # Render with classification: code block / blockquote / bullet / paragraph
        idx = 0
        while idx < len(merged):
            line = merged[idx]
            if is_java_keywords_list(line):
                code_lines = [line]
                j = idx + 1
                while j < len(merged) and is_java_keywords_list(merged[j]):
                    code_lines.append(merged[j])
                    j += 1
                out.append("```java")
                out.extend(code_lines)
                out.append("```")
                out.append("")
                idx = j
                continue
            if is_java_code_line(line):
                # collect contiguous code-like lines OR single short declarations
                code_lines = [line]
                j = idx + 1
                while j < len(merged) and is_java_code_line(merged[j]):
                    code_lines.append(merged[j])
                    j += 1
                if len(code_lines) >= 1:
                    out.append("```java")
                    out.extend(code_lines)
                    out.append("```")
                    out.append("")
                    idx = j
                    continue
            if is_qa and idx == 0 and len(line) >= 15:
                out.append(f"> **答:** {line}")
                out.append("")
                idx += 1
                continue
            if is_exercise:
                # Inside an exercise slide: Java code should still be a code
                # block; the '作业题'/'练习题' label line should be a heading;
                # everything else is a blockquote.
                if '作业题' in line or '面试题' in line or '练习题' in line:
                    out.append(f"## 📝 {line.replace(chr(9), ' ').strip()}")
                    out.append("")
                elif is_java_keywords_list(line):
                    out.append("```java")
                    out.append(line)
                    out.append("```")
                    out.append("")
                elif is_java_code_line(line):
                    code_lines = [line]
                    j = idx + 1
                    while j < len(merged) and is_java_code_line(merged[j]):
                        code_lines.append(merged[j])
                        j += 1
                    out.append("```java")
                    out.extend(code_lines)
                    out.append("```")
                    out.append("")
                    idx = j
                    continue
                else:
                    out.append(f"> 📝 {line}")
                    out.append("")
                idx += 1
                continue
            if len(line) < 80:
                out.append(f"- {line}")
            else:
                out.append(line)
            out.append("")
            idx += 1
        if use_heading:
            out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Markdown cleanup (lighter version of format_notes.py)
# --------------------------------------------------------------------------

YUQUE_IMG_RE = re.compile(r'!\[[^\]]*\]\(https://cdn\.nlark\.com/[^\)]*\)\s*')
EMPTY_FONT_RE = re.compile(r'<font\b[^>]*?>\s*</font>|<font\b[^>]*?/>')
LONE_BR_RE = re.compile(r'(?m)^\s*<br\s*/?>?\s*\n')
TRIPLE_BLANK_RE = re.compile(r'\n{3,}')
PLUS_BULLET_RE = re.compile(r'(?m)^(\s*)\+\s')
FONT_KEEP_RE = re.compile(r'<font\b[^>]*?>([^<]*)</font>')

CN_NUM = '一二三四五六七八九十'


def cn_ordinal(n: int) -> str:
    if n < 11:
        return CN_NUM[n - 1]
    if n < 20:
        return '十' + (CN_NUM[n - 11] if n > 10 else '')
    tens = n // 10
    ones = n % 10
    return CN_NUM[tens - 1] + '十' + (CN_NUM[ones - 1] if ones else '')


# --------------------------------------------------------------------------
# Post-processing: turn flat bullets into visually varied markdown
# --------------------------------------------------------------------------

JAVA_KEYWORDS = (
    'public|private|protected|static|void|int|long|double|float|char|byte|boolean|'
    'short|class|interface|extends|implements|return|new|if|for|while|switch|'
    'case|break|continue|throw|throws|try|catch|finally|import|package|abstract|'
    'final|native|strictfp|super|this|transient|volatile|enum|assert|default|do|'
    'else|goto|const|synchronized|instanceof'
)

# Compiled regex
JAVA_KW_STARTER_RE = re.compile(rf'^(?:{JAVA_KEYWORDS})\s', re.I)
IDENT_LIST_RE = re.compile(r'^([A-Za-z_]\w*)(?:\s*,\s*[A-Za-z_]\w*){2,}$')
PROSE_BLOCKLIST = ('以下代码', '代码如下', '代码是', '代码为', '表示', '意思是',
                   '例子', '示例', '如下:', '如下 ：', '例子:', '如下:', '提示:')


def _looks_like_code_line(s: str) -> bool:
    """Decide if a single line should be rendered as code."""
    s = s.strip()
    if not s or len(s) > 120:
        return False
    # Skip lines that announce code in prose
    if any(p in s for p in PROSE_BLOCKLIST):
        return False
    # Strong: punctuation symbols typical of code
    if any(c in s for c in ';{}()[]=') and re.search(r'[A-Za-z]', s):
        return True
    # Identifier list (comma-separated identifiers)
    if IDENT_LIST_RE.match(s):
        return True
    # Java keyword starter
    if JAVA_KW_STARTER_RE.match(s):
        return True
    return False


def _wrap_run_as_code(run: list[str]) -> str:
    """Wrap a run of consecutive '- xxx' lines as a ```java block.
    Strips the '- ' prefix on each line."""
    body = [l[2:] if l.startswith('- ') else l for l in run]
    return "\n".join(["```java", *body, "```"])


def post_process_pptx(text: str) -> str:
    """Convert flat PPTX bullets into a visually varied stream.

    Detects:
      - runs of code-like bullets  -> ```java fence
      - runs of identifier lists   -> ```text fence (for keyword lists etc.)
      - contrast/error lines       -> blockquote callout with emoji prefix
      - question/answer lines      -> Q/A format
    All transformations are fence-state-aware so we never wrap things inside
    an existing code block or list.
    """
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        stripped = l.lstrip()
        # Honour existing fences and pass through anything inside them
        if re.match(r'^\s*(```|~~~)', stripped):
            out.append(l)
            # skip until matching close
            i += 1
            while i < len(lines):
                out.append(lines[i])
                if re.match(r'^\s*(```|~~~)\s*$', lines[i]):
                    i += 1
                    break
                i += 1
            continue

        # Try to collect a run of consecutive '- ...' bullets that all look like code
        if l.startswith('- '):
            j = i
            run = []
            while j < len(lines) and lines[j].startswith('- '):
                if _looks_like_code_line(lines[j]):
                    run.append(lines[j])
                    j += 1
                else:
                    break
            if len(run) >= 2:
                out.append(_wrap_run_as_code(run))
                out.append("")
                i = j
                continue

            # Identifier-list bullet: a single bullet whose body is a comma-separated identifier list
            body = l[2:].strip()
            if IDENT_LIST_RE.match(body):
                out.append("```text")
                out.append(body)
                out.append("```")
                out.append("")
                i += 1
                continue

            # Contrast/error pattern detection
            contrast_run, consumed = _try_collect_contrast(i, lines)
            if contrast_run:
                out.extend(contrast_run)
                i = consumed
                continue

        out.append(l)
        i += 1

    # Re-merge blank lines so we don't double up
    out_text = "\n".join(out)
    out_text = re.sub(r'\n{3,}', '\n\n', out_text)
    return out_text


def _try_collect_contrast(start: int, lines: list[str]):
    """Detect lines like '以上代码...就不如以下的代码:' followed by a code block,
    and produce a before/after blockquote."""
    l = lines[start]
    if not l.startswith('- '):
        return None, start
    body = l[2:]
    triggers = ('以上代码', '代码如下', '错误示例', '正确示例', '这样是不允许的',
                '不建议这样写', '对比', '下面是', '如下所示', '不允许')
    if not any(t in body for t in triggers):
        return None, start

    out = []
    if '不允许' in body or '不建议' in body or '错误' in body:
        out.append('> ⚠️ **注意(反例):**')
        out.append('>')
    elif '以下' in body or '如下' in body or '下面' in body:
        out.append('> 📝 **示例:**')
        out.append('>')
    # Convert the trigger line to a blockquote as well
    if body.strip():
        # split the rest of the trigger into bullets that go after
        pass

    consumed = start + 1
    return out, consumed


def clean_markdown(text: str) -> str:
    """Clean a Yuque-style markdown source body (chapter-internal content).

    1. Strip cdn.nlark.com Yuque watermarks.
    2. Remove empty <font></font> and self-closing <font/>.
    3. Drop lone <br/> lines.
    4. Convert '+ ' bullets to '- '.
    5. Collapse font wrappers but keep inner text.
    6. Promote/demote headings: any standalone H1 inside a chapter that
       doesn't look like the chapter title (i.e. lacks '第' and '章') gets
       downgraded to H2 so the hierarchy stays: # 第X章 > ## 章节 > ### 小节.
    7. Collapse 3+ blank lines to 1 and trim outer blanks.
    """
    text = YUQUE_IMG_RE.sub('', text)
    text = EMPTY_FONT_RE.sub('', text)
    text = LONE_BR_RE.sub('', text)
    text = PLUS_BULLET_RE.sub(r'\1- ', text)
    text = FONT_KEEP_RE.sub(r'\1', text)

    # Downgrade chapter-internal H1s (those without '第X章') to H2.
    def _demote_internal_h1(m):
        line = m.group(0)
        if re.search(r'第[一二三四五六七八九十百千]+章', line):
            return line  # keep chapter heading
        return '## ' + line[2:]  # '# X' -> '## X'

    text = re.sub(r'^# .+$', _demote_internal_h1, text, flags=re.M)

    text = TRIPLE_BLANK_RE.sub('\n\n', text)
    text = text.strip('\n')
    return text

    # Downgrade chapter-internal H1s (those without '第X章') to H2.
    # Yuque exports every section as H1 — we normalise them to H2 so the
    # hierarchy is consistent: # 第X章 > ## 节 > ### 小节.
    def _demote_internal_h1(m):
        line = m.group(0)
        if re.search(r'第[一二三四五六七八九十百千]+章', line):
            return line  # keep chapter heading
        return '## ' + line[2:]  # '# X' -> '## X'

    text = re.sub(r'^# .+$', _demote_internal_h1, text, flags=re.M)

    text = TRIPLE_BLANK_RE.sub('\n\n', text)
    text = text.strip('\n')
    return text


# --------------------------------------------------------------------------
# Chapter orchestration
# --------------------------------------------------------------------------

CHAPTER_MD = [
    # (file, chapter_number_arabic, chapter_title, kind)
    ('02-第一章 Java开发环境搭建.md', 1, 'Java开发环境搭建', 'md'),
    ('03-第二章 Java基础语法.pptx', 2, 'Java基础语法', 'pptx'),
    ('04-第三章 面向对象.pptx', 3, '面向对象', 'pptx'),
    ('05-第四章 数组.pptx', 4, '数组', 'pptx'),
    ('06-第五章 异常.pptx', 5, '异常', 'pptx'),
    ('07-第六章 常用类.pptx', 6, '常用类', 'pptx'),
    ('08-第七章 集合.pptx', 7, '集合', 'pptx'),
    ('09-第八章 IO流.pptx', 8, 'IO流', 'pptx'),
    ('10-第九章 多线程.pptx', 9, '多线程', 'pptx'),
    ('11-第十章 反射机制.pptx', 10, '反射机制', 'pptx'),
    ('12-第十一章 注解.pptx', 11, '注解', 'pptx'),
    ('13-第十二章 网络编程.pptx', 12, '网络编程', 'pptx'),
    ('14-第十三章 Lambda表达式.md', 13, 'Lambda表达式', 'md'),
    ('15-第十四章 Stream API.md', 14, 'Stream API', 'md'),
    ('16-第十五章 Java新特性.md', 15, 'Java新特性', 'md'),
]

# Emoji per chapter for visual differentiation
CHAPTER_EMOJI = ['🚀', '🔧', '🎯', '📊', '⚡', '🛠️', '📦', '🌊', '🧵',
                 '🔮', '🏷️', '🌍', 'λ', '🌊', '✨']


def build():
    if not SRC.exists():
        sys.exit(f"Source dir not found: {SRC}")

    parts = ["# JavaSE\n", "JavaSE 课程笔记整理,涵盖 Java 基础语法到 Java 21 新特性。\n"]

    toc_lines = ["", "## 目录\n"]
    for _, num, title, _ in CHAPTER_MD:
        toc_lines.append(f"- 第{cn_ordinal(num)}章 {title}")
    parts.append("\n".join(toc_lines) + "\n")

    for fname, num, title, kind in CHAPTER_MD:
        fpath = SRC / fname
        if not fpath.exists():
            print(f"WARN: missing {fpath}",file=sys.stderr)
            continue
        emoji = CHAPTER_EMOJI[num - 1]
        chapter_heading = f"# {emoji} 第{cn_ordinal(num)}章 {title}\n"
        parts.append(chapter_heading)
        if kind == 'md':
            text = fpath.read_text(encoding='utf-8', errors='replace')
            # strip any leading "# XXXX" the source file may already have to avoid dup title
            text = re.sub(r'^#\s*[^\n]*\n', '', text.lstrip('\n'), count=1)
            text = clean_markdown(text)
            parts.append(text)
        else:
            md = pptx_to_markdown(fpath)
            parts.append(md)
        parts.append("\n\n")

    DST.parent.mkdir(parents=True, exist_ok=True)
    raw = "\n".join(parts)
    # global cleanup: collapse triple+ blanks, trim ends
    raw = TRIPLE_BLANK_RE.sub('\n\n', raw).strip('\n') + '\n'
    # Final safety net: any lingering \t in non-code contexts becomes a space.
    # Walk line by line so we don't disturb code fences.
    _tab = '\t'
    _fence_open = re.compile(r'^\s*(```|~~~)\s*(\S+)?')
    _fence_close = re.compile(r'^\s*(```|~~~)\s*$')
    final_lines = []
    in_fence = False
    fence_marker = None
    fence_min = 3
    for ln in raw.split('\n'):
        m_open = _fence_open.match(ln)
        m_close = _fence_close.match(ln)
        if not in_fence and m_open:
            in_fence = True
            fence_marker = m_open.group(1)[0]
            fence_min = len(m_open.group(1))
            final_lines.append(ln)
            continue
        if in_fence and m_close and len(m_close.group(1)) >= fence_min and m_close.group(1)[0] == fence_marker:
            in_fence = False
            final_lines.append(ln)
            continue
        if in_fence:
            final_lines.append(ln)
        else:
            final_lines.append(ln.replace(_tab, ' '))
    raw = '\n'.join(final_lines)
    DST.write_text(raw, encoding='utf-8')

    size_kb = DST.stat().st_size / 1024
    print(f"Wrote {DST} ({size_kb:.1f} KB)")
    total_lines = DST.read_text(encoding='utf-8').count('\n')
    print(f"Total lines: {total_lines:,}")


if __name__ == "__main__":
    build()