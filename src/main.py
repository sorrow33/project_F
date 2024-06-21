# main.py

import logging
import datetime
from portfolio import Portfolio
from data_fetcher import get_cac40_symbols, get_data
from indicators import add_indicators
from strategy import analyze_stock
# from trader import place_order
from config import START_DATE

logging.basicConfig(filename='logs/trading_bot.log', level=logging.INFO)

portfolio = Portfolio()


def prompt_user_for_action():
    while True:
        print("\nListe des actions à acheter aujourd'hui :")
        buy_list = run_bot()  # Obtenez la liste des actions à acheter
        for symbol in buy_list:
            print(symbol)

        while True:
            symbol = input("\nEntrez le symbole de l'action que vous souhaitez acheter (ou 'quit' pour quitter) : ")
            if symbol == 'quit':
                return  # Quitter la fonction et arrêter l'achat
            if symbol in buy_list:
                try:
                    # Demander le nombre d'actions à acheter
                    quantity = int(input(f"Entrez le nombre d'actions à acheter pour {symbol} : "))
                    # Demander le prix total d'achat
                    total_price = float(input(f"Entrez le prix total d'achat pour {quantity} actions de {symbol} : "))

                    buy_price = total_price / quantity  # Calculer le prix unitaire

                    available_balance = portfolio.available_balance
                    if total_price > available_balance:
                        print(
                            f"Fonds insuffisants. Coût total : {total_price} euros. Fonds disponibles : {available_balance} euros.")
                        continue

                    confirmation = input(
                        f"Confirmez-vous l'achat de {quantity} actions de {symbol} pour un total de {total_price} euros? (oui/non) : ")
                    if confirmation.lower() == 'oui':
                        portfolio.buy_stock(symbol, buy_price, quantity)
                        print(f"Achat de {quantity} actions de {symbol} effectué pour un total de {total_price} euros.")
                    else:
                        print("Achat annulé.")

                except ValueError:
                    print("Entrée invalide. Assurez-vous d'entrer un nombre valide et un prix valide.")
            else:
                print("Symbole invalide. Veuillez choisir un symbole valide dans la liste.")

        another_action = input("Voulez-vous acheter une autre action ? (oui/non) : ")
        if another_action.lower() != 'oui':
            break


def run_bot():
    symbols = get_cac40_symbols('data/cac40_symbols.yaml')
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    buy_list = []

    for symbol in symbols:
        df = get_data(symbol, START_DATE, today)
        if df.empty:
            logging.warning(f'No data for symbol: {symbol}')
            continue

        df = add_indicators(df)
        if len(df) < 50:  # Assurez-vous qu'il y a suffisamment de données pour calculer les indicateurs
            logging.warning(f'Not enough data for symbol: {symbol} to calculate indicators')
            continue

        signal = analyze_stock(df)
        logging.info(f'Symbol: {symbol} | Signal: {signal}')

        if signal == 'Buy':
            buy_list.append(symbol)

    return buy_list


if __name__ == "__main__":
    portfolio.load_portfolio()
    portfolio.display_portfolio()  # Afficher le portefeuille au démarrage
    prompt_user_for_action()
    portfolio.save_portfolio()