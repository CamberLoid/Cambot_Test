__module_name__ = "CYTUS II ocr module for MUGMurderer"
__author__ = "Camber"
#With azure OCR
import asyncio,os,sys
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
from pprint import pprint
import collections
async def analyzeLocal(imagePath, subscription_key, language='unk'):
    #Azure的ocr api逻辑
    azureVisionURL = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
    ocrURL = azureVisionURL + "ocr"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params  = {'language': language, 'detectOrientation': 'true'}
    with open(imagePath,'rb') as image:
        imageData = image.read()
        response = requests.post(
            ocrURL, headers=headers, params=params, data=imageData)
        try:
            response.raise_for_status()
        except:
            pass
        analysis = response.json()
        pprint(analysis)
        #自己写的判断
        pass

async def analyzeURL(imageURL, subscription_key, language='unk'):
    #Azure的ocr api逻辑 ver URL
    azureVisionURL = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
    ocrURL = azureVisionURL + "ocr"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/json'}
    params  = {'language': language}
    response = requests.post(
        ocrURL, headers=headers, params=params, json={'url':imageURL})
    try:
        response.raise_for_status()
    except:
        pass
    analysis = response.json()
    pprint(analysis)

def jsonHandle():
    #主逻辑
    pass
"""
    IiEST -> BEST
    SCORC,SCORES -> SCORE
    score: success best score 10000 b AGAIN ConneR 所以大概是找出 (best) score 数字 作为记分
    TP: 带百分号 g->9 o->O l,i -> 1 s->5
    Max Combo
    用途？ 识别卖弱啊（雾） 如果杀了发送恭喜字符
"""
"""
    最终目的是返回一个dict(?) "id"/"score"/"title"/"diff"
"""
"""
    可能还是建哈希表存储曲目信息比较好？
"""