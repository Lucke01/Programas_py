lista = [1,2,3,4,5]
for e in lista:
    print(f'iterando los elementos de la lista; e = {e}')
    
#TUPLA
tupla = (1,2,3,4,5)
for t in tupla:
    print(f'iterando los elementos de la tupla; t = {t}')
    
#DICCIONARIO
    #=> valores
dicc = {1:'a',2:'b',3:'c',4:'d',5:'e'}.values()
for d in dicc:
    print(f'iterando los elementos del dicc(values); d = {d}')
    
    #=> keys
diccionario = {1:'a',2:'b',3:'c',4:'d',5:'e'}
for d in dicc:
    print(f'iterando los elementos del dicc(keys); d = {d}')

#range
print(*[i for i in range(1,12)], sep ="/n")

#cadena de texto
cadena = 'Iteraciones'

for l in cadena:
    print(f'l = {l}')
    