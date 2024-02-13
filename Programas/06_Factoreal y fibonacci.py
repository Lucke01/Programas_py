'''
* DIFICULTAD EXTRA 1(opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número)..
 */
'''

def factoreal(n):
    # 1! = 0 y 0! = 1
    if n == 1 or n == 0:
        return 1
    #formula de factoreal => [n! = n * (n-1)!] 
    return n * factoreal(n-1)

#llamo a una variable que sera nuestra funcion 
resultado_factoreal = factoreal(5)
print(resultado_factoreal)


'''
* DIFICULTAD EXTRA 2(opcional):
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
'''

#creo la formula de fibonacci
def fibonacci(n):
    #creo las restricciones
    # los numeros tienen que ser positivos
    if (n < 0):
        return None
    # si el numero es 0 => es 0
    elif(n == 0):
        return 0
    # si el numero es 1 => es 1
    elif(n == 1):
        return 1
    
    #si el numero es distinto de 0 y 1 =>
    else:
        return fibonacci(n-1) + fibonacci(n-2)

sucesion_fibonacci = fibonacci(11)

print(f'el valor del calculo de fibonacci es: {sucesion_fibonacci}')




#creo la formula de fibonacci dentro de un diccionario vacio que guarda valores

# def fibonacci(n, diccionario_valores = {}):
#     #creamos las restricciones
#     #n es natural => n < 0 no existe
#     if (n < 0):
#         return f'los numeros tienen que ser mayores que 0'
#     #n = 0
#     elif (n == 0):
#         return 0
#     #n=1
#     elif (n == 1): 
#         return 1
    
#     #si el numero esta en el diccionario retornar:
#     elif n in diccionario_valores:
#         return diccionario_valores[n]
    
#     #si no es ni el 0 o el 1 entonces:
#     else:
#         resultado = fibonacci(n-1, diccionario_valores) + fibonacci(n-2, diccionario_valores)
#         #guardamos el valor en el diccionario
#         diccionario_valores[n] = resultado
#         return resultado

# sucesion_fibonacci = fibonacci(10)
# print(f'el valor del calculo de fibonacci es: {sucesion_fibonacci}')

