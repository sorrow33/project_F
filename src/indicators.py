import pandas as pd
import ta


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    # Simple Moving Average (SMA)
    df['SMA20'] = ta.trend.sma_indicator(df['Close'], window=20)
    df['SMA50'] = ta.trend.sma_indicator(df['Close'], window=50)

    # Exponential Moving Average (EMA)
    df['EMA20'] = ta.trend.ema_indicator(df['Close'], window=20)
    df['EMA50'] = ta.trend.ema_indicator(df['Close'], window=50)

    # Relative Strength Index (RSI)
    df['RSI'] = ta.momentum.rsi(df['Close'], window=14)

    # Bollinger Bands
    bollinger = ta.volatility.BollingerBands(df['Close'], window=20, window_dev=2)
    df['Bollinger_High'] = bollinger.bollinger_hband()
    df['Bollinger_Low'] = bollinger.bollinger_lband()
    df['Bollinger_Mid'] = bollinger.bollinger_mavg()

    # MACD (Moving Average Convergence Divergence)
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()  # MACD line
    df['MACD_Signal'] = macd.macd_signal()  # Signal line

    return df
