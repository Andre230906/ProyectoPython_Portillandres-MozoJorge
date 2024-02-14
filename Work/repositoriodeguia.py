import json

# Capturar los datos de un camper
def capturar_datos_camper(campers, rutas_ocupadas):
    print("Eres Un Camper, Ingresa Tus Datos:")
    print("---Menú Camper---")
    
    try:
        NumId = int(input("Ingrese su número de identificación sin puntos ni comas: "))
        
        # Verificar si el número de identificación ya está en uso
        if NumId in campers:
            print("Error: El número de identificación ingresado ya está en uso. Por favor ingrese otro.")
            return None

        Nombre = input("Ingrese sus nombres: ")
        Apellidos = input("Ingrese sus apellidos: ")
        Direccion = input("Ingrese su dirección: ")
        Acudiente = input("Ingrese el nombre de su acudiente: ")
        Celular = input("Ingrese su número de celular: ")
        Fijo = input("Ingrese su número de teléfono fijo: ")
        Riesgo = input("Ingrese el nivel de riesgo: ")
        Ruta = input("Ingrese la ruta de entrenamiento a la cual aspira (NodeJS, Java, NetCore): ").lower()

        # Validar que la ruta ingresada sea una de las opciones válidas
        while Ruta not in ["nodejs", "java", "netcore"]:
            print("Ruta de entrenamiento no válida. Por favor ingrese una de las opciones disponibles.")
            Ruta = input("Ingrese la ruta de entrenamiento (NodeJS, Java, NetCore): ").lower()

        # Verificar si la ruta tiene cupo disponible
        if Ruta in rutas_ocupadas and rutas_ocupadas[Ruta] >= 33:
            print("Lo siento, la ruta", Ruta, "ya ha alcanzado el máximo de 33 campers inscritos.")
            return None
        
        # Incrementar el contador de la ruta
        rutas_ocupadas[Ruta] = rutas_ocupadas.get(Ruta, 0) + 1

        return {
            'NumId': NumId,
            'Nombre': Nombre,
            'Apellidos': Apellidos,
            'Direccion': Direccion,
            'Acudiente': Acudiente,
            'Celular': Celular,
            'Fijo': Fijo,
            'Riesgo': Riesgo,
            'Ruta': Ruta,
            'Estado': 'Inscrito'  # Se añade el estado inicial como "Inscrito"
        }
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido para el número de identificación.")
        return None

# Modificar los datos de un camper
def modificar_camper(camper):
    print("Modificar datos del camper:")
    print("1. Modificar número de identificación")
    print("2. Modificar nombres")
    print("3. Modificar apellidos")
    print("4. Modificar dirección")
    print("5. Modificar acudiente")
    print("6. Modificar número de celular")
    print("7. Modificar número de teléfono fijo")
    print("8. Modificar nivel de riesgo")
    print("9. Modificar ruta de entrenamiento")
    
    try:
        opcion = int(input("Ingrese el número de la opción que desea modificar: "))
        
        if opcion == 1:
            camper['NumId'] = int(input("Ingrese el nuevo número de identificación: "))
        elif opcion == 2:
            camper['Nombre'] = input("Ingrese los nuevos nombres: ")
        elif opcion == 3:
            camper['Apellidos'] = input("Ingrese los nuevos apellidos: ")
        elif opcion == 4:
            camper['Direccion'] = input("Ingrese la nueva dirección: ")
        elif opcion == 5:
            camper['Acudiente'] = input("Ingrese el nuevo acudiente: ")
        elif opcion == 6:
            camper['Celular'] = input("Ingrese el nuevo número de celular: ")
        elif opcion == 7:
            camper['Fijo'] = input("Ingrese el nuevo número de teléfono fijo: ")
        elif opcion == 8:
            camper['Riesgo'] = input("Ingrese el nuevo nivel de riesgo: ")
        elif opcion == 9:
            nueva_ruta = input("Ingrese la nueva ruta de entrenamiento (NodeJS, Java, NetCore): ").lower()
            while nueva_ruta not in ["nodejs", "java", "netcore"]:
                print("Ruta de entrenamiento no válida. Por favor ingrese una de las opciones disponibles.")
                nueva_ruta = input("Ingrese la ruta de entrenamiento (NodeJS, Java, NetCore): ").lower()
            camper['Ruta'] = nueva_ruta
        else:
            print("Opción no válida")
    except ValueError:
        print("Error: Por favor ingrese un número entero válido para la opción.")

