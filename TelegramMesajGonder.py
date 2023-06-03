from datetime import datetime
import requests
import tkinter
from tkinter import Tk
from threading import Thread

class onTelegramBot:
    def onSendMessage(self,chat_id,api,message):
        requests.post(api,data={"chat_id":chat_id,"text":message}).json()
