#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv


def get_html(page):
    url = 'https://sh.lianjia.com/zufang/pg{0}'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Host': 'sh.lianjia.com'
    }
    respone = requests.get(url, headers=headers)
    return respone.text


def get_content(html, page):
    item_url = "https://sh.lianjia.com"
    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find_all('div', class_='content__list--item--main')
    all_info = []
    number = 30 * (page - 1) + 1

    for i in all_data:
        title = i.contents[1].get_text().strip()
        href = item_url + i.find('a').get('href')
        info = [number, title, href]
        for item in i.find('p', class_='content__list--item--des').get_text().strip().split('/'):
            info.append(item.strip().replace(' ', ''))
        all_info.append(info)
        print('正在采集第 {0} 条'.format(number))
        number += 1
    return all_info


def save_csv(rows):
    with open('./files/lianjia_bs4.csv', 'a') as f:
        csv_file = csv.writer(f)
        csv_file.writerows(rows)


if __name__ == '__main__':
    with open('./files/lianjia_bs4.csv', 'a') as f:
        head = ['编号', '标题', '链接', '地点', '面积', '朝向', '布局', '楼层']
        csv_file = csv.writer(f)
        csv_file.writerow(head)

    # 采集 10 页
    for page in range(1, 11):
        save_csv(get_content(get_html(page), page))
    print('信息采集结束')
