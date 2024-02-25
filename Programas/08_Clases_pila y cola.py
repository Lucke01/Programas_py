#creo clase pila
class Pila():
    #metodo constructor
    def __init__(self):
        self.items = []
        
    #agregar elementos
    def agregar(self,elemento):
        #agrego items con append
        self.items.append(elemento)
    
    #eliminar ultimo elemento
    def deletear(self):
        delete_item = self.items.pop()
        return delete_item
    
    #cuento la cantidad de elementos tq
    
    def elementos(self):
        cantidad = len(self.items)
        
        #si hay 0 elementos => retorna:
        if cantidad == 0:
            return f'no quedan mas elementos'
        
        else:
            #sino retorna la cantidad de elementos que hay
            return cantidad
    #definimos obtener informacion
    def informacion(self):
        print(self.items)
        
        
#creando objeto
stack_1 = Pila()

#usando el metodo agregar
stack_1.agregar(1)
stack_1.agregar('algo')
stack_1.agregar(637)

cantidad_elementos = stack_1.elementos()
#como es un return =>
print(f'tenemos una cantidad de :{cantidad_elementos} elementos' )

#obtener informacion =>
stack_1.informacion()

#elimino algunos elementos
eliminando = stack_1.deletear()
print(f'se deleteo este elemento:{eliminando}')

print('la pila actual me quedo:')
stack_1.informacion()


#creo clase cola:
#class cola

class Cola():
    #constructor:
    def __init__(self):
        #lista vacia
        self.items = []
    #creo metodo agregar
    def agregar(self,elemento):
        #le digo que agregue elementos en el primer lugar
        self.items.insert(0,elemento)
    
    def deletear(self):
        item_deleteado = self.items.pop(0)
        return item_deleteado
    
    def contar_elemetos(self):
        contar = len(self.items)
        
        #si:
        if contar == 0:
            return 'no hay elementos'
        
        else:
            return contar
        
    def informacion(self):
        print(self.items)
        
#creo objeto de cola

queue = Cola()

#añadir elementos a mi lista
queue.agregar('algo')
queue.agregar('hola')
queue.agregar(94)
queue.agregar('fjbasdñ')
#obtener cantidad de elementos 

numero_elementos = queue.contar_elemetos()
print(f'tenemos : {numero_elementos} elementos')

#obtener informacion
queue.informacion()

#deletear elementos
eliminar = queue.deletear()
print(f'hemos eliminado el elemento:{eliminar}')


#obtener informacion final de la cola
queue.informacion()
