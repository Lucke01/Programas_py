
'''
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
'''
#creo una funcion que intercambie variables por valor
def intercambio_valor(a,b):
    valor = a
    a = b
    b = valor
    return a,b

#creo variables originales
w = 8
x = 4
#llamo a la funcion
y,z = intercambio_valor(w,x)

print(f'las variables por fuera son: W = {w},  X = {x}')
print(f'las variables intercambiadas por valor son: Y = {y}, Z = {z} ')


#creo una funcion que intercambie variables por referencia

def intercambio_referencia(lista):
    valor = lista
    lista[0] = lista[1]
    lista[1] = valor
    return lista

#creo una lista original
lista_original = [10,20]
#llamo a la funcion
lista_nueva = intercambio_referencia(lista_original.copy())

print(f'la lista original es: {lista_original}')
print(f'la lista nueva es: {lista_nueva}')
