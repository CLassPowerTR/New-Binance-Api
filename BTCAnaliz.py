import TelegramMesajGonder
import RSI
from binance.client import Client
import time
import pandas as pd

def sendTelegramMessage(message):
    chat_id = "Telegram-Chat_id"
    apiUrl = "https://api.telegram.org/botYOURBOTAPİ/sendMessage"
    bot = TelegramMesajGonder.onTelegramBot()
    bot.onSendMessage(chat_id,apiUrl, message)


api_key = 'BINANCE_APİ_KEY'  # Binance API anahtarınızı buraya girin
api_secret = 'BINANCE_APİ_SECRET'  # Binance API gizli anahtarınızı buraya girin

client = Client(api_key, api_secret)

symbol = 'BTCUSDT'  # Analiz yapmak istediğiniz sembolü buraya girin
interval = Client.KLINE_INTERVAL_1DAY  # Kullanmak istediğiniz zaman dilimini burada belirtin
print("   KISA VADE                ORTA VADE                UZUN VADE")
while True:
    try:
        # Son saatlik kapanış fiyatlarını alın
        klines = client.get_klines(symbol=symbol, interval=interval, limit=6)
        klines1 = client.get_klines(symbol=symbol, interval=interval, limit=14)
        klines2 = client.get_klines(symbol=symbol, interval=interval, limit=24)
        close_prices = [float(kline[4]) for kline in klines]
        close_prices1 = [float(kline[4]) for kline in klines1]
        close_prices2 = [float(kline[4]) for kline in klines2]

        # Kapanış fiyatlarını pandas Series'e dönüştürün
        close_series = pd.Series(close_prices)
        close_series1 = pd.Series(close_prices1)
        close_series2 = pd.Series(close_prices2)

        kisaVade = RSI.kisaVadeliRSI(close_series)
        ortaVade = RSI.ortaVadeliRSI(close_series1)
        uzunVade = RSI.uzunVadeliRSI(close_series2)

        output = kisaVade, ortaVade, uzunVade,
        cleaned_output = '          '.join([f"{item[0]} {item[1]}" for item in output])
        print(cleaned_output)

        if kisaVade[0] == "Al" or ortaVade[0] == "Al" or uzunVade[0] == "Al":
            message = cleaned_output
            sendTelegramMessage(message)
        elif kisaVade[0] == "Sat" or ortaVade[0] == "Sat" or uzunVade[0] == "Sat":
            message = cleaned_output
            sendTelegramMessage(message)

    except:
        print("Bir Hata Oluştu")
    time.sleep(60)
