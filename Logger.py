import sys
import time
import os
"""
    Cambot Logger
"""
class logger:
    class WritableException(Exception):
        pass
    def logToFile(self,message,file="Launcher.log"):
        with open(file,"a") as f:
            if not f.writable:
                raise WritableException
            f.write(message)
    """
    Logger For Cambot
    """       
    def log(self,msg,mod=None,file=None):
        isValidFile=True
        output = "[{}:{}:{}] {}"
        t = time.gmtime()
        curtime = [t.tm_hour,t.tm_min,t.tm_sec]
        output=output.format(curtime[0],curtime[1],curtime[2],msg)
        print(output)
        try:
            if mod == 'f' or 'file':
                if file==None:
                    logToFile(msg,file)
        except WritableException:
            log("Error ["+msg+"] Cannot be written ./to Launcher.log, falling to console log")
            isValidFile=False
        finally:
            return