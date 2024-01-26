'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''
#definimos funcion
def palindromos(palabra):
    #definimos parametro, transformalo en minusculas y remplaza espacio por comillas
    palabra = palabra.lower().replace(" ","")
    #retorname la palabra al reves
    return palabra == palabra[::-1]

#def funcion
def anagramas(palabra1,palabra2):
    #def parametros
    palabra1 = palabra1.lower().replace(" ","")
    palabra2 = palabra2.lower().replace(" ","")
    #retornamos en orden ascendente
    return sorted(palabra1) == sorted(palabra2)


def isograma(palabra):
    palabra = palabra.lower().replace(" ", "")
    return len(set(palabra)) == len(palabra)


#definimos palabras
def palabras():
    palabra1 = input('Ingrese una palabra: ')
    palabra2 = input('Ingrese una palabra: ')
    
    #creamos una implicacion
    if palindromos(palabra1):
        print(f'{palabra1} es palindromo')
    else:
        print(f'{palabra1} no es palindromo')
        
    #analogo con palabra2
    if palindromos(palabra2):
        print(f'{palabra2} es palindromo')
    else:
        print(f'{palabra2} no es palindromo')
    
    if anagramas(palabra1,palabra2):
        print(f'{palabra1} y {palabra2} son anagramas')
    else:
        print(f'{palabra1} y {palabra2} son anagramas')

    if isograma(palabra1):
        print(f'{palabra1} es isograma')
    else:
        print(f'{palabra1} no es isograma')
        
    if isograma(palabra2):
        print(f'{palabra2} es isograma')
    else:
        print(f'{palabra2} no es isograma')
        
palabras()