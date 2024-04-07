import unittest
from datetime import datetime,date



#creo dos casos de prueba
class TestDatos(unittest.TestCase):

    #creo un  'contexto' con datos
    def setUp(self) -> None:
        self.datos = {
            'name' :'Juan',
            'age'  :25,
            'birth_date' : datetime.strptime('15-08-98',  "%d-%m-%y").date(),
            'programming_languajes' : ['python','c++','java','js']
        }
        
    #creo test
    def test_fields_exists(self):
        #me fijo si existe ese campo en data 
        self.assertIn('name', self.datos)
        self.assertIn('age', self.datos)
        self.assertIn('birth_date', self.datos)
        self.assertIn('programming_languajes', self.datos)
    
    
    #creo test
    def test_data_is_correct(self):
        self.assertIsInstance(self.datos['name'],str)
        self.assertIsInstance(self.datos['age'],int)
        self.assertIsInstance(self.datos['birth_date'],date)
        self.assertIsInstance(self.datos['programming_languajes'],list)

unittest.main()