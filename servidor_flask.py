from flask import Flask, jsonify
import random

app = Flask(__name__)

# Lista fija de tus 60 puntos con coordenadas y nombre (sin el "nivel")
nivel_agua = [
     {"nombre": "Kennedy Centro", "lat": 4.650, "lon": -74.150, "nivel": 35},
    {"nombre": "Kennedy Norte", "lat": 4.660, "lon": -74.145, "nivel": 60},
    {"nombre": "Kennedy Sur", "lat": 4.640, "lon": -74.155, "nivel": 45},
    {"nombre": "Kennedy Oriente", "lat": 4.650, "lon": -74.140, "nivel": 75},
    {"nombre": "Kennedy Occidente", "lat": 4.650, "lon": -74.160, "nivel": 80},
    {"nombre": "Kennedy NE", "lat": 4.665, "lon": -74.143, "nivel": 30},
    {"nombre": "Kennedy SE", "lat": 4.635, "lon": -74.148, "nivel": 70},
    {"nombre": "Kennedy NW", "lat": 4.655, "lon": -74.153, "nivel": 65},
    {"nombre": "Kennedy SW", "lat": 4.645, "lon": -74.160, "nivel": 50},
    {"nombre": "Kennedy Este", "lat": 4.652, "lon": -74.135, "nivel": 40},
    {"nombre": "Kennedy Oeste", "lat": 4.652, "lon": -74.165, "nivel": 62},
    {"nombre": "Kennedy Noroeste", "lat": 4.670, "lon": -74.150, "nivel": 58},


    # BOSA
    {"nombre": "Bosa Centro", "lat": 4.610, "lon": -74.190, "nivel": 50},
    {"nombre": "Bosa Norte", "lat": 4.620, "lon": -74.185, "nivel": 30},
    {"nombre": "Bosa Sur", "lat": 4.600, "lon": -74.195, "nivel": 75},
    {"nombre": "Bosa Oriente", "lat": 4.610, "lon": -74.180, "nivel": 65},
    {"nombre": "Bosa Occidente", "lat": 4.610, "lon": -74.200, "nivel": 85},
    {"nombre": "Bosa NE", "lat": 4.625, "lon": -74.183, "nivel": 45},
    {"nombre": "Bosa SE", "lat": 4.595, "lon": -74.187, "nivel": 58},
    {"nombre": "Bosa NW", "lat": 4.615, "lon": -74.198, "nivel": 90},
    {"nombre": "Bosa SW", "lat": 4.605, "lon": -74.198, "nivel": 52},
    {"nombre": "Bosa Este", "lat": 4.608, "lon": -74.175, "nivel": 68},
    {"nombre": "Bosa Oeste", "lat": 4.608, "lon": -74.205, "nivel": 43},
    {"nombre": "Bosa Noroeste", "lat": 4.622, "lon": -74.192, "nivel": 59},


    # ENGATIVÁ
    {"nombre": "Engativá Centro", "lat": 4.725, "lon": -74.115, "nivel": 55},
    {"nombre": "Engativá Norte", "lat": 4.735, "lon": -74.110, "nivel": 70},
    {"nombre": "Engativá Sur", "lat": 4.715, "lon": -74.120, "nivel": 40},
    {"nombre": "Engativá Occidente", "lat": 4.725, "lon": -74.125, "nivel": 38},
    {"nombre": "Engativá NE", "lat": 4.740, "lon": -74.108, "nivel": 30},
    {"nombre": "Engativá SE", "lat": 4.710, "lon": -74.110, "nivel": 50},
    {"nombre": "Engativá NW", "lat": 4.730, "lon": -74.122, "nivel": 45},
    {"nombre": "Engativá SW", "lat": 4.715, "lon": -74.128, "nivel": 60},
    {"nombre": "Engativá Este", "lat": 4.728, "lon": -74.100, "nivel": 42},
    {"nombre": "Engativá Oeste", "lat": 4.728, "lon": -74.130, "nivel": 57},
   


    # FONTIBÓN
    {"nombre": "Fontibón Centro", "lat": 4.680, "lon": -74.140, "nivel": 40},
    {"nombre": "Fontibón Norte", "lat": 4.690, "lon": -74.135, "nivel": 35},
    {"nombre": "Fontibón Sur", "lat": 4.670, "lon": -74.145, "nivel": 60},
    {"nombre": "Fontibón Oriente", "lat": 4.680, "lon": -74.130, "nivel": 72},
    {"nombre": "Fontibón Occidente", "lat": 4.680, "lon": -74.150, "nivel": 55},
    {"nombre": "Fontibón NE", "lat": 4.695, "lon": -74.133, "nivel": 50},
    {"nombre": "Fontibón SE", "lat": 4.665, "lon": -74.138, "nivel": 48},
    {"nombre": "Fontibón NW", "lat": 4.685, "lon": -74.145, "nivel": 62},
    {"nombre": "Fontibón SW", "lat": 4.675, "lon": -74.150, "nivel": 46},
    {"nombre": "Fontibón Este", "lat": 4.678, "lon": -74.128, "nivel": 39},
    {"nombre": "Fontibón Oeste", "lat": 4.678, "lon": -74.155, "nivel": 41},
    {"nombre": "Fontibón Noroeste", "lat": 4.692, "lon": -74.142, "nivel": 54},
    {"nombre": "Corabastos", "lat": 4.631, "lon": -74.162, "nivel": 50},
    {"nombre": "Patio Bonito", "lat": 4.652, "lon": -74.156, "nivel": 65},
    {"nombre": "UPZ Gran Britalia", "lat": 4.620, "lon": -74.165, "nivel": 55},
    {"nombre": "UPZ El Porvenir", "lat": 4.602, "lon": -74.196, "nivel": 60},
    # PATIO BONITO


    {"nombre": "Patio Bonito Norte", "lat": 4.655, "lon": -74.155, "nivel": 58},
    {"nombre": "Patio Bonito Sur", "lat": 4.648, "lon": -74.158, "nivel": 67},
    {"nombre": "Patio Bonito Oriente", "lat": 4.651, "lon": -74.152, "nivel": 52},
    {"nombre": "Patio Bonito Occidente", "lat": 4.651, "lon": -74.162, "nivel": 75},


    # UPZ GRAN BRITALIA
    {"nombre": "Gran Britalia Norte", "lat": 4.625, "lon": -74.165, "nivel": 60},
    {"nombre": "Gran Britalia Sur", "lat": 4.615, "lon": -74.165, "nivel": 68},
    {"nombre": "Gran Britalia Centro", "lat": 4.620, "lon": -74.160, "nivel": 62},


    # UPZ EL PORVENIR
    {"nombre": "El Porvenir Norte", "lat": 4.606, "lon": -74.193, "nivel": 58},
    {"nombre": "El Porvenir Sur", "lat": 4.598, "lon": -74.198, "nivel": 64},


    #    UPZ MODELIA
    {"nombre": "Modelia Norte", "lat": 4.678, "lon": -74.120, "nivel": 55},
    {"nombre": "Modelia Sur", "lat": 4.670, "lon": -74.125, "nivel": 50},
    {"nombre": "Modelia Centro", "lat": 4.674, "lon": -74.122, "nivel": 58},


    #       UPZ ENGATIVÁ
    {"nombre": "UPZ Engativá Norte", "lat": 4.730, "lon": -74.115, "nivel": 65},
    {"nombre": "UPZ Engativá Sur", "lat": 4.720, "lon": -74.115, "nivel": 60},
    {"nombre": "UPZ Engativá Centro", "lat": 4.725, "lon": -74.110, "nivel": 72},
    {"nombre": "La Margarita Sur",          "lat": 4.6344,  "lon": -74.1808, "nivel": 60},
    {"nombre": "La Margarita Centro-Sur",   "lat": 4.6364,  "lon": -74.1800, "nivel": 63},
    {"nombre": "La Margarita Centro",       "lat": 4.6384,  "lon": -74.1790, "nivel": 65},
    {"nombre": "La Margarita Centro-Norte", "lat": 4.6304,  "lon": -74.1780, "nivel": 68},
    {"nombre": "La Margarita Norte",        "lat": 4.6392,  "lon": -74.1860, "nivel": 70},
    {"nombre": "La Margarita Oriente",      "lat": 4.6339,  "lon": -74.1975, "nivel": 72},
    {"nombre": "La Margarita noroeste",     "lat": 4.6399,  "lon": -74.1830, "nivel": 66}


    # (...) Agrega los demás puntos aquí (Bosa, Engativá, Fontibón, etc.)
]

@app.route("/api/niveles")
def obtener_niveles():
    # Simular el nivel de agua con valores aleatorios
    puntos_simulados = []
    for punto in nivel_agua:
        punto_simulado = punto.copy()
        punto_simulado["nivel"] = random.randint(5, 95)  # valores entre 5 cm y 95 cm
        puntos_simulados.append(punto_simulado)
    return jsonify(puntos_simulados)

if __name__ == "__main__":
    app.run(debug=True)
