from flask import Flask, request
import requests
import json

app = Flask(__name__)

BOT_TOKEN = '7563053664:AAGbK6aLnreK8-Pqo0ePgpFERfinLutUKhQ'
archivo_usuarios = 'usuarios.txt'

@app.route(f"/bot{BOT_TOKEN}", methods=["POST"])
def recibir_mensaje():
    data = request.get_json()
    chat_id = data['message']['chat']['id']

    # Guarda el chat_id si no está ya guardado
    with open(archivo_usuarios, 'a+') as f:
        f.seek(0)
        if str(chat_id) not in f.read():
            f.write(f"{chat_id}\n")

    return "ok", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
