#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'https://fe-api.zhaopin.com/c/i/sou?start=10&pageSize=10&kw=python&kt=3'


def get_des(des_url):
    '''

    :param des_url: 有岗位职责的 URL 地址
    :return:  返回岗位职责的 文本信息
    '''
    headers = {
        'UserAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'sec-fetch-user': '?1',
        'referer': des_url,
        'sec-fetch-mode': 'navigate',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'cookie': 'x-zp-client-id=fbca7395-2467-4671-deb6-d5dc1f70b8f3; sts_deviceid=16d10d1d9b12d8-0fb8abba57f662-38637501-1296000-16d10d1d9b27f1; sou_experiment=capi; urlfrom2=121126445; adfcid2=none; adfbid2=0; LastCity=%E6%B7%B1%E5%9C%B3; LastCity%5Fid=765; acw_tc=2760826a15679498710024257e7615f156ae3631e718623ed990a025cdd082; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fcrossincode.com%2Fvip%2Fhomework%2F30%2F; jobRiskWarning=true; dywea=95841923.720504351528878600.1567945252.1567948582.1568520919.3; dywec=95841923; dywez=95841923.1568520919.3.3.dywecsr=crossincode.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/vip/homework/30/; __utma=269921210.1991216172.1567945252.1567948582.1568520920.3; __utmc=269921210; __utmz=269921210.1568520920.3.3.utmcsr=crossincode.com|utmccn=(referral)|utmcmd=referral|utmcct=/vip/homework/30/; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1567945252,1568520920; ZP_OLD_FLAG=false; POSSPORTLOGIN=6; CANCELALL=1; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568521267; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d10d1da9e508-00e33c9efd9ff3-38637501-1296000-16d10d1da9fb73%22%2C%22%24device_id%22%3A%2216d10d1da9e508-00e33c9efd9ff3-38637501-1296000-16d10d1da9fb73%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_sc__v2=5d7dd358cc7464ad6df6c7f0acdfc8c566374e04; sts_sid=16d3381aa37bad-0b1d7e0385159e-38607501-1296000-16d3381aa38a4e; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%225c165a32-77d2-4a42-9d34-87dadecb45df-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22e895b2d2-2445-484a-a209-37c4e1c23004-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_evtseq=8'

    }
    response = requests.get(des_url, headers=headers)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')
    job_text = soup.find_all('div', class_='describtion__detail-content')[0].get_text()
    return job_text


def get_info(url):
    '''
    :param url: 相关岗位的 API 信息
    :return: 返回所有相关工作需要提取的信息
    '''
    response = requests.get(url).json()
    time.sleep(0.3)
    all_jobs = []
    for i in range(len(response['data']) - 1):
        job_info = []
        jobname = response['data']['results'][i]['jobName']
        salaery = response['data']['results'][i]['salary']
        eduLevel = response['data']['results'][i]['eduLevel']['name']
        workingExp = response['data']['results'][i]['workingExp']['name']
        company = response['data']['results'][i]['company']['name']
        positionURL = response['data']['results'][i]['positionURL']
        job_des = get_des(positionURL)
        for i in jobname, salaery, eduLevel, workingExp, company, positionURL, job_des:
            job_info.append(i)
        all_jobs.append(job_info)
        print('正在收集职位信息 「{0}」'.format(jobname))
    return all_jobs


def main():
    with open('./files/zhilian.csv', 'w') as f:
        csv_file = csv.writer(f)
        csv_file.writerows(get_info(url))


if __name__ == '__main__':
    main()
