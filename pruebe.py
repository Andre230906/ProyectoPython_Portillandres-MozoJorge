import json

def modificar_ruta_general(ruta_json):
    # Solicitar al usuario el ID del camper
    camper_id = int(input("Ingrese el ID del camper: "))

    with open(ruta_json, 'r') as file:
        data = json.load(file)
        campers = data['Campers']

        for camper in campers:
            if camper['ID'] == camper_id:
                print("Rutas de Entrenamiento Disponibles:")
                print("1. Java")
                print("2. NodeJS")
                print("3. NetCore")

                opcion = int(input("Seleccione la ruta de entrenamiento (1, 2 o 3): "))

                if opcion == 1:
                    camper['Ruta General'] = "Java"
                elif opcion == 2:
                    camper['Ruta General'] = "NodeJS"
                elif opcion == 3:
                    camper['Ruta General'] = "NetCore"
                else:
                    print("Opción no válida. Por favor seleccione 1, 2 o 3.")
                    return

        with open(ruta_json, 'w') as file:
            json.dump(data, file, indent=4)

# Llamada a la función para modificar la ruta general en el archivo JSON
ruta_json = 'JSON/Campers.json'

modificar_ruta_general(ruta_json)