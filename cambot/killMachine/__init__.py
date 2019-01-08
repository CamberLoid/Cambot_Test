"""
    cambot.killMachine.__init__
    是一个用来记录杀人案(雾) 音游记录的模组
    (太菜了不会用装饰器)
    需要调用库 json base64 {ocr}->apiurl/大概是azure {imageedit}
    <TODO> 需要请求帮助分游戏添加杀人识别代码 
    <TODO> 可以把cytus2的写了,比arc好写的多
    
    组织:
    killMachine下将有比较多的.py文件（都是空的，别看了，明天考高数
    包含一个与文件名同名的[example]class cytys2(),作为统一返回的值

    
    统一的返回值

"""
import json
import base64
class ArgumentError(Exception):
    pass
class killMachine(object):
    def __init__(self,apiurl,*args,**kwargs):
        if apiurl is str:
            _apiurl=apiurl
        else:
            raise ArgumentError()
        
