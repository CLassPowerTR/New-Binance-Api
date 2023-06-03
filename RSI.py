import ta

def kisaVadeliRSI(close_series):
    if len(close_series) >= 6:
        # RSI hesaplamak için kapanış fiyatlarını kullanın
        rsi = ta.momentum.RSIIndicator(close_series, window=6)
        current_rsi = rsi.rsi()
        current_rsi = list(current_rsi)
        current_rsi = current_rsi[-1]
        current_rsi = round(current_rsi, 2)
        rsiPuan = f"RSI: {current_rsi}"

        if current_rsi < 20:
            durum = "Al"
        elif current_rsi > 80:
            durum = "Sat"
        else:
            durum = "Hodl"
        return durum, rsiPuan

def ortaVadeliRSI(close_series):
    if len(close_series) >= 14:
        # RSI hesaplamak için kapanış fiyatlarını kullanın
        rsi = ta.momentum.RSIIndicator(close_series, window=14)
        current_rsi = rsi.rsi()
        current_rsi = list(current_rsi)
        current_rsi = current_rsi[-1]
        current_rsi = round(current_rsi, 2)
        rsiPuan = f"RSI: {current_rsi}"

        if current_rsi < 25:
            durum = "Al"
        elif current_rsi > 75:
            durum = "Sat"
        else:
            durum = "Hodl"
        return durum, rsiPuan

def uzunVadeliRSI(close_series):
    if len(close_series) >= 24:
        # RSI hesaplamak için kapanış fiyatlarını kullanın
        rsi = ta.momentum.RSIIndicator(close_series, window=24)
        current_rsi = rsi.rsi()
        current_rsi = list(current_rsi)
        current_rsi = current_rsi[-1]
        current_rsi = round(current_rsi, 2)
        rsiPuan = f"RSI: {current_rsi}"

        if current_rsi < 20:
            durum = "Al"
        elif current_rsi > 80:
            durum = "Sat"
        else:
            durum = "Hodl"
        return durum, rsiPuan
