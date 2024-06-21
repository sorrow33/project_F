import pandas as pd


def analyze_stock(df: pd.DataFrame) -> str:
    if len(df) < 50:  # Assurez-vous qu'il y a suffisamment de données pour les indicateurs
        return 'Hold'

    latest_close = df['Close'].iloc[-1]
    sma20 = df['SMA20'].iloc[-1]
    sma50 = df['SMA50'].iloc[-1]
    rsi = df['RSI'].iloc[-1]
    bollinger_high = df['Bollinger_High'].iloc[-1]
    bollinger_low = df['Bollinger_Low'].iloc[-1]
    macd = df['MACD'].iloc[-1]
    macd_signal = df['MACD_Signal'].iloc[-1]

    # Exemple de règles de trading
    # if latest_close > sma20 and latest_close > sma50 and rsi < 70 and macd > macd_signal:
    if latest_close > sma20 and latest_close > sma50 and rsi < 70:
        return 'Buy'
    #elif latest_close < sma20 and latest_close < sma50 and rsi > 30 and macd < macd_signal:
    elif latest_close < sma20 and latest_close < sma50 and rsi > 30:
        return 'Sell'
    elif latest_close < bollinger_low and rsi < 30 and macd > macd_signal:
        return 'Buy'
    elif latest_close > bollinger_high and rsi > 70 and macd < macd_signal:
        return 'Sell'
    else:
        return 'Hold'

