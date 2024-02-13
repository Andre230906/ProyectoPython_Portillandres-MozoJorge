import json
import os
def limpiar_terminal():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def add_campers():
    limpiar_terminal()
    print("""
            **********************
            *                    *
            * REGISTRO DE CAMPER *
            *                    *
            **********************
            """)
    with open("JSON/Campers.json", "r") as outfile:
        Data = json.load(outfile)


    newc = {}
    newc["ID"] = int(input("*Ingrese el ID (numero de documento) del camper que deseas agregar: "))
    newc["nombres"] = input("*Ingrese los nombres del camper                                   : ")
    newc["apellido"] = input("*Ingresa los apellidos del camper                                 : ")
    newc["ciudad"] = input("*Ingrese la ciudad del  camper que deseas agregar                 : ")
    newc["Direccion"] = input("*Ingrese la Dirección del camper que deseas agregar               : ")
    newc["Acudiente"] = input("*Ingrese El nombre del acudiente del nuevo camper                 : ")
    newc["N_celular"] = input("*Ingrese el numero de celular del nuevo camper                    : ")
    newc["N_fijo"] = input("*Ingrese el numero de teléfono fijo del nuevo camper              : ")
    newc["Estado"] = "inscrito"
    newc["Nota"] = "0"

    Data["Campers"].append(newc)

    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
        
def actualizar_datos_camper():
    edit = open("JSON/Campers.json")
    Data = json.load(edit)
    campers = Data["Campers"]
    IDi_camper = int(input("Ingresa el id del Camper que quieras actualizar: "))
    for camper in campers:
        if camper["ID"] == IDi_camper:
            
            nombres = input("Ingresa los nuevos nombres: ") 
            apellidos = input("Ingresa los nuevos apellidos: ")
            ciudad = input("Ingresa la ciudad a cambiar: ")
            Direccion = input("Ingrese la direccion a cambiar: ")
            Acudiente = input("Ingresa el acudiente a cambiar : ")
            N_celular = input("Ingresa el nuevo numero de celular: ")
            N_fijo = input("Ingresa el nuevo numero de teléfono fijo: ")
            
            camper["nombres"] = nombres
            camper["apellido"] = apellidos
            camper["ciudad"] = ciudad
            camper["Direccion"] = Direccion
            camper["Acudiente"] = Acudiente
            camper["N_celular"] = N_celular
            camper["N_fijo"] = N_fijo
            camper["Estado"] = N_fijo

    
    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)


def ev_camper():
    edit = open("JSON/Campers.json")
    Dat = json.load(edit)
    camp = Dat["Campers"]
    ID_camper = int(input("Ingrese el número de identificación del camper que desea hallar su calificacion final:"))
    for camp in camp:
        if camp["ID"] == ID_camper:  
            teo = float(input("Ingrese promedio de notas de la teorica: "))
            pra = float(input("Ingrese promedio de notas de la practica: "))
            pro = float(input("Ingrese promedio da la procedimental: "))
            final = (teo *  0.3) + (pra *  0.6) + (pro *  0.1)
            if final >=  60:
                camp['Estado'] = "Continua"  
                camp["nota"] = ("",final) 
                print("¡Este camper ha aprobado el filtro mensual con una nota final de", final)
            else:
                camp['Estado'] = "Reprobado"   
                camp["nota"] = ("",final)
                print("El camper no ha aprobado, Su nota final es", final)
        else:
            print("Camper no encontrado.")     
                         
                    
                      
    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Dat, outfile, indent=4)

def imprimir_todos_los_campers():
    print("""
            **********************
            *                    *
            *  IMPRIMIR CAMPERS  *
            *                    *
            **********************
            """)
    try:
        with open('JSON/Campers.json', 'r') as archivo:
            # Carga los datos del archivo
            datos = json.load(archivo)
            a = int(input("Ingresa (1) para continuar: "))
            if a == 1:
                for camper in datos['Campers']:
                    print("ID: ", camper['ID']) # Agrega una línea en blanco entre cada camper
                    print("Nombres: ", camper['nombres'])
                    print("Apellido:", camper['apellido'])
                    print("Ciudad:", camper['ciudad'])
                    print("Direccion:", camper['Direccion'])
                    print("Acudiente:", camper['Acudiente'])
                    print("N_celular:", camper['N_celular'])
                    print("N_fijo:", camper['N_fijo'])
                    print("Estado:", camper['Estado'])
                    print("")

                  # print(f"ID: {camper['ID']}, nombres: {camper['nombres']}, Apellido: {camper['apellido']}, ciudad: {camper['ciudad']}, direccion: {camper['Direccion']}, Acudiente: {camper['Acudiente']}, Ncelular: {camper['N_celular']}, Nfijo: {camper['N_fijo']}, Estado: {camper['Estado']}")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")

def camper_menu():
    while True:   
        print("""
            *********************
            *                   *
            *MENU ADMINISTRACION*
            *                   *
            *********************
            """)
        print("*Agregar Camper    (1)")
        print("*Notas Camper      (2)")
        print("*Actualizar Camper (3)")
        print("*Listar Campers    (4)")
        print("*Atras             (5)")
        
        opcion = input("Ingrese la opción deseada: ")
        
        opciones_dict = {
            1: add_campers,
            2: ev_camper,
            3: actualizar_datos_camper ,
            4: imprimir_todos_los_campers,
            5: lambda: print("Saliendo del menú de administración.")
        }
        
        if opcion.isdigit() and int(opcion) in range(1,  6):
            opciones_dict[int(opcion)]()
        elif opcion.lower() == '0':
            print("Saliendo del menú de administración.")
            break
        else:
            print("Ingrese una opción válida (1-5).")
            continue

camper_menu()
