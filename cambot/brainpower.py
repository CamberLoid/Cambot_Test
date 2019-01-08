#brainpower.py
"""
    做什么？
    合唱脑力啊
"""
import sys
from Logger import *

class Chronical(object):
    """
        class Chronical(object) 合唱类
        大概的设计 针对每一个群组id实例化一个Brainpower
        -> Launcher.py
    """
    method = []
    def __init__(self, title, *args, **kwargs):
        self._begin="{} 看起来有人合唱{} 本Bot也要来~~~".format("{}",title)
        self._break="{} 没有人合唱了吗，好寂寞QAQ"
        
    
    pass
class Brainpower(Chronical):
    """脑力歌词"""
    brainpower       = [
        "adrenaline","is","pumping","adrenaline","is","pumping",
        "generator","automatic","power",
        "atomic","atomic","overdrive",
        "blockbuster","brainpower","call","me","leader","cocaine",
        "don't","you","try","it","don't","you","try","it",
        "innovator","kill","machine","there",
        "is","no","fate","take","control","Brainpower",
        "let","the","bass","kick"]
    """脑力副歌"""
    brainpowerCore   = "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A-JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().method.append("Brainpower")
        logger.log("Cambot.Brainpower initialized")
        
    def listen(self):
        pass

def __init__():
    reg = ["/brainpower","::text"]
    print("Imported {}")

if __name__ == "__main__":
    pass