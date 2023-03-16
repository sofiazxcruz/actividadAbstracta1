from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractmethod
    def presentarse(self):
        pass


class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso
    
    def presentarse(self):
        print(f"//Buenos días, mi nombre es {self.nombre}, tengo {self.edad} años\n y soy estudiante en la {self.curso}//")


class Hobby(Persona):
    def __init__(self, nombre, edad, gusto, grupo):
        super().__init__(nombre, edad)
        self.gusto = gusto
        self.grupo = grupo
    
    def presentarse(self):
        print(f"\n//Buenas tardes, mi nombre es {self.nombre}, tengo {self.edad} años\n y me gusta escuchar {self.gusto}, en especial de {self.grupo}//")


class MadreFamilia(Persona):
    def __init__(self, nombre, edad, hijos, hijoP, hijoG):
        super().__init__(nombre, edad)
        self.hijos = hijos
        self.hijoP = hijoP
        self.hijoG = hijoG
        
    
    def presentarse(self):
        print(f"\n//Buenas noches, mi nombre es {self.nombre}, tengo {self.edad} años\n y soy madre luchona de {self.hijos}, un {self.hijoP} y un {self.hijoG}//")

persona1 = Estudiante("Martha Sofia", 19, "Universidad de Oriente")
persona2 = Hobby("Sofia Cruz", 19, "música", "Twice")
persona3 = MadreFamilia("Sofia Martha", 19, 2, "Perro", "Gato")

personas = [persona1, persona2, persona3]

for persona in personas:
    persona.presentarse()
