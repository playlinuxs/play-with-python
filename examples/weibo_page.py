#!/usr/bin/env python3

import requests

url = 'https://weibo.com/a/hot/realtime'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie':
        'grow-G0=6fd5dedc9d0f894fec342d051b79679e; SUB=_2AkMqNgfEf8NxqwJRmP4Rz\WjlbIx2zAvEieKcavYfJRMxHRl-yT83qk0OtRB6AbYpKjflxGZlDbjVD6PMcpL7gIPSyRxJ; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWypLyadvsYBDp7c9_H_3lR; YF-V5-G0=4358a4493c1ebf8ed493ef9c46f04cae; WBStorage=f54cf4e4362237da|undefined'
}
response = requests.get(url, headers=headers)
with open('./files/weibo_page.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
