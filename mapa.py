import folium
from folium.plugins import MarkerCluster
from branca.element import Template, MacroElement, Element
import requests
import random
import time
from datetime import datetime

# Configuración
API_FLASK_URL = "http://127.0.0.1:5000/api/niveles"
API_KEY = "687e0fa8cf90a696fc386db3b6277344"

# Datos iniciales (tus datos originales completos)
nivel_agua = [
    # KENNEDY
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

]

# Puntos de clima (tus datos originales)
puntos_clima = {
    "Kennedy": [(4.648, -74.138), (4.642, -74.155)],
    "Bosa": [(4.605, -74.178), (4.618, -74.192)],
    "Engativá": [(4.720, -74.110), (4.735, -74.122)],
    "Fontibón": [(4.688, -74.132), (4.672, -74.148)]
}

# Puntos de densidad (tus datos originales)
puntos_densidad = [
    {"localidad": "Kennedy", "lat": 4.634, "lon": -74.162, "densidad": 23000},
    {"localidad": "Kennedy", "lat": 4.640, "lon": -74.150, "densidad": 22500},
    {"localidad": "Bosa", "lat": 4.600, "lon": -74.193, "densidad": 22000},
    {"localidad": "Bosa", "lat": 4.610, "lon": -74.185, "densidad": 21500},
    {"localidad": "Engativá", "lat": 4.725, "lon": -74.110, "densidad": 19500},
    {"localidad": "Engativá", "lat": 4.730, "lon": -74.120, "densidad": 20000},
    {"localidad": "Fontibón", "lat": 4.682, "lon": -74.142, "densidad": 18500},
    {"localidad": "Fontibón", "lat": 4.675, "lon": -74.130, "densidad": 19000},
]

# Iconos de clima (tus datos originales)
iconos_clima = {
    "clear": "https://cdn-icons-png.flaticon.com/512/869/869869.png",
    "clouds": "https://cdn-icons-png.flaticon.com/512/414/414825.png",
    "rain": "https://cdn-icons-png.flaticon.com/512/1163/1163624.png",
    "drizzle": "https://cdn-icons-png.flaticon.com/512/4005/4005901.png",
    "thunderstorm": "https://cdn-icons-png.flaticon.com/512/1146/1146860.png",
    "snow": "https://cdn-icons-png.flaticon.com/512/642/642102.png",
    "mist": "https://cdn-icons-png.flaticon.com/512/1779/1779807.png"
}

# Función para actualizar datos
def actualizar_datos():
    try:
        response = requests.get(API_FLASK_URL)
        return response.json()
    except:
        for punto in nivel_agua:
            punto["nivel"] = random.randint(20, 90)
        return nivel_agua

