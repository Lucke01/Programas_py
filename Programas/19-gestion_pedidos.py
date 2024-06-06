'''DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */
'''
from enum import Enum

class Gestion_pedidos(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4
    
class Pedido:
    #el envio de forma predeterminado esta pendiente
    estado_pedido = Gestion_pedidos.PENDIENTE
    #atributos de instancia
    def __init__(self,id:int):
        self.id = id
    #metodos
    #funcionalidad de envio
    def enviar(self):
        if self.estado_pedido == Gestion_pedidos.PENDIENTE: # =>
            self.estado_pedido = Gestion_pedidos.ENVIADO
            self.mostrar_estado()
        else:
            print('el pedido ya fue enviado o cancelado')
    #funcionalidad de entrega        
    def entregar(self):
        if self.estado_pedido == Gestion_pedidos.ENVIADO: #=>
            self.estado_pedido = Gestion_pedidos.ENTREGADO
            self.mostrar_estado()
        else:
            print('el pedido no fue enviado')
    #funcionalidad de cancelar        
    def cancelar(self):
        if self.estado_pedido != Gestion_pedidos.ENTREGADO:
            self.estado_pedido = Gestion_pedidos.CANCELADO
            self.mostrar_estado()
        else:
            print('el pedido ya fue entregado, no se puede cancelar...')
    
    #funcionalidad que me muestra el estado del pedido 
    def mostrar_estado(self):
        print(f'el pedido {self.id} se encuentra: {self.estado_pedido.name}')
        

pedido_1 = Pedido(1)
pedido_1.enviar()
pedido_1.entregar()


pedido_2 = Pedido(2)
pedido_2.cancelar()

pedido_3 = Pedido(3)
pedido_3.cancelar()
