#!/usr/bin/env python3
import requests
import csv

def main():
    url = 'https://www.zhihu.com'
    m_data = '/api/v3/feed/topstory/recommend?session_token=653f4a3d6760b9c0003fdcf9aee5d1ea&desktop=true&page_number=2' \
             '&limit=6&action=down&after_id=5'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'cookie': '_zap=41370ef5-5d14-491a-8775-7eea329192b4; d_c0="AIAjnROn8w-PTg4t9UxY9AY4OuWnQ6lO8Kk=|1566829289"; _xsrf=0dfc91d1-5de1-4b26-a383-b6655f162925; tgw_l7_route=e9ff3200fd05d0af15498c125aecf1a1; capsion_ticket="2|1:0|10:1567265081|14:capsion_ticket|44:ZDBkZWUyNWNmODVjNDEwMTg4Mjk4NDgyYzI4OTNiZmY=|79ef25352b767c0d328c4759a7d4dca060822bfd655a93a16d1eddd808c06259"; z_c0="2|1:0|10:1567265173|4:z_c0|92:Mi4xQW5QTkFnQUFBQUFBZ0NPZEU2ZnpEeVlBQUFCZ0FsVk5sZDlYWGdDVDB4Ml9JLXdwaDIyWklsTF9MTDY4dzZFZGxn|02f21ec044dfcab05e01a4f84687663002d6db6a30657642646edfad858a49ef"; tst=r'
    }

    js_data = requests.get(url=url + m_data, headers=headers).json()['data']
    rows = []
    for i in range(len(js_data)):
        one_dict = {}
        try:
            one_dict['分类'] = js_data[i]['action_text']
            one_dict['标题'] = js_data[i]['target']['question']['title']
            one_dict['作者'] = js_data[i]['target']['author']['name']
            one_dict['链接'] = url + '/question/{q_id}/answer/{a_id}'.format(q_id=js_data[i]['target']['question']['id'],
                                                                           a_id=js_data[i]['target']['id'])
        except KeyError:
            continue
        finally:
            print(one_dict)
            rows.append(one_dict)

    with open('./files/zhihu_fresh.csv', 'w') as f:
        head = ['分类', '标题', '作者', '链接']
        csv_file = csv.DictWriter(f, head)
        csv_file.writeheader()
        csv_file.writerows(rows)

if __name__== '__main__':
    main()
