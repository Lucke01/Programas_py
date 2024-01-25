'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
'''

def extra(texto1 , texto2):
    #creo una variable
    count = 0
    #creo un for para tener numeros del 1 al 100
    for x in range(1,101):
        #si cumple ambas condiciones => mostra los dos parametros
        if x % 3 == 0 and x % 5 == 0:
            print(f'{texto1} {texto2} ')
        #si cumple que x es multiplo de 3 => mostra parametro1
        elif x % 3 == 0:
            print(f'{texto1} ')
        #si cumple que x es multiplo de 5 => mostra parametro1    
        elif x % 5 == 0:
            print(f'{texto2} ')
        #entonces mostrame los x y a la variable sumale 1
        else:
            print(x)
            #le sumamos 1 
            count +=1
    #retornamos contar            
    return f'Hubo {count} numeros que no cumplian las condiciones'

print(extra('Fizz','Buzz'))