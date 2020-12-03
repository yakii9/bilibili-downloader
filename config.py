# _*_ coding: utf-8 _*_
"""
@Author     : tyler
@Email      : tyler_d1128@outlook.com
@Project    : bilibili-video-download 
@File       : config.py
@License    : GNU GENERAL PUBLIC LICENSE
"""
from requests import session
from bilibili_api import Verify
from json import loads

with open('config.json', 'rt', encoding='utf-8') as f:
    user_config = loads(f.read())
config = {
    'BILIBILI': {
        'SESSDATA': user_config['BILIBILI_ACCOUNT']['SESSDATA'],
        'CSRF': user_config['BILIBILI_ACCOUNT']['CSRF'],
    },
    'DATA_PATH': user_config['DATA_PATH'],
    'THREAD': user_config['THREAD']['NUM'],
    'SEGMENT': {
        "MAX_SIZE": user_config['SEGMENT']['MAX_SIZE'],
        "MIN_SIZE": user_config['SEGMENT']['MIN_SIZE'],
    },
}

verify = Verify(sessdata=config['BILIBILI']['SESSDATA'], csrf=config['BILIBILI']['CSRF'])


def get_session():
    sessions = session()
    sessions.headers.update({
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Safari/537.36',
        'Origin': 'https://www.bilibili.com',
    })
    return sessions

