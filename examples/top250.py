#!/usr/bin/env python3
import requests
import csv


class top250(object):

    def __init__(self, start, apikey='0df993c66c0c636e29ecbb5344252a4a'):
        self.start = start
        self.apikey = apikey
        self.url = 'https://api.douban.com/v2/movie/top250?start={start}&apikey={apikey}'.format(start=self.start,
                                                                                                 apikey=self.apikey)
        self.movies_json = requests.get(self.url).json()['subjects']

    def movies_data(self):
        movies = []
        for i in range(len(self.movies_json)):
            single_movie = []
            for item in self.movies_json[i]['title'], self.movies_json[i]['rating']['average'], self.movies_json[i][
                'year'], self.movies_json[i]['directors'][0]['name'], self.movies_json[i]['alt']:
                single_movie.append(item)
            print(self.movies_json[i]['title'] + ' is OK.')
            movies.append(single_movie)
        return movies

    def save_csv(self):
        with open('./files/top250.csv', 'a', encoding='utf-8') as f:
            csv_file = csv.writer(f)
            csv_file.writerows(self.movies_data())


if __name__ == '__main__':
    with open('./files/top250.csv', 'w', encoding='utf-8') as f:
        header = ['电影名称', '评分', '上映时间', '导演', '链接信息']
        csv_file = csv.writer(f)
        csv_file.writerow(header)
    for i in range(0, 250, 20):
        gogo = top250(i)
        gogo.save_csv()
    print('豆瓣电影 Top 250 统计完毕。')
