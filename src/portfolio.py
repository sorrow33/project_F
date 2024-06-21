# portfolio.py

import json
import logging
import datetime
from stock import Stock  # Importer la classe Stock depuis stock.py

portfolio_file = 'portfolio.json'
initial_balance = 100000  # Portefeuille initial de 100 000 euros


class Portfolio:
    def __init__(self):
        self.available_balance = initial_balance
        self.stocks = []

    def calculate_available_investment(self):
        invested_amount = sum(stock.quantity * stock.buy_price for stock in self.stocks)
        available_balance = initial_balance - invested_amount
        return available_balance

    def buy_stock(self, symbol, buy_price, quantity):
        total_cost = buy_price * quantity
        if total_cost > self.available_balance:
            raise ValueError(
                f"Fonds insuffisants. Coût total : {total_cost} euros. Fonds disponibles : {self.available_balance} euros.")

        new_stock = Stock(symbol, buy_price, quantity, datetime.datetime.now().strftime('%Y-%m-%d'))
        self.stocks.append(new_stock)
        self.available_balance -= total_cost

    def sell_stock(self, symbol, sell_price, quantity):
        found = False
        for stock in self.stocks:
            if stock.symbol == symbol:
                found = True
                if stock.quantity >= quantity:
                    stock.quantity -= quantity
                    self.available_balance += sell_price * quantity
                    if stock.quantity == 0:
                        self.stocks.remove(stock)
                    break
                else:
                    raise ValueError(
                        f"Trying to sell {quantity} shares of {symbol} but only {stock.quantity} available.")

        if not found:
            logging.warning(f"Trying to sell {quantity} shares of {symbol} which are not in the portfolio.")

    def get_portfolio_value(self):
        total_value = self.available_balance
        for stock in self.stocks:
            total_value += stock.quantity * stock.buy_price
        return total_value

    def save_portfolio(self):
        portfolio_data = {
            'available_balance': self.available_balance,
            'stocks': [stock.__dict__ for stock in self.stocks]
        }
        with open(portfolio_file, 'w') as f:
            json.dump(portfolio_data, f, indent=4)

    def load_portfolio(self):
        global initial_balance
        try:
            with open(portfolio_file, 'r') as f:
                portfolio_data = json.load(f)
                self.available_balance = portfolio_data['available_balance']
                self.stocks = [Stock(**stock_data) for stock_data in portfolio_data.get('stocks', [])]
        except FileNotFoundError:
            logging.warning(f'Portfolio file {portfolio_file} not found. Starting with empty portfolio.')
            self.available_balance = initial_balance
            self.stocks = []

    def display_portfolio(self):
        print(f"Solde disponible: {self.available_balance} euros")
        if not self.stocks:
            print("Le portefeuille est vide.")
        else:
            for stock in self.stocks:
                print(
                    f"Symbole: {stock.symbol}, Quantité: {stock.quantity}, Prix d'achat: {stock.buy_price}, Date d'achat: {stock.buy_date}")
