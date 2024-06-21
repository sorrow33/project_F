import yfinance as yf
import pandas as pd
import yaml


def get_cac40_symbols(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        symbols = yaml.safe_load(file)
    return symbols['symbols']


def get_data(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    return yf.download(symbol, start=start_date, end=end_date)
