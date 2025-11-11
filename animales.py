follow = True
animals = []

while follow:
    print('')
    print('* RIWI Z00-L0GIC *')
    print('Seleccione una opción:')
    print('----------------------------------')
    print('1. Agregar animal')
    print('2. Ver animales')
    print('3. Borrar animal por ID')
    print('4. Borrar animal por nombre')
    print('5. Borrar todos')
    print('6. Ver animal por ID')
    print('7. Salir')
    print('----------------------------------')

    try:
        decision = int(input('¿Qué desea hacer?: '))

        if decision == 1:
            new_animal = input('Ingrese el nombre del nuevo animal: ')
            animals.append(new_animal)
            print(f'"{new_animal}" agregado correctamente.')
            continue

        elif decision == 2:
            if animals:
                print('\n********** LISTA DE ANIMALES **********')
                for i, animal in enumerate(animals, start=1):
                    print(f'{i}. {animal}')
                print('***************************************')
                print(f'Total: {len(animals)} animales.\n')
            else:
                print('No hay animales registrados.')
            continue

        elif decision == 3:
            if not animals:
                print('No hay animales para eliminar.')
                continue

            try:
                indexDelete = int(input('Ingrese el ID del animal a eliminar: ')) - 1
                animals.pop(indexDelete)
                print('Animal eliminado correctamente.')
            except IndexError:
                print('No existe un animal con ese ID.')
            continue

        elif decision == 4:
            if not animals:
                print('No hay animales registrados.')
                continue

            nameDelete = input('Ingrese el nombre del animal a eliminar: ')
            if nameDelete in animals:
                while nameDelete in animals:
                    animals.remove(nameDelete)
                    print(f'Se eliminaron Total: {len(animals)} de animales llamados "{nameDelete}".')
            else:
                print(f'No se encontró un animal con el nombre "{nameDelete}".')
            continue

        elif decision == 5:
            if animals:
                animals.clear()
                print('Todos los animales fueron eliminados.')
            else:
                print('La lista ya está vacía.')
            continue

        elif decision == 6:
            if not animals:
                print('No hay animales registrados.')
                continue

            try:
                index = int(input('Ingrese el ID del animal a visualizar: ')) - 1
                print('\n********** ANIMAL **********')
                print(animals[index])
                print('****************************\n')
            except IndexError:
                print('No existe un animal con ese ID.')
            continue

        elif decision == 7:
            print('Hasta luego')
            follow = False
            break

        else:
            print('Por favor seleccione una opción válida.')
            continue

    except ValueError:
        print('Error: debe ingresar un número.')
        continue
