import datetime,time
import asyncio # asincronia

async def task(name:str, t:int):
        #defino el nombre de la tarea, la duracion y el inicio
        print(f'Tarea: {name}, Duracion: {t}s. Inicio: {datetime.datetime.now()} ')
        #termina el tiempo de ejecucion pero con espera
        await asyncio.sleep(t)
        # finaliza la tarea
        print(f'Tarea:{name}, fin: {datetime.datetime.now()} ')

#las quiero ejecutar en paralelo =>        


async def async_task():
    await asyncio.gather(task("C", 5), task("B", 3), task("A", 2))
    await task("D", 1)

asyncio.run(async_task())