import os
import requests

def send_message():
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    pesan = "Halo! Ini adalah update otomatis dari bot kamu."
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": pesan}
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_message()
