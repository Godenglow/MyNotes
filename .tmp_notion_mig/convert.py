# -*- coding: utf-8 -*-
"""Screenpipe 日报 HTML → Notion Markdown 转换器 v2"""
import re, io, sys
from html.parser import HTMLParser

ESCAPE_CHARS = set('\\*~$[]<>{}|^')

def esc(text):
    out = []
    for ch in text:
        out.append('\\' + ch if ch in ESCAPE_CHARS else ch)
    return ''.join(out)

class Conv(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.buf = []
        self.skip = 0
        self.mode = []          # h1 h2 h3 sub meta box bt it itt tm dh tag day p li ol ul cell code
        self.table_rows = []
        self.row = None
        self.cards = None
        self.card = None
        self.card_field = None  # 0=k 1=v 2=d
        self.li_counter = 0

    def flush(self):
        t = ''.join(self.buf)
        self.buf = []
        return t.strip()

    def emit(self, line):
        if line:
            self.out.append(line)

    def handle_starttag(self, tag, attrs):
        if self.skip:
            if tag in ('script', 'style'):
                self.skip += 1
            return
        cls = dict(attrs).get('class', '')
        if tag in ('script', 'style'):
            self.skip = 1
            return
        if cls == 'crumbs':
            self.mode.append('crumb')
            return
        if tag == 'br':
            self.buf.append('\n')
            return
        if tag == 'hr':
            self.emit('')
            self.emit('---')
            return
        if tag == 'h1':
            self.mode.append('h1')
            self.buf = []
            return
        if tag == 'h2':
            self.mode.append('h2')
            return
        if tag == 'h3':
            self.mode.append('h3')
            return
        if cls == 'cards':
            self.cards = []
            self.mode.append('cards')
            return
        if cls == 'card' and self.mode and self.mode[-1] == 'cards':
            self.card = ['', '', '']
            self.mode.append('card')
            return
        if cls in ('k', 'v', 'd') and self.mode and self.mode[-1] == 'card':
            self.mode.append(('field', {'k': 0, 'v': 1, 'd': 2}[cls]))
            self.buf = []
            return
        if cls == 'bar' and self.mode and self.mode[-1] == 'card':
            self.mode.append('bar')
            return
        if cls == 'sub':
            self.mode.append('sub')
            self.buf = []
            return
        if cls == 'meta':
            self.mode.append('meta')
            self.buf = []
            return
        if tag == 'div' and cls.startswith('box'):
            self.mode.append('box')
            self.buf = []
            return
        if cls == 't' and self.mode and self.mode[-1] == 'box':
            self.mode.append('bt')
            self.buf.append('**')
            return
        if cls in ('it', 'day'):
            self.mode.append(cls)
            self.buf = []
            return
        if cls == 'tm':
            self.mode.append('tm')
            return
        if cls == 't' and self.mode and self.mode[-1] == 'it':
            self.mode.append('itt')
            self.buf.append('**')
            return
        if cls == 'dh':
            self.mode.append('dh')
            return
        if cls == 'tag' or 'tag' in cls.split():
            self.buf.append('「')
            self.mode.append('tag')
            return
        if tag == 'table':
            self.table_rows = []
            return
        if tag == 'tr':
            self.row = []
            return
        if tag in ('td', 'th'):
            self.mode.append('cell')
            self.buf = []
            return
        if tag == 'p':
            self.mode.append('p')
            self.buf = []
            return
        if tag in ('ol', 'ul'):
            self.li_counter = 0
            self.mode.append(tag)
            return
        if tag == 'li':
            self.li_counter += 1
            self.mode.append('li')
            self.buf = []
            return
        if tag in ('b', 'strong'):
            self.buf.append('**')
            return
        if tag == 'code':
            self.buf.append('`')
            self.mode.append('code')
            return

    def handle_endtag(self, tag):
        if self.skip:
            if tag in ('script', 'style'):
                self.skip -= 1
            return
        m = self.mode
        if tag == 'h1':
            self.flush()
            if m and m[-1] == 'h1':
                m.pop()
            return
        if tag == 'h2':
            t = re.sub(r'\s+', ' ', self.flush())
            self.emit('')
            self.emit('## ' + t)
            if m and m[-1] == 'h2':
                m.pop()
            return
        if tag == 'h3':
            t = re.sub(r'\s+', ' ', self.flush())
            self.emit('')
            self.emit('### ' + t)
            if m and m[-1] == 'h3':
                m.pop()
            return
        if tag == 'div':
            if m and m[-1] == 'crumb':
                m.pop()
                return
            if m and m[-1] == 'bt':
                self.buf.append('**')
                m.pop()
                return
            if m and m[-1] == 'box':
                t = re.sub(r'\s+', ' ', self.flush())
                self.emit('')
                self.emit('> ' + t)
                m.pop()
                return
            if m and m[-1] == 'it':
                t = re.sub(r'\s+', ' ', self.flush())
                self.emit('- ' + t)
                m.pop()
                return
            if m and m[-1] == 'day':
                t = re.sub(r'\s+', ' ', self.flush())
                self.emit('')
                self.emit(t)
                m.pop()
                return
            if m and m[-1] == 'sub':
                t = re.sub(r'\s+', ' ', self.flush())
                self.emit(t)
                self.emit('')
                m.pop()
                return
            if m and m[-1] == 'meta':
                t = self.flush()
                for ln in t.split('\n'):
                    ln = ln.strip()
                    if ln:
                        self.emit(ln)
                self.emit('')
                m.pop()
                return
            if m and m[-1] == 'p':
                t = re.sub(r'\s+', ' ', self.flush())
                if t:
                    self.emit('')
                    self.emit(t)
                m.pop()
                return
            if m and m and isinstance(m[-1], tuple) and m[-1][0] == 'field':
                idx = m[-1][1]
                self.card[idx] = re.sub(r'\s+', ' ', self.flush())
                m.pop()
                return
            if m and m[-1] == 'bar':
                m.pop()
                return
            if m and m[-1] == 'card':
                self.cards.append(self.card)
                self.card = None
                m.pop()
                return
            if m and m[-1] == 'cards':
                rows = [['项目', '数值', '说明']]
                for k, v, d in self.cards:
                    rows.append([k, v, d])
                self.emit('')
                self.emit_table(rows)
                self.emit('')
                self.cards = None
                m.pop()
                return
            return
        if tag == 'span':
            if m and m[-1] == 'tag':
                self.buf.append('」')
                m.pop()
                return
            if m and m[-1] == 'tm':
                t = self.flush()
                self.buf.append(t + ' ')
                m.pop()
                return
            if m and m[-1] == 'dh':
                self.buf.append(' — ')
                m.pop()
                return
            return
        if tag in ('td', 'th'):
            t = re.sub(r'\s+', ' ', self.flush()).replace('|', '\\|')
            self.row.append(t)
            if m and m[-1] == 'cell':
                m.pop()
            return
        if tag == 'tr':
            if self.row is not None:
                self.table_rows.append(self.row)
                self.row = None
            return
        if tag == 'table':
            if self.table_rows:
                self.emit('')
                self.emit_table(self.table_rows)
                self.emit('')
                self.table_rows = []
            return
        if tag == 'p':
            if m and m[-1] == 'p':
                t = re.sub(r'\s+', ' ', self.flush())
                if t:
                    self.emit('')
                    self.emit(t)
                m.pop()
            return
        if tag == 'li':
            t = re.sub(r'\s+', ' ', self.flush())
            marker = (self.li_counter and str(self.li_counter) + '.' or '-')
            self.emit(marker + ' ' + t)
            if m and m[-1] == 'li':
                m.pop()
            return
        if tag in ('ol', 'ul'):
            if m and m[-1] == tag:
                m.pop()
            return
        if tag in ('b', 'strong'):
            self.buf.append('**')
            if m and m[-1] == 'itt':
                self.buf.append(' ')
                m.pop()
            return
        if tag == 'code':
            self.buf.append('`')
            if m and m[-1] == 'code':
                m.pop()
            return

    def emit_table(self, rows):
        if not rows:
            return
        ncol = max(len(r) for r in rows)
        rows = [r + [''] * (ncol - len(r)) for r in rows]
        self.emit('<table fit-page-width="true" header-row="true">')
        self.emit('<tr>' + ''.join('<th>%s</th>' % c for c in rows[0]) + '</tr>')
        for r in rows[1:]:
            self.emit('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>')
        self.emit('</table>')

    def handle_data(self, data):
        if self.skip:
            return
        m = self.mode
        if m and m[-1] == 'h1':
            return
        if m and m[-1] == 'code':
            self.buf.append(data)
            return
        if m and m[-1] == 'meta':
            d = data.strip()
            self.buf.append(d if d else '\n')
            return
        self.buf.append(esc(re.sub(r'\s+', ' ', data)))

def convert(path):
    s = io.open(path, encoding='utf-8').read()
    s = s.split('<body', 1)[1]
    s = s.split('>', 1)[1]
    c = Conv()
    c.feed(s)
    c.close()
    out = [ln for ln in c.out if '← 前日' not in ln and '查看当日日报' not in ln]
    out = [re.sub(r'^(##+) (\d+)(?=\S)', r'\1 \2 ', ln) for ln in out]
    return '\n'.join(out)

if __name__ == '__main__':
    print('module only')