# Buscar la información de un camper en el diccionario
def buscar_camper(diccionario, num_id):
    if num_id in diccionario:
        return diccionario[num_id]
    else:
        return "Camper no encontrado."

# Evaluar la nota final de un camper
def evaluar_camper(campers):
    num_id = int(input("Ingrese el número de identificación del camper que desea evaluar: "))
    if num_id in campers:
        nota_teorica = float(input("Ingrese la nota de la prueba teórica: "))
        nota_practica = float(input("Ingrese la nota de la prueba práctica: "))
        nota_quices_trabajos = float(input("Ingrese la nota de los quices/trabajos: "))
        
        nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quices_trabajos * 0.1)
        
        if nota_final >= 60:
            campers[num_id]['Estado'] = "Aprobado"
            print("¡Felicidades! El camper ha aprobado el módulo con una nota final de", nota_final)
        else:
            campers[num_id]['Estado'] = "Reprobado"  # Se añade el estado como "Reprobado" si la nota es inferior a 60
            print("El camper no ha aprobado el módulo. Su nota final es", nota_final)
    else:
        print("Camper no encontrado.")

# Menú para el Trainer
def menu_trainer(campers):
    while True:
        print("\n---Menú Trainer---")
        print("1. Ver datos de un camper")
        print("2. Evaluar un camper")
        print("3. Volver al menú principal")
        
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))
        
        if opcion == 1:
            num_id = int(input("Ingrese el número de identificación del camper que desea ver: "))
            if num_id in campers:
                print("Datos del camper:")
                print(buscar_camper(campers, num_id))
            else:
                print("Camper no encontrado.")
        elif opcion == 2:
            evaluar_camper(campers)
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Por favor ingrese una opción válida.")

# Menú para el Coordinador
def menu_coordinador(campers):
    while True:
        print("\n---Menú Coordinador---")
        print("1. Ver datos de un camper")
        print("2. Evaluar un camper")
        print("3. Modificar datos de un camper")
        print("4. Reportes")
        print("5. Salir")
        
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))
        
        if opcion == 1:
            num_id = int(input("Ingrese el número de identificación del camper que desea ver: "))
            if num_id in campers:
                print("Datos del camper:")
                print(buscar_camper(campers, num_id))
            else:
                print("Camper no encontrado.")
        elif opcion == 2:
            evaluar_camper(campers)
        elif opcion == 3:
            num_id = int(input("Ingrese el número de identificación del camper que desea modificar: "))
            if num_id in campers:
                modificar_camper(campers[num_id])
                print("Datos del camper modificados correctamente.")
            else:
                print("Camper no encontrado.")
        elif opcion == 4:
            menu_reportes(campers)
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Por favor ingrese una opción válida.")

# Función para el menú principal según el rol seleccionado
def menu_principal():
    campers = cargar_campers_json()
    rutas_ocupadas = {}

    while True:
        print("\n---Menú Principal---")
        print("1. Camper")
        print("2. Trainer")
        print("3. Coordinador")
        print("4. Salir")
        
        try:
            rol = int(input("Ingrese el número correspondiente a su rol: "))
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue
        
        if rol == 1:
            camper = capturar_datos_camper(campers, rutas_ocupadas)
            if camper:
                campers[camper['NumId']] = camper
                print("Datos del camper ingresados correctamente.")
                guardar_campers_json(campers)
        elif rol == 2:
            menu_trainer(campers)
        elif rol == 3:
            menu_coordinador(campers)
        elif rol == 4:
            print("¡Hasta luego!")
            guardar_campers_json(campers)
            break
        else:
            print("Rol no válido. Por favor ingrese un rol válido.")

# Función para guardar los campers en un archivo JSON
def guardar_campers_json(campers):
    with open('campers.json', 'w') as archivo_json:
        json.dump(campers, archivo_json)

# Función para cargar campers desde un archivo JSON
def cargar_campers_json():
    try:
        with open('campers.json', 'r') as archivo_json:
            return json.load(archivo_json)
    except FileNotFoundError:
        return {}

# Función para listar campers inscritos
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

