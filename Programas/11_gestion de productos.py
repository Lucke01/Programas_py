import os
#como tendremos muchos iteracciones con el usuario inifinitamente hasta romperlo => usar while 

#creo el fichero
file_name = "Gestion de ventas.txt"

open(file_name,'w')
    

while True:
    #control de gestion de inventario
    print('1 - añadir producto')
    print('2 - consultar producto')
    print('3 - actualizar producto')
    print('4 - borrar producto')
    print('5 - mostrar productos')
    print('6 - calcular venta total')
    print('7 - calcular venta por producto')
    print('8 - salir')
    
    #creo una variable donde el usuario va a seleccionar su opcion
    opcion = input('selecciona una opcion: ')
    
    #creo un if talque cada opcion corresponde a un bloque de codigo 
    if opcion == "1":
        #tenemos que recolectar la info de los productos con restriccion
        nombre =input('agrega el nombre del producto: ')
        cantidad =input('cantidad: ')
        precio = input('precio: $ ')
    
        #tenemos que guardarlo en el file usando el parametro "append"
        with open (file_name, "a") as file:
            file.write(f'{nombre}, {cantidad}, {precio} \n')
        
        
    elif opcion == "2":
        nombre =input('selecciona el nombre del producto: ')
        #abrimos el fichero en modo read
        with open(file_name, 'r') as file:
            #creo un for de cada linea del archivo
            for line in file.readlines():
                #corto la cadena y me quedo con el primer elemento
                if line.split(", ")[0] == nombre:
                    print(line)
                    break
            
    elif opcion == "3":
        #consultar lo que queremos actualizar
        nombre =input('selecciona el producto que deseas actualizar: ')
        cantidad =input('cantidad: ')
        precio = input('precio: $ ')
        #abrimos el archivo en readmode
        with open(file_name, 'r') as file:
            #creo variable linea para almacenar 
            lines = file.readlines()
            
        #abrimos el archivo
        with open(file_name, 'w') as file:
            #quiero recorrer el fichero
            for line in lines:
                #separar linea por espacio y coma
                if line.split(", ")[0] == nombre:
                    #si existe, lo actualizamos
                    file.write(f'{nombre}, {cantidad}, {precio} \n')
                #sino...
                else:
                    file.write(line)
                    
    elif opcion == "4":
        #consultar el producto que queremos eliminar
        nombre =input('selecciona el producto que deseas borrar: ')
        #abro el fichero para leerlo
        with open(file_name, 'r') as file:
            #creo variable linea para almacenar 
            lines = file.readlines()
            
        #abrimos el archivo para sobreescribir
        with open(file_name, 'w') as file:
            #quiero recorrer el fichero
            for line in lines:
                #separar linea por espacio y coma si no coincide => mantenerlo
                if line.split(", ")[0] != nombre:
                    #si existe, lo actualizamos
                    file.write(line)
                
    elif opcion == "5":
        #mostrar archivo
        with open(file_name,'r') as file:
            print(file.read())
    
    elif opcion == "6":
        #creo una variable
        total = 0
        #tenemos que leer el fichero
        with open(file_name,'r') as file:
        #tenemos que recorrer el fichero
            for line in file.readlines():
                #hay que acceder a la cantidad y al precio
                componentes = line.split(", ")
                cantidad = int(componentes[1])
                precio = float(componentes[2])
                #definimos total
                total += cantidad * precio
        print(f' el total es de: ${total}')
    elif opcion == "7":
        #pido el producto que quiero calcular
        nombre =input('selecciona el producto que deseas calcular: ')
        total = 0
        #tenemos que leer el fichero
        with open(file_name,'r') as file:
        #tenemos que recorrer el fichero
            for line in file.readlines():
                #hay que acceder a la cantidad y al precio
                componentes = line.split(", ")
                if componentes[0] == nombre:
                    cantidad = int(componentes[1])
                    precio = float(componentes[2])
                    #definimos total
                    total += cantidad * precio
                    break
        print(total)
    #como la opcion 8 es salir => rompemos bucle y eliminamos el fichero
    elif opcion == "8":
        #delete
        os.remove(file_name)
        break
    
    else:
        print('selecciona una de las opciones disponibles')