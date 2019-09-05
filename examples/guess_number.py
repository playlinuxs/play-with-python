#!/usr/bin/env python

count = 0
for i in range(3):
     try:
         number = int(input('请输入一个数字，还可以猜 {0} 次 ：'.format(3 - count)))
         count += 1
     except ValueError:
         print('类型为数字，请重新输入：')
         count += 1
         continue
     if number < 10 :
         print('你输入的数字是{0},猜小了'.format(number))
     if number > 10:
         print('你输入的数字是{0},猜大了'.format(number))
     if number == 10:
         print('你输入的数字是{0},恭喜猜对了'.format(number))
