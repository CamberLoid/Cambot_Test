#brainpower.py
"""
    做什么？
    合唱脑力啊

    想出来了！！！！！！
    一个函数不断判断是否有符合条件的更新 发现就return true
    另一个函数await 没有return true 超时则Exception
"""
import sys,asyncio,async_timeout
from cambot.utils import Logger
import telepot,telepot.aio,telepot.namedtuple
from telepot.aio.loop import MessageLoop
import random

class Chronical(object):
    """
        class Chronical(object) 合唱类
        大概的设计 针对每一个群组id实例化一个Brainpower
        -> Launcher.py
    """
    method = []
    def __init__(self, title, bot, *args, **kwargs):
        chronicalPool = [] #等待处理队列 用于判断超时什么的
        self._begin="{} 看起来有人合唱{} 本Bot也要来~~~".format("啊啦?",title)
        self._break="{} 没有人合唱了吗，好寂寞QAQ"
    pass
class brainpower(Chronical):
    """
        cambot.brainpower.Brainpower

        O-oooooooooo AAAAE-A-A-I-A-U- 
        JO-oooooooooooo AAE-O-A-A-U-U-A- 
        E-eee-ee-eee AAAAE-A-E-I-E-A-
        JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA(雾)
    """
    brainpowerBegin  = "Are you rea-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-"
    brainpower       = [
        "adrenaline","is","pumping","adrenaline","is","pumping",
        "generator","automatic","power",
        "atomic","atomic","overdrive",
        "blockbuster","brainpower","call","me","leader","cocaine",
        "don't","you","try","it","don't","you","try","it",
        "innovator","kill","machine","there",
        "is","no","fate","take","control","Brainpower",
        "let","the","bass","kick"]
    """脑力歌词"""
    
    brainpowerCore   = "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A-JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA"
    """脑力副歌"""
    def __init__(self, bot, *args, **kwargs):
        super().__init__("脑力",bot,*args, **kwargs)
        mode = random.choice([self.brainpowerBegin]+
                              self.brainpower+
                             [self.brainpowerCore])
        Logger.logger.log("Cambot.Brainpower initialized")
    
    def 


"""
    <TODO>蛮记录下模块化的理解
    大概是每个模块创建一个同名实例？
    pass
"""