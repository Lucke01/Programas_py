def navegacion_web():
    #creamos una pila
    stack = []
    #creo bucle
    while True:
        #creo una accion que interactue con el usuario
        accion = input("Añade una url o interactua con palabras 'adelante/atras/salir: ' ")
        
        #que pasa si accion es:
        if accion == 'salir':
            print('saliendo del navegador')
            break
        elif accion == 'adelante':
            pass
        elif accion == 'atras':
            #creamos la condicion de ejecucion:
            if stack > 0:
                stack.pop()
            
        
        else:
            #se le agrefa lo que el usuario diga:
            stack.append(accion)
        
        #condicionamos el accion
        if len(stack) >0:
            
            print(f'has navegado a la web: {stack[len(stack) - 1]}')
        else:
            print('estas en la pagina de inicio.')
        


#llamo al programa
navegacion_web()




def shareded_printered():
    
    queue = []
    
    while True:
        accion = input('Añade un documento selecciona imprimir /salir: ')
        
        if accion == 'salir':
            break
        
        elif accion == 'imprimir':
            if len(queue) > 0:
                print(f'imprimiendo: {queue.pop(0)}')
            
            
            
        
        elif accion == 'añadir':
            pass
        
        else:
            queue.append(accion)
            
            
        print(f'cola de impresion: {queue}')
        

shareded_printered()