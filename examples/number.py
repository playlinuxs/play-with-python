#!/usr/bin/env python


while True:
    number = input('请输入一个数字：')
    try:
        if isinstance(int(number),int):
            print('你输入的数字为 {0}'.format(number))
            break
    except ValueError:
            print('输入的不是数字，请重新输入：')
            continue
