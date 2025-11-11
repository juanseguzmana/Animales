follow = True

animals = []

while follow:

    print('')
    print('* RIWI ZOO *')
    print('1. Agregar Animal')
    print('2. Ver animales')
    print('3. Borrar animal por (ID)')
    print('4. Borrar animal por (Nombre)')
    print('5. Borrar Todos')
    print('6. Listar animal por (ID)')


    try:
        desicion = int(input('¿Qué desea hacer?: '))
        if(desicion == 1):
            print('Porfavor escriba el nombre de un nuevo animal')
            print('')
            new_animal = input('Ingreso un nuevo animal: ')
            animals.append(new_animal)
            continue

        elif(desicion == 2):
            print('**********')
            print('*******')
            print('')
            print(animals)
            print('')
            print('**********')
            print('*******')
            continue

        elif(desicion == 3):
            try:
                if(animals != ""):
                    indexDelete = int(input('¿Cual es el ID del animal a eliminar?: '))
                    animals.pop(indexDelete)
                else:
                    print('')
                    print('Lo sentimos no tenemos registro de animales en el sistema')
                    continue
            except IndexError:
                print('No existe animal por ese ID')
        elif(desicion == 4):
            nameDelete = input('¿Cual es el nombre animal a eliminar?: ')
            animals.remove(nameDelete)
        elif(desicion == 5):
            animals.clear()
            continue
        elif(desicion == 6 and animals != ""):
            index = int(input('¿Cual es el ID a visualizar?: '))
            print('**********')
            print('*******')
            print('')
            print(animals[index])
            print('')
            print('**********')
            print('*******')
            continue
        else:
            print('Lo sentimos algo no es un valor valido')
            print('Por favor seleccione una opcion')
            continue

    except ValueError:
        print('El valor no puede ser un texto')
        continue
