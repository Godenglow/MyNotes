# -*- coding: utf-8 -*-
"""把 项目一.md / 技能特长.md 的排版统一成 项目二.md 的样式。

只动格式，不动文字：
  1. `**N. 题干**`              -> `### N. 题干`
  2. 密不透风的长答案段落        -> 在「。**标签**：」与 ①②③ 枚举处断开成多段
  3. 每组紧跟 `## 标题` 的斜体提示 -> Obsidian warning callout
"""
import re
import sys

BASE = r"D:\MyNotes\面试\简历提问"

HEAD_RE = re.compile(r'^\*\*(\d+)\. (.+?)\*\*$')
STD_HINT = re.compile(r'^本组最容易被打穿的点[：:](.+)$')

# 段内断开点
BOLD_SPLIT = re.compile(r'(?<=。)(?=\*\*[^*\n]+?\*\*[：:])')
ENUM_SPLIT = re.compile(r'(?<=[；。：])(?=[\u2460-\u2473])')

SKIP_START = ('#', '|', '>', '```', '~~~', '![', '$$')


def is_body(line):
    """判断这行是不是可以断句的普通段落。"""
    s = line.strip()
    if not s:
        return False
    if s.startswith(SKIP_START):
        return False
    if re.match(r'^[-*+] ', s):          # 无序列表
        return False
    if re.match(r'^\d+[.)] ', s):        # 有序列表
        return False
    if re.match(r'^[-*_]{3,}$', s):      # 分隔线
        return False
    return True


def split_paragraph(text):
    """把一个长段落切成若干段。"""
    parts = []
    for chunk in BOLD_SPLIT.split(text):
        merged = []
        for s in ENUM_SPLIT.split(chunk):
            if s == '':
                continue
            if merged and len(merged[-1]) < 6:   # 极短的开场语并入下一条
                merged[-1] += s
            else:
                merged.append(s)
        parts.extend(merged)
    return [p.strip() for p in parts if p.strip()]


def is_group_hint(line):
    """整行是斜体、且是 `## 标题` 后的第一行非空内容 -> 视为组提示。"""
    s = line.strip()
    return (len(s) > 2 and s.startswith('*') and not s.startswith('**')
            and s.endswith('*') and '*：' not in s[:3])


def reformat(path):
    raw = open(path, 'rb').read().decode('utf-8')
    nl = '\r\n' if '\r\n' in raw else '\n'
    lines = raw.replace('\r\n', '\n').split('\n')

    out = []
    stats = {'head': 0, 'split': 0, 'hint': 0}
    after_h2 = False
    for line in lines:
        if re.match(r'^## ', line):
            out.append(line)
            after_h2 = True
            continue

        if line.strip() == '':
            out.append(line)
            continue

        if after_h2:
            after_h2 = False
            if is_group_hint(line):
                inner = line.strip()[1:-1]
                m = STD_HINT.match(inner)
                if m:
                    out.append('> [!warning] 本组最容易被打穿的点')
                    out.append('> ' + m.group(1))
                else:
                    out.append('> [!warning] 本组提示')
                    out.append('> ' + inner)
                stats['hint'] += 1
                continue

        m = HEAD_RE.match(line)
        if m:
            out.append('### %s. %s' % (m.group(1), m.group(2)))
            out.append('')
            stats['head'] += 1
            continue

        if is_body(line):
            segs = split_paragraph(line)
            if len(segs) > 1:
                stats['split'] += 1
                for s in segs:
                    out.append(s)
                    out.append('')
                continue

        out.append(line)

    # 每段之间空一行；收拢连续空行
    cleaned = []
    for line in out:
        if line.strip() == '' and cleaned and cleaned[-1].strip() == '':
            continue
        cleaned.append(line)
    text = '\n'.join(cleaned).rstrip('\n') + '\n'
    open(path, 'wb').write(text.replace('\n', nl).encode('utf-8'))
    return stats


def strip_part_prefix(path):
    """问题.md：去掉每条问题前重复的【第一部分·项目一】标注。"""
    raw = open(path, 'rb').read().decode('utf-8')
    nl = '\r\n' if '\r\n' in raw else '\n'
    text = raw.replace('\r\n', '\n')
    new, n = re.subn(r'(?m)^(\d+\. )【第[一二]部分·[^】]+】', r'\1', text)
    open(path, 'wb').write(new.replace('\n', nl).encode('utf-8'))
    return n


if __name__ == '__main__':
    for name in sys.argv[1:]:
        if name == '问题.md':
            print(name, 'stripped', strip_part_prefix(BASE + '\\' + name))
        else:
            print(name, reformat(BASE + '\\' + name))
