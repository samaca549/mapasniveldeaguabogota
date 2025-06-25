from dotenv import load_dotenv
import os
import requests

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

MENSAJE = "🚨 Alerta: Se ha detectado un nivel de agua crítico en Bogotá. Consulta el mapa para más información."

def obtener_chat_ids(archivo="usuarios.txt"):
    try:
        with open(archivo, "r") as f:
            lineas = f.read().splitlines()
            chat_ids = [linea.split()[0] for linea in lineas if linea.strip()]
            return chat_ids
    except FileNotFoundError:
        print("❌ No se encontró el archivo de usuarios.")
        return []

def enviar_mensaje(chat_id, mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": mensaje
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"✅ Mensaje enviado a {chat_id}")
    else:
        print(f"❌ Error al enviar a {chat_id}: {response.text}")

def main():
    chat_ids = obtener_chat_ids()
    if not chat_ids:
        print("⚠️ No hay usuarios registrados.")
        return
    for chat_id in chat_ids:
        enviar_mensaje(chat_id, MENSAJE)

if __name__ == "__main__":
    main()

