def listar_campers_inscritos(campers):
    campers_inscritos = [camper for camper in campers.values() if camper['Estado'] == 'Inscrito']
    if campers_inscritos:
        print("Campers inscritos:")
        for camper in campers_inscritos:
            print(camper)
    else:
        print("No hay campers inscritos.")

# Función para listar campers que aprobaron el examen inicial
def listar_campers_aprobados(campers):
    campers_aprobados = [camper for camper in campers.values() if camper['Estado'] == 'Aprobado']
    if campers_aprobados:
        print("Campers que aprobaron el examen inicial:")
        for camper in campers_aprobados:
            print(camper)
    else:
        print("No hay campers que hayan aprobado el examen inicial.")

# Función para listar campers con bajo rendimiento
def listar_campers_bajo_rendimiento(campers):
    campers_bajo_rendimiento = [camper for camper in campers.values() if camper['Estado'] == 'Reprobado']
    if campers_bajo_rendimiento:
        print("Campers con bajo rendimiento:")
        for camper in campers_bajo_rendimiento:
            print(camper)
    else:
        print("No hay campers con bajo rendimiento.")