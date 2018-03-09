# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:44:31 2018

@author: xydroot

获取12306城市名和城市代码的数据
文件名： parse_station.py
"""
import requests
import re

#关闭https证书验证警告
requests.packages.urllib3.disable_warnings()
# 12306的城市名和城市代码js文件url
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
r = requests.get(url,verify=False)
pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
result = re.findall(pattern,r.text)
station = dict(result)
# 将站点词典 保存到 csv 文件中，
with open("station.csv","w") as fhandler:
    fhandler.write('站点名称NAME' + ',' + '站点编码ID' + '\n')
    for stat in station.items():
        fhandler.write(stat[0] + ',' + stat[1] + '\n')
fhandler.closed
