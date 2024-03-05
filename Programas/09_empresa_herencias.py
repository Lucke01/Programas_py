'''
DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser  , Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
'''

class Empleado():
    #creo constructor
    def __init__(self,nombre,ID):
        self.nombre = nombre
        self.ID = ID
    #metodo para identificarse
    
    def __str__(self):
        return f'empleado:{self.nombre} ,ID:{self.ID}'
    
    def identificarse(self):
        print(f'Nombre: {self.nombre}')
        print(f'ID: {self.ID}')

#Creo subclases

class Gerentes(Empleado):
    #metodo constructor heredando
    def __init__(self,nombre,ID):
        #heredo los metodos de empleado
        super().__init__(nombre,ID)
        self.empleados_monitoreo = []
        
    def mostrar_datos(self):
        print(f'gerente: NOMBRE :{self.nombre}, ID:{self.ID}')

    #creo metodo de agregar 
    def agregar(self,empleado):
        #si el empleado no esta en la lsita => agregalo
        if not empleado in self.empleados_monitoreo:
            self.empleados_monitoreo.append(empleado)
        else:
            #sino ya esta 
            print(f'el empleado:{empleado} ya esta en la lista...')

    #despedir empleado
    def despedir(self,empleado):
        #si el empleado esta en la lista => removerlo
        if empleado in self.empleados_monitoreo:
            self.empleados_monitoreo.remove(empleado)
        
        else:
            #sino no esta a cargo
            print(f'el gerente:{self.nombre},{self.id} no esta a cargo de dicho empleado')
            
    #cantidad de empleados
    def cantidad_empleados(self):
        print('monitoreando empleados: ')
        #para cada e(numero) y empleado enumerados, 
        for e,empleado in enumerate(self.empleados_monitoreo):
            print(f'{e + 1}:{empleado}')


#clase hija
class Gerentes_proyectos(Empleado):
    #metodo constructor heredando
    def __init__(self,nombre,ID):
        #heredo los metodos de empleado
        super().__init__(nombre,ID)
        self.proyectos_monitoreo = []
    #identificar gerente_proyectos
    def mostrar_datos(self):
        print(f'gerente de proyectos: NOMBRE :{self.nombre}, ID:{self.ID}')
        
    #agregar proyectos
    def agregar_proyectos(self,proyecto):
        #si el proyecto no esta en la lista => agregalo
        if not proyecto in self.proyectos_monitoreo:
            self.proyectos_monitoreo.append(proyecto)
        #sino:
        else:
            print(f'el proyecto{proyecto} ya esta en la lista')
    
    #quitar proyecto
    def eliminar_proyecto(self,proyecto):
        #si el proyecto esta en la lista => quitalo
        if proyecto in self.proyectos_monitoreo:
            self.proyectos_monitoreo.remove(proyecto)
        else:
            print(f'el gerente de proyectos: {self.nombre},{self.id} no esta a cargo de este proyecto...')
            
    #proyectos a cargo
    def cantidad_proyectos(self):
        print('monitoreo de proyectos...')
        for p,proyectos in enumerate(self.proyectos_monitoreo):
            print(f'{p+1}:{proyectos}')
            
            
#clase hija
class Programadores(Empleado):
    #metodo constructor heredando
    def __init__(self,nombre,ID):
        #heredo los metodos de empleado
        super().__init__(nombre,ID)
        self.lenguajes = []
    #identificar gerente_proyectos
    def mostrar_datos(self):
        print(f'Programador - NOMBRE :{self.nombre}, ID:{self.ID}')
    
    #agregar lenguaje:
    def agregar_lenguaje(self,lenguaje):
        #si el lenguaje no esta en la lista => agregalo
        if not lenguaje in self.lenguajes:
            self.lenguajes.append(lenguaje)
        #sino:
        else:
            print(f'{lenguaje} ya esta en la lista de: {self.nombre}')
    
    #lenguajes aprendidos
    def lenguajes_aprendidos(self):
        print('aprendimos: ')
        
        for l,lenguaje in enumerate(self.lenguajes):
            print(f'{l + 1} :{lenguaje}')


#creo objetos
gerente_principal = Gerentes('Sergio',598)
gerente_secundario = Gerentes('Camila',591)


#gerente de proyectos
gerente_proyectos = Gerentes_proyectos('Hector',584)
gerente_proyectos_2 = Gerentes_proyectos('Tiara',583)

#programadores
senior = Programadores('Lucas',570)
middle1 = Programadores('Zaira',575)
middle2 = Programadores('bastian',578)
middle3 = Programadores('Kiara',577)
junior = Programadores('Sebastian',579)


#GERENTES AGREGANDO EMPLEADOS
print('----------------------')
gerente_principal.agregar(junior)
gerente_principal.agregar(middle2)
gerente_principal.agregar(senior)

gerente_secundario.agregar(middle1)
gerente_secundario.agregar(middle3)



# gerente_principal.despedir(junior)
gerente_principal.cantidad_empleados()
gerente_secundario.cantidad_empleados()


print('----------------------')
gerente_proyectos.agregar_proyectos('Crypto_mercado')
gerente_proyectos.agregar_proyectos('banco nacion')
gerente_proyectos.agregar_proyectos('Csgo3')
gerente_proyectos.agregar_proyectos('Google_maps clon')
gerente_proyectos.cantidad_proyectos()

print('----------------------')
senior.agregar_lenguaje('c++')
middle1.agregar_lenguaje('python')
middle2.agregar_lenguaje('Js')

middle2.lenguajes_aprendidos()