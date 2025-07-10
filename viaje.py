# viaje.py
from geopy.distance import geodesic

# Coordenadas aproximadas (latitud, longitud)
ciudades = {
    "santiago": (-33.4489, -70.6693),
    "arica": (-18.4783, -70.3126),
    "iquique": (-20.2133, -70.1524),
    "lima": (-12.0464, -77.0428),
    "cusco": (-13.5320, -71.9675),
    "arequipa": (-16.4090, -71.5375)
}

while True:
    origen = input("Ingrese la ciudad de origen (Chile) o 's' para salir: ").lower()
    if origen == "s":
        break

    destino = input("Ingrese la ciudad de destino (Perú) o 's' para salir: ").lower()
    if destino == "s":
        break

    if origen not in ciudades or destino not in ciudades:
        print("❌ Ciudad no reconocida. Intente con otra.")
        print("🌎 Opciones disponibles:", list(ciudades.keys()))
        continue

    print("\nSeleccione el medio de transporte:")
    print("1. Automóvil (~80 km/h)")
    print("2. Caminando (~5 km/h)")
    medio = input("Ingrese 1 o 2: ")

    coord_origen = ciudades[origen]
    coord_destino = ciudades[destino]
    distancia_km = round(geodesic(coord_origen, coord_destino).km, 2)
    distancia_millas = round(distancia_km * 0.621371, 2)

    if medio == "1":
        velocidad = 80  # km/h
        transporte = "Automóvil"
    elif medio == "2":
        velocidad = 5  # km/h
        transporte = "Caminando"
    else:
        print("❌ Opción inválida.")
        continue

    duracion_horas = round(distancia_km / velocidad, 2)

    print("\n🗺️ Resultado del viaje:")
    print(f"➡️ De: {origen.capitalize()} a {destino.capitalize()}")
    print(f"📏 Distancia: {distancia_km} km / {distancia_millas} millas")
    print(f"🚗 Medio de transporte: {transporte}")
    print(f"⏱️ Duración estimada: {duracion_horas} horas")
    print(f"📌 Narrativa: Viajar desde {origen.capitalize()} hasta {destino.capitalize()} cubriendo aproximadamente {distancia_km} km usando {transporte}.\n")
