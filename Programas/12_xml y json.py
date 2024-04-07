import os
import xml.etree.ElementTree as xml #es un modulo que nos permite estructurar mas facilmente el fichero


archivo_xml = 'archivo.xml'
archivo_json = 'archivo.json'
#creo clase
class info:
    #creo constructor
    def __init__(self,nombre,edad,fecha_nacimiento,lenguajes_programacion):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programacion = lenguajes_programacion
        
#usando with open creamos el fichero
with open(archivo_xml ,'r') as xml_info:
    #operacion que le paso el texto y genera los datps
    root = xml.fromstring(xml_info.read())
    
    #recuperamos los datos (find)
    nombre = root.find('nombre').text
    edad = root.find('edad').text
    fecha_nacimiento = root.find('fecha_nacimiento').text
    #lista vacia
    lenguajes_programacion = []
    #recorro la lista
    for item in root.find('lenguajes_programacion'):
        #accedo a la lista y accedo al texto de los items
        lenguajes_programacion.append(item.text)
    
    
    #creo una variable
    xml_class = info(nombre,edad,fecha_nacimiento,lenguajes_programacion)
    
    print(xml_class.__dict__) #obtenemos el json desde el xml
    
    
#---> JSON
import json

with open(archivo_json ,'r') as json_info:
    json_dict = json.load(json_info)
    json_class = info(
                json_dict['nombre'],
                json_dict['edad'],
                json_dict['fecha_nacimiento'],
                json_dict['lenguajes_programacion']
                )
            
    
    print(json_class.__dict__)
    
os.remove(archivo_xml)
os.remove(archivo_json)