# Función principal para crear el mapa (tu código original con encapsulado)
def crear_mapa_completo(datos):
    m = folium.Map(location=[4.675, -74.13], zoom_start=11)
    
    # Capas (tu código original sin cambios)
    nivel_group = folium.FeatureGroup(name="🌊 Nivel del Agua")
    clima_group = folium.FeatureGroup(name="☁️ Clima Actual")
    densidad_group = folium.FeatureGroup(name="👥 Densidad Poblacional")
    cluster = MarkerCluster().add_to(nivel_group)

    # Marcadores de nivel de agua (original)
    for punto in datos:
        color = "green" if punto["nivel"] < 30 else "orange" if punto["nivel"] < 60 else "red"
        folium.CircleMarker(
            location=[punto["lat"], punto["lon"]],
            radius=10,
            weight=4,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.9,
            popup=f"<b>{punto['nombre']}</b><br>🌊 Nivel agua: {punto['nivel']} cm"
        ).add_to(cluster)

    # Densidad poblacional (original)
    icono_densidad = folium.CustomIcon(
        "https://cdn-icons-png.flaticon.com/512/1077/1077012.png", 
        icon_size=(42, 42)
    )
    for punto in puntos_densidad:
        folium.Marker(
            location=[punto["lat"], punto["lon"]],
            icon=icono_densidad,
            popup=f"<b>{punto['localidad']}</b><br>👥 Alta densidad poblacional<br>{punto['densidad']} hab/km²"
        ).add_to(densidad_group)

    # Clima (original)
    for localidad, coords_list in puntos_clima.items():
        for lat, lon in coords_list:
            try:
                url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=es"
                r = requests.get(url)
                data = r.json()
                lluvia = data.get("clouds", {}).get("all", 0)
                temp = data.get("main", {}).get("temp", 0)
                clima_main = data.get("weather", [{}])[0].get("description", "").capitalize()
                icon_url = iconos_clima.get(clima_main.lower(), "https://cdn-icons-png.flaticon.com/512/1146/1146858.png")
                icon = folium.CustomIcon(icon_url, icon_size=(48, 48))
                folium.Marker(
                    location=[lat, lon],
                    icon=icon,
                    popup=f"<b>{localidad}</b><br>☁️ Clima: {clima_main}<br>🌧️ Lluvia: {lluvia}%<br>🌡️ Temp: {temp}°C"
                ).add_to(clima_group)
            except:
                continue

    # Añadir capas al mapa
    nivel_group.add_to(m)
    clima_group.add_to(m)
    densidad_group.add_to(m)
    folium.LayerControl(collapsed=False).add_to(m)

    # Leyenda (original)
    leyenda_html = """
    {% macro html(this, kwargs) %}
    <div style="position: fixed; bottom: 50px; left: 50px; width: 240px; height: 200px;
         background-color: white; z-index:9999; font-size:14px;
         border:2px solid grey; padding: 10px;">
    <b>Leyenda de Riesgo</b><br>
    <i style="background:green;width:10px;height:10px;float:left;margin-right:5px;"></i>Bajo (&lt; 30 cm)<br>
    <i style="background:orange;width:10px;height:10px;float:left;margin-right:5px;"></i>Medio (30–59 cm)<br>
    <i style="background:red;width:10px;height:10px;float:left;margin-right:5px;"></i>Alto (≥ 60 cm)<br><br>
    🌧️: Probabilidad de lluvia<br>
    🌡️: Temperatura actual<br>
    ☁️: Tipo de clima<br>
    👥: Alta densidad poblacional<br>
    </div>
    {% endmacro %}
    """
    macro = MacroElement()
    macro._template = Template(leyenda_html)
    m.get_root().add_child(macro)

    # Tabla de puntos críticos (original)
    criticos = sorted([p for p in datos if p["nivel"] >= 60], key=lambda x: x["nivel"], reverse=True)[:10]
    tabla_html = """
    {% macro html(this, kwargs) %}
    <div style="position: fixed; bottom: 30px; right: 30px; z-index:9999; font-size: 14px;">
        <button onclick="toggleTabla()" style="padding:4px 8px; margin-bottom:5px;">Mostrar/Ocultar Críticos</button>
        <div id="tablaCriticos" style="width: 300px; height: auto; background-color: white; border:2px solid gray; padding:10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.3);">
            <b>🔴 Puntos Críticos</b><br>
            <ul style='list-style:none; padding:0; margin:0;'>
    """ + "\n".join([f"<li class='critical-point' style='cursor:pointer; margin:4px 0;' data-lat='{p['lat']}' data-lon='{p['lon']}'>📍 {p['nombre']} ({p['nivel']} cm)</li>" for p in criticos]) + """
            </ul>
        </div>
    </div>
    {% endmacro %}
    """
    tabla_element = MacroElement()
    tabla_element._template = Template(tabla_html)
    m.get_root().add_child(tabla_element)

    # Script para tabla (original)
    script_js = Element("""
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const map = window._map || Object.values(window).find(v => v instanceof L.Map);
            window._map = map;
            document.querySelectorAll('.critical-point').forEach(function(el) {
                el.addEventListener('click', function() {
                    const lat = parseFloat(this.getAttribute('data-lat'));
                    const lon = parseFloat(this.getAttribute('data-lon'));
                    if (map) map.setView([lat, lon], 15, {animate: true, duration: 1.5});
                });
            });
        });
        function toggleTabla() {
            const tabla = document.getElementById("tablaCriticos");
            tabla.style.display = tabla.style.display === "none" ? "block" : "none";
        }
    </script>
    """)
    m.get_root().html.add_child(script_js)

    return m

# Bucle principal de actualización (nueva funcionalidad)
if __name__ == "__main__":
    while True:
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Actualizando mapa...")
        datos_actuales = actualizar_datos()
        mapa = crear_mapa_completo(datos_actuales)
        mapa.save("mapa_profesional_completo.html")
        time.sleep(30)  # Espera 30 segundos