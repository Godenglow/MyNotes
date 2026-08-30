"""Extract Markdown from a JavaSE chapter PPTX.

Strategy: PPTX = zip archive of slide XML files. For each slide:
- parse <a:t> nodes in document order (preserves visual reading order)
- first <a:t> tends to be the slide title; rest is body
- join body lines; strip XML entities and inline tags

The output is structured but conservative — no invented bullet hierarchy.
"""
import re
import zipfile
import sys
from pathlib import Path

# XML entity decode map (in addition to what python's html.unescape covers)
ENTITIES = {
    '&quot;': '"', '&apos;': "'", '&amp;': '&',
    '&lt;': '<', '&gt;': '>', '&nbsp;': ' ',
}

INLINE_TAG_RE = re.compile(r'<[^>]+>')
XML_ENT_RE = re.compile(r'&(?:quot|apos|amp|lt|gt|nbsp);')
TEXT_NODE_RE = re.compile(r'<a:t[^>]*>(.*?)</a:t>', re.S)


def extract_slide_text(xml: str) -> list[str]:
    """Return cleaned text fragments from a single slide XML, in doc order."""
    out = []
    for m in TEXT_NODE_RE.finditer(xml):
        raw = m.group(1)
        # strip inner tags (e.g. <a:rPr> is OUTSIDE <a:t>; nested <a:r>...</a:t> structure means
        # the text inside <a:t> itself is plain; but <a:r> structure is processed by the regex
        # because <a:t>...</a:t> matches the inner text)
        cleaned = INLINE_TAG_RE.sub('', raw)
        cleaned = XML_ENT_RE.sub(lambda m: ENTITIES[m.group(0)], cleaned)
        cleaned = cleaned.strip()
        if cleaned:
            out.append(cleaned)
    return out


def extract_pptx(pptx_path: Path) -> list[tuple[int, list[str]]]:
    """Return [(slide_num, [text_fragments]) ...] for a pptx file."""
    with zipfile.ZipFile(pptx_path) as z:
        slide_names = sorted(
            [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)],
            key=lambda n: int(re.search(r'(\d+)', n).group(1)),
        )
        out = []
        for sn in slide_names:
            with z.open(sn) as f:
                xml = f.read().decode('utf-8', errors='replace')
            n = int(re.search(r'(\d+)', sn).group(1))
            out.append((n, extract_slide_text(xml)))
    return out


def slide_to_markdown(slide_num: int, fragments: list[str]) -> str:
    """Render a slide's fragments as markdown.

    Heuristic:
    - first fragment becomes `### title`
    - remaining fragments become bullet items if they're short, else paragraphs
    - very short fragments (single char/number) are merged into the next line
    - skip the title slide (slide 1) when it's a chapter cover
    """
    if not fragments:
        return ""
    # Skip chapter cover: slide 1 typically has only chapter title + author
    if slide_num == 1 and len(fragments) <= 8:
        # treat as cover
        return ""  # caller can decide

    title = fragments[0]
    body = fragments[1:]

    lines = [f"### {title}", ""]
    # Group consecutive short tokens into one line if they look like a numbered sub-section
    # E.g. ['03', '字面量', 'Java', '中有哪些字面量'] -> '03 字面量'
    cleaned = []
    i = 0
    while i < len(body):
        f = body[i]
        # short token + next fragment(s) -> join
        if len(f) <= 3 and i + 1 < len(body) and not body[i+1][0].isdigit():
            # likely a number or symbol prefix
            f = f"{f} {body[i+1]}"
            i += 2
        else:
            i += 1
        cleaned.append(f)

    for line in cleaned:
        if len(line) < 60:
            lines.append(f"- {line}")
        else:
            lines.append(line)
        lines.append("")

    return "\n".join(lines)


def main():
    src = Path(sys.argv[1])
    slides = extract_pptx(src)
    print(f"Total slides: {len(slides)}")
    for n, frags in slides[:3]:
        print(f"--- Slide {n} ({len(frags)} frags) ---")
        for f in frags:
            print(f"  | {f}")
        print()


if __name__ == "__main__":
    main()