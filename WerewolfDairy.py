from random import randint

from backpack import Backpack
from config import *
from functions import *
from item import *

data = get_data()
backpack = Backpack(get_backpack())


def main():
    verify_username()
    while data['health'] > 0:
        print()

        info('第' + str(data['date']) + '天')
        if data['active_balance'] > 0:
            update_daytime()
            info('现在是' + time_tips[data['daytime']])

            act_home = input('你要干什么？[1.去大街上逛逛 2.去森林打猎 3.待在家里] (按q保存并退出): ')
            if act_home in ['1', '去大街上逛逛']:
                visit_street()
            elif act_home in ['2', '去森林打猎']:
                visit_forest()
            elif act_home in ['3', '待在家里']:
                pass
            elif act_home == 'q':

                break
        else:
            print('夜幕降临，你感到很疲惫，回到家便开始了休息……')
            data['date'] += 1
            data['daytime'] = 0
            data['active_balance'] = recover_active_balance

    if data['health'] <= 0:
        print('你被怪物插穿了胸膛，死亡的恐惧攫住了你的心。')
        print('“不，我不想死！”你大喊，狰狞的声音回荡在冷寂的森林。')
        print('次日，政府的探险队找到了你，队长在你残缺不全的尸体上发现了一本日记……')
        info(f'\n你的名字：{data["username"]}\n你的财产：{data["balance"]}\n{backpack.get_formatted_items()}')


def save_data():
    save('data\\data.json', data)
    save('data\\backpack.json', backpack.get_formatted_items())


def update_daytime():
    if data['daytime'] < 5:
        if data['active_balance'] == 6:
            data['daytime'] = 0
        elif data['active_balance'] == 5:
            data['daytime'] = 1
        elif data['active_balance'] == 4:
            data['daytime'] = 2
        elif data['active_balance'] == 3:
            data['daytime'] = 3
        elif data['active_balance'] == 2:
            data['daytime'] = 4
        elif data['active_balance'] == 1:
            data['daytime'] = 5


def visit_forest():
    data['active_balance'] -= 1
    print('正在通向森林……')
    while data['active_balance'] > 0:
        print()

        act_forest = input('你来到了森林，你要做什么？[1.搜索 2.挖掘 3.砍伐] (按q返回)')
        if act_forest in ['1', '搜索']:
            data['active_balance'] -= 1

            blueprint = random_choice(
                [
                    Items.BLUEPRINT_CHAINSAW,
                    Items.BLUEPRINT_IRON_TOOLS,
                    Items.BLUEPRINT_GOLDEN_TOOLS
                ],
                0.05
            )
            if blueprint is not None:  # TODO 验证蓝图是否重复获得
                backpack.add_item(blueprint)
                print(f'你太辛运了，你找到了一张图纸：[{str(blueprint)}]')

            meat = randint(0, 3)
            mushroom = randint(0, 5)
            backpack.add_item(Items.MEAT, meat)
            backpack.add_item(Items.MUSHROOM, mushroom)
            info(f'找到了 {Backpack([f"肉*{meat}", f"蘑菇*{mushroom}"]).get_formatted_items()}')
            info('现在是' + time_tips[data['daytime']])
        elif act_forest in ['2', '挖掘']:
            pass
        elif act_forest in ['3', '砍伐']:
            pass
        elif act_forest == 'q':
            break


def visit_street():
    while data['active_balance'] > 0:
        print()

        print('你出了家门，外面是热闹的大街。')
        print('可以去的地方：[1.路边 2.城郊]')
        act_street = input('你要去哪里？(按q返回)')

        if act_street in ['1', '路边']:
            print('你走到了路边，这里有很多人在摆摊，贸易或者干些其他的事，看上去治安不怎么好')

            rand = random_choice(stochastic_events, 0.3)
            if rand is not None:
                print(rand)
                # TODO 事件对应的任务 奖励等
        elif act_street in ['2', '城郊']:
            print('你来到了街道的尽头，这里已经是城郊了，四周是破烂的街道，到处都笼罩着贫穷腐朽的气息')
            # TODO 随机怪物
        elif act_street == 'q':
            break
        else:
            warn('你好像不记得有这个地方')


def verify_username():
    if not data['username']:
        while not data['username']:
            username = input('你的昵称是: \033[1m')
            print('\033[0m', end='')
            if not username.strip():
                warn(f'”{username}“不是一个有效的昵称，请重新输入！')
            else:
                print(f'\n剧情：曙光破晓，怪物停止了杀戮，幸存者从新一天的阳光中醒来。你叫{username},是东镇的一个合法居民。')
                print('你住在东镇东区外围，这里濒临城郊，晚上就是怪物的天堂。')
                print('你的剧情从8点开始，晚上10点结束，一天有6次活动时间。')
                print('肉和蘑菇都是你生存的必需品，肉能保证你不被饿死。')
                print('肉还能用来换取金币，蘑菇也是制汤或制药的好材料。你可以去森林搜索来获得它们。')
                print('这个小镇有很多的特殊剧情，玩家要自行探索。')
                print('现在开始你的日记')

                data['username'] = username


if __name__ == '__main__':
    main()
