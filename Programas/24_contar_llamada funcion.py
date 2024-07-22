'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */
'''
def contar_llamadas(funcion):
    def func_contar():
        func_contar.contar_llamada += 1
        print(f'la funcion "{funcion.__name__}" se ha llamado "{func_contar.contar_llamada}" vez/veces ')
        return funcion
    
    func_contar.contar_llamada = 0
    return func_contar



@contar_llamadas
def funcion_ejemplo_4():
    pass

def funcion_ejemplo_5():
    pass

def funcion_ejemplo_6():
    pass

funcion_ejemplo_4()
funcion_ejemplo_4()