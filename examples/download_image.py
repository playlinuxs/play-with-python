#!/usr/bin/env python3

import requests

# get image url
js = requests.get('https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a').json()
image_url = js['image']

# get image data
response = requests.get(image_url)
img = response.content

# write local file
try:
    with open('files/xiaoshenke.jpg', 'wb') as f:
        f.write(img)
        print('Image download success!')

except FileNotFoundError as e:
    print('ERROR,Please check file path.')

except ValueError as e:
    print('ERROR,Please check file args')
