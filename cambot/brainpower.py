#brainpower.py
"""
    做什么？
    合唱脑力啊
"""
import sys,asyncio,async_timeout
from cambot.utils import Logger
import telepot,telepot.aio,telepot.namedtuple
from telepot.aio.loop import MessageLoop

class Chronical(object):
    """
        class Chronical(object) 合唱类
        大概的设计 针对每一个群组id实例化一个Brainpower
        -> Launcher.py
    """
    method = []
    def __init__(self, title, bot, *args, **kwargs):
        self._begin="{} 看起来有人合唱{} 本Bot也要来~~~".format("啊啦?",title)
        self._break="{} 没有人合唱了吗，好寂寞QAQ"
        
    
    pass
class Brainpower(Chronical):
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

        Logger.logger.log("Cambot.Brainpower initialized")
        
    def listen(self):
        pass
    async def timeout(self,curiter):
        try:    
            while 1:
                if self._get.lower..split(' ') 
                    return
                else:

        except asyncio.
            pass
    async def updateStatus(parameter_list):
        try:
            await asyncio.wait_for(timeout,)
        except asyncio.TimeoutError:

    

def __init__():
    reg = ["/brainpower","::text"] #预计要让上层程序读取
    print("Imported {}")

if __name__ == "__main__":
    pass