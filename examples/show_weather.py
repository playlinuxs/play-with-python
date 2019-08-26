#!/usr/bin/env python3
import requests

while True:
    city = input('请输入城市，按 q 退出： ')
    response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city={city}'.format(city=city))

    if city == 'Q' or city == 'q':
        break
    if response.json()['status'] != 1000:
        print('城市名字错误，请重新输入。')
        continue

    today_weather = response.json()['data']['forecast'][0]
    [print(today_weather[item]) for item in ['date', 'high', 'low', 'type']]
