from random import random, randint

from config import *
from functions import *

data = get_data()


def main():
    verify_username()
    while data['health'] > 0:
        info('第' + str(data['date']) + '天')
        if data['active_balance'] > 0:
            info("现在是" + time_tips[data['daytime']])

            act_home = input("你要干什么？[1.去大街上逛逛 2.去森林打猎 3.待在家里] (按q保存并退出): ")
            if act_home in ['1', '去大街上逛逛']:
                visit_street()
            elif act_home in ['2', '去森林打猎']:
                pass
            elif act_home in ['3', '待在家里']:
                pass
            elif act_home == 'q':
                save('data\\data.json', data)
                break
        else:
            data['date'] += 1
            data['daytime'] = 0
            data['active_balance'] = 6
        print()


def visit_forest():
    pass


def visit_street():
    while data['active_balance'] > 0:
        print('你出了家门，外面是热闹的大街。')
        print('可以去的地方：[1.路边 2.城郊]')
        act_street = input('你要去哪里？(按q返回)')

        if act_street in ['1', '路边']:
            print('你走到了路边，这里有很多人在摆摊，贸易或者干些其他的事，看上去治安不怎么好')

            if random() > 0.5:
                print(stochastic_events[randint(0, 2)])
                # TODO 事件对应的任务 奖励等
        elif act_street in ['2', '城郊']:
            print('你来到了街道的尽头，这里已经是城郊了，四周是破烂的街道，到处都笼罩着贫穷腐朽的气息')
            # TODO 随机怪物
        elif act_street == 'q':
            break
        else:
            warn('你好像不记得有这个地方')
        print()


def verify_username():
    if not data['username']:
        while not data['username']:
            username = input('你的昵称是: \033[1m')
            print('\033[0m', end='')
            if not username.strip():
                warn(f'"{username}"不是一个有效的昵称，请重新输入！')
            else:
                print(f'\n剧情：曙光破晓，怪物停止了杀戮，幸存者从新一天的阳光中醒来。你叫{username},是东镇的一个合法居民。')
                print('你住在东镇东区外围，这里濒临城郊，晚上就是怪物的天堂。')
                print('你的剧情从8点开始，晚上10点结束，一天有6次活动时间。')
                print('食物和蘑菇都是你生存的必需品，食物能保证你不被饿死。')
                print('食物还能用来换取金币，蘑菇也是制汤或制药的好材料。你可以去森林搜索来获得它们。')
                print('这个小镇有很多的特殊剧情，玩家要自行探索。')
                print('现在开始你的日记')

                data['username'] = username
            print()


if __name__ == '__main__':
    main()
