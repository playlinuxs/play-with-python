#!/usr/bin/env python3
from random import randint

name = input("请输入你的名字：")

playtime = 0  # 玩的次数
lun = 0  # 每次猜的轮数
lun_list = []  # 每次总轮数的列表

while True:
    playtime += 1  # 外部控制游戏次数，每次循环加 1
    number = randint(1, 5)  # 随机数不变必须放外循环

    while True:  # 内部循环控制每次猜数字的轮数
        guess = int(input('请输入一个 1- 5 的数字：'))

        lun += 1  # 每猜一次 轮数加 1

        if guess < number:
            print('猜小了，再试试')
            continue
        elif guess > number:
            print('猜大了，再试试')
            continue
        else:
            print('猜对了,一共猜了 {0} 轮'.format(lun))
            lun_list.append(lun)  # 把每次猜对后对结果追加到列表，便于统计
            min_lun = min(lun_list)  # 最小轮数
            average_lun = sum(lun_list) // len(lun_list)  # 平均轮数
            lun = 0  # 猜对之后，把轮数归位到 0
            break

    print('{0}, 你已经玩了 {1} 次，最少 {2} 轮猜出答案，平均 {3} 轮猜出答案'.format(name, playtime, min_lun, average_lun))

    print('按任意键继续，回车退出')
    if not input():
        with open('./files/number.txt', 'w') as f:
            f.write('姓名：{0}\n'.format(name))
            f.write('总游戏次数：{0}\n'.format(playtime))
            f.write('最快猜出轮数：{0}\n'.format(min_lun))
            f.write('猜过的总轮数：{0}\n'.format(sum(lun_list)))
        print('游戏统计已保存到 {0} ,退出游戏，欢迎下次再来！'.format('./files/number.txt'))
        break
    else:
        continue
