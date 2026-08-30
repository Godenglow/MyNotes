"""Stats the visual differentiation in 00-JavaSE.md."""
from pathlib import Path
import re

text = Path('00-JavaSE.md').read_text(encoding='utf-8')
lines = text.splitlines()
print(f'Total lines: {len(lines):,}')

# Block size distribution
import re
blocks = re.findall(r'```java\n(.*?)\n```', text, re.S)
total = len(blocks)
print(f'Total ```java blocks: {total}')
one_line = sum(1 for b in blocks if b.count(chr(10)) == 0)
short = sum(1 for b in blocks if 0 < b.count(chr(10)) <= 2)
multi = sum(1 for b in blocks if b.count(chr(10)) > 2)
print(f'  1-line blocks: {one_line}')
print(f'  2-3 line blocks: {short}')
print(f'  4+ line blocks: {multi}')

print(f'> **答:** blocks: {text.count(chr(62) + " **答:**"):,}')
print(f'> 📝 blocks: {text.count(chr(62) + " 📝"):,}')
print(f'### headings: {sum(1 for l in lines if l.startswith("### ")):,}')
print(f'## headings: {sum(1 for l in lines if l.startswith("## ")):,}')
print(f'# headings: {sum(1 for l in lines if l.startswith("# ")):,}')