#<TODO>
#做出脑力bot作为测试
#有时间写bot还不去写开题报告和策划和复习
#
"""
    <TODO>
    Python-Async
    Brainpowerbot
    Killbot
    Cambot-Launcher
    你见到的每一个pass 都是我的下一个todo
"""
""" 1.   使用的模组
         telepot.Bot, 
         ~~暂时没有delegate 因为看不懂~~ delegate -> 委托，针对某用户/群组/频道
    2.   我想让这个bot做什么？
    2.1. 合唱脑力 /brainpower 或者 自动合唱
    2.2. MUG杀人登记+图像处理库 +
    2.3. <TODO>改写为异步处理
    2.4. 目前只想实现单一目标
    3.   可能会自己写个wrapper/或者自己基于需求调用api
"""
#个人纪录
#Router -> 映射指令到函数
#动态import -> importlib

import os
import sys
#初始化导入
#sys.path.append('.\\telepot-master')
#sys.path.append('.')
import telepot,telepot.aio,telepot.namedtuple
from telepot.aio.loop import MessageLoop
import time,threading,asyncio
import cambot
from cambot import generalhandler as handle
from cambot.utils import Logger

def theWorldTheEndingTheUltimateAnswer():
    return 16
    
def importmod(direction):
    """
    <TODO>
    """
    pass

session = {}
"""
    dict:session
    预期配对: id : instance 
    大概只会在脑力上面用到 =v=
"""

activatedCommands = {"brainpower":"brainpower","study":"updatefile",
                    "register":"killMachine","":""}
"""
    dict:activatedCommands
    str:command : func
    <TODO> 把硬编码改了
"""
def commandHandler(command,msg):
    """
    """

    if command is not list:
        return []

    if command[0].lower == 'brainpower':
        session[msg.chat.id] = cambot.brainpower.Brainpower()
    if command[0].lower == 'register':
        if msg.chat.id >0: #个人对话
            pass
        else: #群组
            pass
        pass
    if command[]
    
    pass

def messagehandler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    _msg = telepot.namedtuple.Message(**msg)
    if _msg.text is not None:
        if _msg.text[0] is '/':
            replymessage = commandHandler(_msg.text[1:].split(' '),_msg)

importmod(direction="cambot")
token = sys.argv[1:]

if len(token) is 0:
    token.append("714345613:AAGbEL0LhzXakqfqkmEyggvMOO8ZVHwT87g") 
    #个人测试用token,因为已经Expired所以保留,要用的话自己删掉

bot = []
for i in token:
    bot.append(telepot.aio.Bot(i))
Logger.logger.log(len(bot))
loop = asyncio.get_event_loop()

for bots in bot:
    Logger.logger.log("{}".format(bots.getMe()))
for bots in bot:
    loop.create_task(MessageLoop(bots,messagehandler).run_forever())

Logger.logger.log("Engaged Cambot")
loop.run_forever()