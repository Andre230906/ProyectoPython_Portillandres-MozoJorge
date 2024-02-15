import json
from os import system

def ingresar_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():  
            return valor
        else:
            print("Por favor, ingrese un valor numérico.")

def registrar_trainer():
    with open("JSON/Trainers.json", "r") as outfile:
        Data = json.load(outfile)


    nuevo_trainer = {}
    ultimo_id = max([trainer["ID"] for trainer in Data["Trainers"]], default=0)
    nuevo_id = ultimo_id + 1
    nuevo_trainer["ID"] = nuevo_id
    nuevo_trainer["N_documento"] = ingresar_numero("Ingrese el numero de documento del nuevo trainer: ")
    nuevo_trainer["nombre"] = input("Ingrese el primer nombre del nuevo trainer: ")
    nuevo_trainer["apellido"] = input("Ingrese el primer apellido del nuevo trainer: ")
    nuevo_trainer["N_celular"] = ingresar_numero("Ingrese el numero de celular del nuevo trainer: ")
    nuevo_trainer["Jornada"] = "No asignado"

    Data["Trainers"].append(nuevo_trainer)

    with open("JSON/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def mostrar_info_trainers():
    with open("Datas/Trainers.json", "r") as outfile:
        Data = json.load(outfile)

        trainers = Data["Trainers"]
        while True:
            try:
                ID_trainer = int(input("Ingresa el id del Trainer del que quieras ver la información: "))
                print("\n")

                for trainer in trainers: 
                    if trainer["ID"] == ID_trainer:
                        for key, value in trainer.items():
                            print(f"{key}: {value}")
                        print("\n")    
            except ValueError:
                print("\nPor favor ingrese un  valor numerico")            
            break    
        
def jornada_trainer():
    with open("Datas/Trainers.json", "r") as outfile:
        Data = json.load(outfile)

    trainers = Data["Trainers"]
    while True:
        try:
            ID_trainer = int(input("Ingrese el ID del trainer al cual desea asignarle un horario: "))
            for trainer in trainers:
                if trainer["ID"] == ID_trainer:
                    print("\nJornadas:")
                    print("1. Mañana (6:00 a.m - 2:00 p.m)")
                    print("2. Tarde (2:00 p.m - 10:00 p.m)")
                    
                    opcion = input("Seleccione la jornada que desea asignar: ")
                    system("clear")

                    if opcion == '1':
                        jornada = "Mañana"
                        trainer["Jornada"] = jornada
                    elif opcion == '2':
                        jornada = "Tarde"
                        trainer["Jornada"] = jornada
                    else:
                        print("Ingrese una opción válida")
        except ValueError:
            print("\nIngrese un valor numérico")
        break

    with open("Datas/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def actualizar_trainers():
    editacion = open("Datas/Trainers.json")
    Data = json.load(editacion)
    trainers = Data["Trainers"]
    ID_trainer = int(input("Ingresa el id del trainer que quieras actualizar: "))
    for trainer in trainers:
        if trainer["ID"] == ID_trainer:
            
            N_documento = input("Ingresa el nuevo numero de documento: ")
            nombre = input("Ingresa el nuevo primer nombre: ") 
            apellido = input("Ingresa el nuevo apellido: ")
            N_celular = input("Ingresa el nuevo numero de celular: ")
            
            trainer["N_documento"] = N_documento
            trainer["nombre"] = nombre
            trainer["apellido"] = apellido
            trainer["N_celular"] = N_celular
    
    with open("Datas/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
        
def main_menu():
    while True:
        print("Menú:")
        print("1. Registrar Trainer")
        print("2. Mostrar Info Trainers")
        print("3. Asignar Jornada a Trainer")
        print("4. Actualizar Trainers")
        print("5. Salir")
        
        choice = input("Ingrese su elección: ")
        
        if choice == '1':
            registrar_trainer()
        elif choice == '2':
            mostrar_info_trainers()
        elif choice == '3':
            jornada_trainer()
        elif choice == '4':
            actualizar_trainers()
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Llamada a la función principal para iniciar el menú
main_menu()