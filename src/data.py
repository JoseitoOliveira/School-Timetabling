"""
Definições do logger

@authors	joseito.junior@brphotonics.com
@date   	20/01/2022

"""

import os.path
import json


default = {
    'device_index': 0,
    'width': 1920,
    'height': 1080,
    'path': './pictures/',
    'types': [
        'SMF',
        'UHUNA_4_Panda',
        'UHUNA_7_Panda',
    ],
}

if not os.path.isfile('data.json'):
    with open('data.json', mode='w', encoding='utf8') as f:
        json.dump(default, f)

with open('data.json', mode='r', encoding='utf8') as f:
    data: dict = json.load(f)


def data_update(key, value):
    data[key] = value
    with open('data.json', mode='w', encoding='utf8') as f:
        json.dump(data, f)
