import random,threading,time
'''
DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
'''


def proceso_pedido(nombre_plato:str , confirmar_callback, listo_callback, entregado_callback):
    def proceso():
            confirmar_callback(nombre_plato)
            time.sleep(random.randint(1,10))
            listo_callback(nombre_plato)
            time.sleep(random.randint(1,10))
            entregado_callback(nombre_plato)
            
        #asincronia
    threading.Tread(target=proceso).start()

def confirmar_pedido(nombre_plato:str):
    print(f'tu pedido {nombre_plato} ha sido confirmado! .')
    
def pedido_listo(nombre_plato:str):
    print(f'tu pedido {nombre_plato} esta listo')
    
def entrega_pedido(nombre_plato:str):
    print(f'tu pedido {nombre_plato} ha sido entregado')
    

proceso_pedido('Cheese Burger',confirmar_pedido,pedido_listo,entrega_pedido)
proceso_pedido('Cheese Burger XL',confirmar_pedido,pedido_listo,entrega_pedido)
proceso_pedido('quarter libra xxl',confirmar_pedido,pedido_listo,entrega_pedido)
proceso_pedido('Milanga',confirmar_pedido,pedido_listo,entrega_pedido)