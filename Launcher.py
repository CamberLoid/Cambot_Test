#<TODO>
#做出脑力bot作为测试
#有时间写bot还不去写开题报告和策划
#
"""
    <TODO>
    Python-Async
    Brainpowerbot
    Killbot
    Cambot-Launcher
"""
""" 1.   使用的模组
         telepot.Bot, 
         ~~暂时没有delegate 因为看不懂~~ delegate -> 委托，针对某用户/群组/频道
    2.   我想让这个bot做什么？
    2.1. 合唱脑力 /brainpower 或者 自动合唱
    2.2. MUG杀人登记+图像处理库 +
    2.3. <TODO>改写为异步处理
    3.   可能会自己写个wrapper/或者自己基于需求调用api
"""
#个人纪录
#Router -> 映射指令到函数
#动态import -> importlib

import os
import sys
#初始化导入
sys.path.append('.\\telepot-master')
sys.path.append('.')
import telepot
import telepot.aio
import time,threading,asyncio
from cambot import *

def theWorldTheEndingTheUltimateAnswer():
    pass

def importmod():
    pass

def messagehandle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pass
async def runBot(bots):
    await asyncio.wait(1)
token = sys.argv[1:]
if token.count is 0:
    token.append("714345613:AAGbEL0LhzXakqfqkmEyggvMOO8ZVHwT87g")
#个人测试用token,发布时移除
bot = []
for i in token:
    bot.append(telepot.Bot(i))

while True:
    time.sleep(1)