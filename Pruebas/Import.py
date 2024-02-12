import json

class Start:
    def __init__(self, game, data={}):
        self.name = game + 'Campers.json'
        self.data = data

    def xyz(self):
        self.method_y()  # Llamar a otros métodos con self.method está bien

    def loading(self, file=None):
        if not file:
            file = self.name
        with open(file, 'r') as file:
            game_data = json.load(file)
        return game_data

    def guardar(self, nuevo_camper):
        game_data = self.loading()  # Cargar datos actuales
        game_data["camper"].append(nuevo_camper)  # Agregar nuevo camper
        with open(self.name, 'w') as file:
            json.dump(game_data, file, indent=4)  # Guardar la estructura actualizada en el archivo JSON
            
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

start = Start('nombre_del_juego')
start.guardar(nuevo_camper)