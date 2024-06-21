import schedule
import time
from src.main import run_bot

def start_scheduler():
    schedule.every().day.at("09:00").do(run_bot)
    while True:
        schedule.run_pending()
        time.sleep(1)