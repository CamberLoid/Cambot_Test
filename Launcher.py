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
#Router -> 映射指令到函数 用不到
#动态import -> importlib 大概用不到

#系统库导入
import os
import sys
import time,threading,asyncio

#telepot模块导入
import telepot, telepot.aio, telepot.namedtuple
from telepot.aio.loop import MessageLoop

#cambot导入
#from cambot import generalhandler as handle #暂时用不上
from cambot.utils import Logger

def theWorldTheEndingTheUltimateAnswer():
    return 16

sessionPool = {}
"""
    dict:sessionPool
    预期配对: id : instance 
    大概只会在脑力上面用到 =v=
"""

activatedCommands = {"brainpower":"brainpower","study":"updatefile",
                    "register":"killMachine","":""}
"""
    dict:activatedCommands
    str(command) : func
    <TODO> 把硬编码改了
"""
TUser = []
"""
"""
      
async def updateModule(user_id,msg):
    replymsg = []
    if user_id in TUser:
        pass
    else:
        Logger.logger.log("Warning::User ID {} is Trying to Access Modulefile")
        pass

isChecked = False
async def messagehandler(msg):
    flavor=telepot.flavor(msg)
    content_type, chat_type, chat_id = telepot.glance(msg,flavor=flavor)
    if not isChecked:
        isChecked = True
        t = bot[0].getMe()
        Logger.logger.log("{}".format())
    _msg = telepot.namedtuple.Message(**msg) #**->dict
    if content_type == 'file':
        pass

token = sys.argv[1]
bot = []
for i in token:
    bot.append(telepot.aio.Bot(i))
Logger.logger.log(len(bot))
loop = asyncio.get_event_loop()

for bots in bot:
    loop.create_task(MessageLoop(bots,messagehandler).run_forever())

Logger.logger.log("Engaged Cambot")
loop.run_forever()