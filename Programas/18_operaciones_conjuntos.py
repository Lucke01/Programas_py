#creo varios conjuntos
A = {1,2,3,4,5}
B = {1,5,7,'chain'}

# UNION [AUB]

union = A.union(B)
print(f'operacion de conjuntos union: {union}')


#INTERCECCION [AnB]
interseccion = A.intersection(B)
print(f'operacion de conjuntos interseccion: {interseccion}')

#DIFERENCIA [A-B]
diff = A.difference(B)
print(f'operacion de conjuntos diferencia: {diff}')

#DIFERENCIA SIMETRICA [AΔB]
difΔ = A.symmetric_difference(B)
print(f'operacion diferencia simetrica: {difΔ}')