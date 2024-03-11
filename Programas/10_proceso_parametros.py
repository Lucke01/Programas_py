
'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
'''

#creo una excepcion:
class number_error(Exception):
    pass

def proceso_parametros(parametro:list):
    

    if len(parametro) < 3:
        raise IndexError()
    
    elif parametro[1] == 0:
        raise ZeroDivisionError()
    
    elif type(parametro[2]) == int:
        raise number_error('El segundo elemento no tiene que ser del tipo numerico')
    
    print(parametro[2])
    print(parametro[0] / parametro[1])
    print(parametro[2] + 'hola')

try:
    proceso_parametros([1,0,'navo',4])
except IndexError as e:
    print('el num de la lista debe ser mayor que 2')
    
except ZeroDivisionError as e:
    print('el segundo elemento de la lista tiene que ser distinto de 0 ')
    
except number_error as e:
    print(f'{e}')
    

except Exception as e:
    print(f'se produjo un error inesperado:{e}')
    
else:
    print('no ocurrio ningun error')

finally:
    print('el programa corre perfectamente')