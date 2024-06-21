# stock.py

class Stock:
    def __init__(self, symbol, buy_price, quantity, buy_date):
        self.symbol = symbol
        self.buy_price = buy_price
        self.quantity = quantity
        self.buy_date = buy_date

    def __repr__(self):
        return f"Stock(symbol='{self.symbol}', buy_price={self.buy_price}, quantity={self.quantity}, buy_date='{self.buy_date}')"