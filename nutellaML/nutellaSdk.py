import threading
import psutil
import time
import schedule
import asyncio
import base64
from asyncio import Future
import struct
from rx import interval
from apscheduler.schedulers.background import BackgroundScheduler
from nutellaML import nutellaRequests

class Nutella(threading.Thread):

    def __init__(self):
        self.requestData=dict()


    def init(self,modelName=None, projectKey=None, reinit=False):
        self.requestData["projectKey"]=projectKey
        self.requestData["modelName"] =modelName
        self.requestData["reinit"] = reinit


    def config(self,**configDatas):
        for key,value in configDatas.items():
            self.requestData[key]=value

    def log(self,**logDatas):
        for key,value in logDatas.items():
            self.requestData[key]=value

    def printDict(self):
        print(self.requestData)
        a=nutellaRequests.Requests()
        asyncio.run(a.requestAction(requestDatas=self.requestData))



a=Nutella()
a.init(modelName="123",projectKey="12345",reinit=True)
a.printDict()