# Función para listar entrenadores trabajando con CampusLands
def listar_entrenadores_campuslands(campers):
    # Suponiendo que solo los Trainers están asociados a CampusLands
    entrenadores_campuslands = set()
    for camper in campers.values():
        if camper['Estado'] != 'Inscrito':  # Se verifica que el camper no esté inscrito
            entrenadores_campuslands.add((camper['Nombre'], camper['Apellidos']))
    if entrenadores_campuslands:
        print("Entrenadores trabajando con CampusLands:")
        for nombre, apellidos in entrenadores_campuslands:
            print(f"{nombre} {apellidos}")
    else:
        print("No hay entrenadores trabajando con CampusLands.")

# Función para listar campers y trainers asociados a una ruta de entrenamiento
def listar_campers_trainers_ruta(campers):
    ruta = input("Ingrese la ruta de entrenamiento (NodeJS, Java, NetCore): ").lower()
    while ruta not in ["nodejs", "java", "netcore"]:
        print("Ruta de entrenamiento no válida. Por favor ingrese una de las opciones disponibles.")
        ruta = input("Ingrese la ruta de entrenamiento (NodeJS, Java, NetCore): ").lower()

    campers_ruta = [camper for camper in campers.values() if camper['Ruta'] == ruta]
    if campers_ruta:
        print(f"Campers asociados a la ruta de entrenamiento {ruta}:")
        for camper in campers_ruta:
            print(camper)
    else:
        print("No hay campers asociados a la ruta de entrenamiento especificada.")

    trainers_ruta = set()
    for camper in campers.values():
        if camper['Ruta'] == ruta and camper['Estado'] != 'Inscrito':  # Se verifica que el camper no esté inscrito
            trainers_ruta.add((camper['Nombre'], camper['Apellidos']))
    if trainers_ruta:
        print("Trainers asociados a la ruta de entrenamiento:")
        for nombre, apellidos in trainers_ruta:
            print(f"{nombre} {apellidos}")
    else:
        print("No hay trainers asociados a la ruta de entrenamiento especificada.")

# Función para mostrar el número de campers que aprobaron y perdieron cada módulo por ruta y entrenador
def mostrar_aprobados_perdidos(campers):
    # Inicializar un diccionario para almacenar los resultados
    resultados = {}

    # Recorrer cada camper
    for camper in campers.values():
        # Verificar que el camper no esté inscrito y tenga un estado
        if camper['Estado'] != 'Inscrito':
            # Clave para identificar el módulo y el entrenador
            clave = (camper['Ruta'], camper['Nombre'], camper['Apellidos'])

            # Incrementar el contador correspondiente según el estado del camper
            if camper['Estado'] == 'Aprobado':
                resultados[clave] = (resultados.get(clave, (0, 0))[0] + 1, resultados.get(clave, (0, 0))[1])
            elif camper['Estado'] == 'Reprobado':
                resultados[clave] = (resultados.get(clave, (0, 0))[0], resultados.get(clave, (0, 0))[1] + 1)

    # Mostrar los resultados
    print("Aprobados y perdidos por módulo y entrenador:")
    for clave, valor in resultados.items():
        ruta, nombre, apellidos = clave
        aprobados, perdidos = valor
        print(f"Ruta: {ruta}, Entrenador: {nombre} {apellidos}, Aprobados: {aprobados}, Perdidos: {perdidos}")

# Menú de reportes
def menu_reportes(campers):
    while True:
        print("\n---Módulo de Reportes---")
        print("1. Listar campers inscritos")
        print("2. Listar campers que aprobaron el examen inicial")
        print("3. Listar campers con bajo rendimiento")
        print("4. Listar entrenadores trabajando con CampusLands")
        print("5. Listar campers y trainers asociados a una ruta de entrenamiento")
        print("6. Mostrar número de campers que aprobaron y perdieron cada módulo")
        print("7. Volver al menú principal")
        
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))
        
        if opcion == 1:
            listar_campers_inscritos(campers)
        elif opcion == 2:
            listar_campers_aprobados(campers)
        elif opcion == 3:
            listar_campers_bajo_rendimiento(campers)
        elif opcion == 4:
            listar_entrenadores_campuslands(campers)
        elif opcion == 5:
            listar_campers_trainers_ruta(campers)
        elif opcion == 6:
            mostrar_aprobados_perdidos(campers)
        elif opcion == 7:
            break
        else:
            print("Opción no válida. Por favor ingrese una opción válida.")

# Ejecutar el menú principal
menu_principal()