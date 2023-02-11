# -*- coding: utf-8 -*
'''
new Env('闪电猫机场签到');
'''

import os
import datetime
import requests 
from notify import send  # 导入青龙消息通知模块

#读取闪电猫机场COOKIES
cookie = os.environ['SPEEDCAT_COOKIE']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.191.400 QQBrowser/11.5.5245.400',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': cookie,
}

url='https://aff03.speedcat-aff02.com/user/checkin'
post_data = ''

def main(*args):

    html_code = requests.session().post(url, data=post_data, headers=headers).json()
    print(html_code)
    #{"msg":"您获得了 0 MB流量","ret":1}
    #{'ret': 0, 'msg': '您似乎已经签到过了...'}

    if html_code['ret']==1:
        end('闪电猫机场签到', '💖签到成功\n\n本通知 By HY-闪电猫机场\n通知时间:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        send('闪电猫机场签到', '💖签到失败\n\n本通知 By HY-闪电猫机场\n通知时间:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    main()
