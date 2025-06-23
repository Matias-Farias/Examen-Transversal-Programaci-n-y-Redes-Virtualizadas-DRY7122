import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "iNgWfOmKCgJieCt9d6MCx9zFlzqxF4Qj"

while True:
    orig = input("Ciudad de Origen (o 's' para salir): ")
    if orig.lower() == "s" or orig.lower() == "salir":
        break

    dest = input("Ciudad de Destino (o 's' para salir): ")
    if dest.lower() == "s" or dest.lower() == "salir":
        break

    medio = input("Medio de transporte (auto, bicicleta, caminando): ").lower()

    url = main_api + urllib.parse.urlencode({
        "key": key,
        "from": orig,
        "to": dest,
        "routeType": "fastest" if medio == "auto" else "bicycle" if medio == "bicicleta" else "pedestrian"
    })

    print("URL:", url)
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]

    if status_code == 0:
        print("=============================================")
        print(f"Ruta desde {orig} a {dest}")
        print("Duración del viaje:", json_data["route"]["formattedTime"])
        print("Kilómetros:", "{:.2f}".format(json_data["route"]["distance"] * 1.61))
        print("Combustible utilizado (Ltr):", "{:.2f}".format(json_data["route"].get("fuelUsed", 0) * 3.78))
        print("=============================================")
        for step in json_data["route"]["legs"][0]["maneuvers"]:
            print(f"{step['narrative']} ({step['distance'] * 1.61:.2f} km)")
        print("=============================================\n")
    elif status_code == 402:
        print("*** Error 402: Entradas inválidas para una o ambas ubicaciones ***\n")
    elif status_code == 611:
        print("*** Error 611: Faltan ubicaciones ***\n")
    else:
        print(f"*** Error desconocido (código {status_code}) ***\n")