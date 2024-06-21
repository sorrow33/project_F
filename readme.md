# Trading Bot CAC40

## Description

Ce projet est un bot de trading automatisé conçu pour analyser et effectuer des transactions sur les actions du CAC40. Le bot utilise des indicateurs techniques tels que les moyennes mobiles (SMA, EMA), l'indice de force relative (RSI), les bandes de Bollinger et la divergence de convergence moyenne mobile (MACD) pour générer des signaux d'achat ou de vente. L'utilisateur peut également gérer un portefeuille d'actions et exécuter manuellement des achats en fonction des suggestions du bot.

## Fonctionnalités

- **Analyse des actions du CAC40** : Utilisation des indicateurs techniques pour générer des signaux d'achat et de vente.
- **Gestion du portefeuille** : Permet à l'utilisateur d'acheter et de vendre des actions, et de suivre les fonds disponibles et la valeur du portefeuille.
- **Exécution manuelle des achats** : L'utilisateur peut choisir les actions à acheter et spécifier le nombre d'actions et le prix total d'achat.

## Prérequis

- Python 3.10 ou supérieur
- Bibliothèques Python :
  - `pandas`
  - `ta`
  - `yfinance`
  - `json`
  - `logging`

## Installation

1. **Clonez le repository :**
   ```bash
   git clone https://github.com/votre-utilisateur/trading-bot-cac40.git
   cd trading-bot-cac40

2. **Créez et activez un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Sur Windows: venv\Scripts\activate

3. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   
4. **Ajoutez les symboles des actions du CAC40 dans un fichier YAML :**
   ```yaml
   # data/cac40_symbols.yaml
    symbols:
      - AC.PA
      - AI.PA
      - AIR.PA
      ...

## Utilisation
1. **Initialisez le portefeuille :**

Assurez-vous que le fichier portfolio.json est présent dans le répertoire principal. Si le fichier n'existe pas, il sera créé automatiquement.

2. **Lancez le bot de trading :**
    ```bash
   python main.py

3. **Suivez les instructions à l'écran pour acheter des actions :**

Le bot affichera une liste d'actions recommandées pour l'achat. Vous pourrez choisir les actions à acheter, spécifier le nombre d'actions et le prix total d'achat.

## Structure du projet
    trading-bot-cac40/
    ├── data/
    │   └── cac40_symbols.yaml
    ├── logs/
    │   └── trading_bot.log
    ├── portfolio.json
    ├── main.py
    ├── data_fetcher.py
    ├── indicators.py
    ├── strategy.py
    ├── portfolio.py
    ├── stock.py
    ├── config.py
    └── requirements.txt

## Fichiers
- main.py : Point d'entrée du programme. Gère l'analyse des actions et l'interaction avec l'utilisateur pour l'achat d'actions.
- data_fetcher.py : Contient les fonctions pour récupérer les données des actions du CAC40.
- indicators.py : Ajoute les indicateurs techniques aux données des actions.
- strategy.py : Contient la logique d'analyse des actions et génère les signaux d'achat et de vente.
- portfolio.py : Gère le portefeuille d'actions, y compris l'achat, la vente et l'affichage du portefeuille.
- stock.py : Définition de la classe Stock représentant une action dans le portefeuille.
- config.py : Fichier de configuration contenant les paramètres de date de début et de fin pour l'analyse.