import requests

BOT_TOKEN = '7563053664:AAGbK6aLnreK8-Pqo0ePgpFERfinLutUKhQ'
NGROK_URL = 'https://f726-2800-484-c275-95f4-1411-20db-f5d2-5565.ngrok-free.app'

url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={NGROK_URL}/bot{BOT_TOKEN}"
response = requests.get(url)

print(response.json())
