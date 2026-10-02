# -*- coding: utf-8 -*-
"""Notion MCP streamable-HTTP 直连客户端（无状态）"""
import json, os, sys, urllib.request, urllib.error

_cfg = json.loads(os.environ['CODEBUDDY_MCP_CONFIG'])['mcpServers']['notion']
URL = _cfg['url']
HEADERS = dict(_cfg['headers'])
HEADERS.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/event-stream',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
})

def _post(payload):
    req = urllib.request.Request(URL, data=json.dumps(payload).encode('utf-8'), headers=HEADERS, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            body = r.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        raise RuntimeError('HTTP %d: %s' % (e.code, e.read().decode()[:500]))
    data = None
    if body.lstrip().startswith('{'):
        data = json.loads(body)
    else:
        for line in body.splitlines():
            if line.startswith('data:'):
                data = json.loads(line[5:].strip())
    if data is None:
        raise RuntimeError('no data in response')
    if 'error' in data:
        raise RuntimeError(json.dumps(data['error'], ensure_ascii=False)[:2000])
    return data['result']

def call(tool, args):
    res = _post({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
                 'params': {'name': tool, 'arguments': args}})
    if res.get('isError'):
        raise RuntimeError(json.dumps(res, ensure_ascii=False)[:5000])
    txts = []
    for c in res.get('content', []):
        if c.get('type') == 'text':
            txts.append(c['text'])
    return '\n'.join(txts)

if __name__ == '__main__':
    out = call(sys.argv[1], json.loads(sys.argv[2]) if len(sys.argv) > 2 else {})
    print(out if len(sys.argv) <= 3 else out[:int(sys.argv[3])])
