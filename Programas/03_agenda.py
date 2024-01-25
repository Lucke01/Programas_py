'''
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
'''

#def funcion agenda
def agenda():
    #def diccionario vacio
    mi_agenda = {}
    
    #def funcion de ingresar contacto
    def ingresar_contacto():
        cel = input('Ingrese su numero: ')
        #con if vamos a obligar que sea digito y que tenga 10 digitos
        if cel.isdigit() and len(cel) > 0 and len(cel) <= 10:
            mi_agenda[nombre] = cel
        else:
            print('debes introducir tu numero de telefono de 10 digitos...')
    #creamos un bucle que sea True => ejecutable
    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        #creamos una variable que nos permita decidir:
        elegir_opcion = input("\nSeleccione una opcion: ")
        #en caso de coincidir
        match elegir_opcion:
            #caso 1:
            case '1':
                #usuario elige nombre a buscar
                nombre = input('Introduce el nombre del usuario: ')
                #si se encuentra =>
                if nombre in mi_agenda:
                    print(f'el telefono de:{nombre} es: {mi_agenda[nombre]}')
                #sino:
                else:
                    print(f'no se encuentra el contacto: {nombre}')

            #caso 2:
            case '2':
                #usuario elige nombre
                nombre = input('introduce el nombre del contacto: ')
                #mencionamios la funcion para registrar contacto
                ingresar_contacto()
            
            #caso 3
            case '3':
                #usuario elige nombre
                nombre = input('introduce el nombre del contacto: ')
                #si el nombre existe agregar a la agenda
                if nombre in mi_agenda:
                    ingresar_contacto()
                #sino:
                else:
                    print(f'no se encuentra el contacto: {nombre}')

            #caso 4
            case '4':
                #usuario elige nombre
                nombre = input('introduce el nombre del contacto: ')
                #si el nombre existe => deletear
                if nombre in mi_agenda:
                    del mi_agenda[nombre]
                #sino:
                else:
                    print(f'no se encuentra el contacto: {nombre}')

            #caso 5
            case '5':
                print('saliendo de la agenda')
                break
            
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")
agenda()