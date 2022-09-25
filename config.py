__version__ = '2.0.0indev'

from color import Color

default_backpack = [
    'wooden_sword*1',
    'wooden_axe*1',
    'wooden_shovel*1',
    'electric_torch*1',
    'meat*4',
    'timber*50',
    'stone*50'
]

default_data = {
    'username': '',
    'health': 5,
    'balance': 0,
    'location': '',
    'date': 1,
    'daytime': 0,
    'active_balance': 6,
    'alive_enemy': {},
    'knowledge': []
}

recover_active_balance = 6

time_tips = ['早上8点', '上午10点', '正午12点', '下午3点', '下午5点', '晚上7点', '晚上10点', '午夜12点']
stochastic_events = [
    '你突然看见了一个老奶奶站在红绿灯旁，她看上去需要帮助。',
    '你遇到了一个乞丐，他衣衫褴褛，面前有一只破碗，貌似需要点钱。',
    '一个魁梧的男人挡住了你的去路，他看上去不好惹。',
]

debug_color = Color(Color.States.PLAIN, Color.Colors.GREEN)
info_color = Color(Color.States.PLAIN, Color.Colors.CYAN)
warn_color = Color(Color.States.PLAIN, Color.Colors.YELLOW)
fatal_color = Color(Color.States.PLAIN, Color.Colors.RED)
