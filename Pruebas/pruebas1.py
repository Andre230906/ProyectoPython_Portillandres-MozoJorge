import json


with open('Campers.json', 'r') as file:
    data = json.load(file)


nuevo_camper = {
    "id": "67890",
    "nombres": "Ana",
    "apellidos": "Gutiérrez",
    "direccion": "Carrera 45, Ciudad",
    "acudiente": "Luis Gómez",
    "telefonos": {
        "celular": "3109876543",
        "fijo": "7654321"
    },
    "estado": "Inscrito",
    "riesgo": "Medio"
}

data["campers"].append(nuevo_camper)

# Guardar la estructura actualizada en el archivo JSON
with open('Campers.json', 'w') as file:
    json.dump(data, file, indent=4)