import time

#creo funcion temporizador
def temporizador(segundos):
    while segundos:
        #divido los segundos por 60 
        min,seg = divmod(segundos, 60)
        #el tiempo lo marco en dos digitos formato minutos y seg
        tiempo = '{:02d}:{:02d}'.format(min,seg)
        print (tiempo,end="\r")
        time.sleep(1)
        segundos -= 1
    
    print('el tiempo ha finalizado')
    
temporizador(10)
    