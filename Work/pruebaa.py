import json

def listar_campers_por_estado(estado):
    with open('JSON/Campers.json') as f:
        data = json.load(f)
        campers = data['Campers']

    campers_segun_estado = [camper for camper in campers if camper['Estado'] == estado]

    if campers_segun_estado:
        print(f"Campers con estado '{estado}':")
        for camper in campers_segun_estado:
            print(camper)
    else:
        print(f"No hay campers con estado '{estado}'.")

# Ejemplo de uso
listar_campers_por_estado('Inscrito')
listar_campers_por_estado('Aprobado')
listar_campers_por_estado('Reprobado')

listar_campers_por_estado()