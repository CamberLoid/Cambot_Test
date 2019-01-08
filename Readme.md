# Cambot&Cambot_launcher prototype

基于telepot的telegram bot，可能会往CQ拓展

Bot在建，还没写完

不想写
逻辑：
```
group -> `/brainpower` #群组脑力合唱
        ->随机发送brainpowerCore/"Are you rea-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-"后接合唱
      -> `/show` 向目标群组发送最近一次杀人登记信息,Forward
      -> `/register` 知道某个user在groupid里了
private -> `/brainpower` 返回 `单人脑力多没有意思 去群组里发/brianpower试试`
        -> `/register game`
           :Picture:
           -> 对指定的区域ocr识别分数/成绩/id
              保存为`{}`
           预期实现的数据结构为(class/json)
           TelegramID - id:int
                      - usrname:str # 随杀人记录请求向telegram请求更新
                      - game - title:str
                             - isFC()
                             - @abstract isKilled() # 视游戏而定
                      - example:Arcaea - gameID:str
                                       - pure:int
                                       - far:int
                                       - isKilled():bool
                      - groupid:[] # 广播杀人通知
           对每一个TelegramID建立{ID}.json
        -> `/cast` 以FW+Comment的形式 for i in TelegramID.groupid: sendMessage()
```
