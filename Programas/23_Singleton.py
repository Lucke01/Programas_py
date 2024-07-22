''''
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email), recuperar los datos del usuario y borrar los datos de la sesión.
 */
'''

class Sesion_usuario:
    
    _instance = None
    #datos
    id:None
    username:None
    name:None
    email:None
    
    

    #creo el constructor del singleton
    def __new__(cls):
        #si no existe la instancia => la creamos
        if not cls._instance:
            cls._instance = super(Sesion_usuario, cls).__new__(cls)
        return cls._instance
    
    #creo funcion de clase
    def set_datos(self, id, username, name, email):
        #creo atributos
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    #funcion para recuperar datos
    def get_datos(self):
        return f'{self.id},{self.username},{self.name},{self.email}'
    
    #funcion para deletear datos    
    def clear_datos(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None
        

sesion1 = Sesion_usuario()
sesion1.set_datos(1,'lucke01','lucke','any')
#obtengo datos
print(sesion1.get_datos())


sesion2 = Sesion_usuario()
sesion2.clear_datos()

sesion3 = Sesion_usuario()
print(sesion3.get_datos())
