#!/usr/bin/env python
from random import randint

count = 0
number = randint(1, 10)

while True:
    try:
        count += 1
        guess = int(input('请输入一个数字，这是第 {0} 次 ：'.format(count)))
    except ValueError:
        print('类型为数字，请重新输入：')
        continue
    if guess < number:
        print('你输入的数字是{0},猜小了'.format(guess))
        continue
    if guess > number:
        print('你输入的数字是{0},猜大了'.format(guess))
        continue
    if guess == number:
        bool = True
        print('你输入的数字是{0},恭喜猜对了，总共答了 {1} 次。'.format(guess, count))
        while True:
            select = input('是否要继续游戏 y/n ？')
            if select.lower() == 'y':
                count = 0
                break
            elif select.lower() == 'n':
                bool = False
                break
            else:
                continue
        if bool == False:
            break
