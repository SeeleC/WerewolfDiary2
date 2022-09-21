from config import *
from functions import *
from text import *

data = get_data()

if not data['username']:
    username = input('你的用户名是: ')
