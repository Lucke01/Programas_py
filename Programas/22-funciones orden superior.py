from datetime import datetime
'''
DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
'''

#creo un mapa
estudiantes = [
    {'nombre' : 'Juan', 'cumpleaños':'12/05/2004', 'notas':[4,6,5,8]},
    {'nombre' : 'Pedro', 'cumpleaños':'17/10/2000', 'notas':[4,3,8,4]},
    {'nombre' : 'Bruno', 'cumpleaños':'04/09/1997', 'notas':[3,1,6,7]},
    {'nombre' : 'Federico', 'cumpleaños':'25/03/1999', 'notas':[9,8,10,9]},
    {'nombre' : 'Marcis', 'cumpleaños':'20/01/1990', 'notas':[9,10,10,8]}
]


#Promedio
#creo una funcion que me dice el promedio de las notas
def promedio(notas):
    return sum(notas) / len(notas)

#usando map creamos una lista con nombre y notas
print(list(map(lambda estudiante: {
            'nombre':estudiante['nombre'],
            'promedio':promedio(estudiante['notas'])}, estudiantes))
    )

#Mejores
print(
    list(
        map(lambda estudiante:
        estudiante['nombre'],
        filter(lambda estudiante: promedio(estudiante['notas']) >= 9 ,estudiantes)
        )
    )
)

#fecha nacimiento ordenada

print(sorted(estudiantes, key = lambda estudiante:datetime.strptime(estudiante['cumpleaños'],"%d/%m/%Y"), reverse=True))

#calificacion mas alta
print(max(map(lambda estudiante: max(estudiante['notas']),estudiantes)))