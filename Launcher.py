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
"""
    2.   我想让这个bot做什么？
    2.1. 合唱脑力 /brainpower 或者 自动合唱
    2.2. MUG杀人登记+图像处理库 +
    2.3. <TODO>改写为异步处理
"""
import os
import sys
#初始化导入
sys.path.append('.\\telepot-master')
sys.path.append('.')
import telepot,telepot.aio,time,threading
from cambot import *
import Logger

def theWorldTheEndingTheUltimateAnswer():
    return 

def messagehandle(msg):
    pass
modules = []
modules.append(cambot.brainpower())

token = []
token.append("714345613:AAGbEL0LhzXakqfqkmEyggvMOO8ZVHwT87g")
#个人测试用token,发布时移除
bot = []
for i in token:
    bot.append(telepot.Bot(i))

while True:
    time.sleep(1)