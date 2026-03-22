#Pruebas de claude

###class estudiante:
    #def __init__(self, nombre, carrera, promedio):
        #self.nombre = nombre
        #self.carrera = carrera 
        #self.promedio = promedio 
    
    #def presentarse(self):
        #print(f"Hola soy {self.nombre}, estudio {self.carrera} y tengo un promedio de {self.promedio}")
    
    #def aprobo(self):
        #return self.promedio > 6
class animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"{self.nombre} hace {self.sonido}")
class perro(animal):
    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)
        self.raza = raza 
    def hacer_sonido(self):
        print(f"La raza {self.raza} hace {self.sonido}")
perro1 = perro("Rex", "guau", "Labrador")
perro1.hacer_sonido()  
print(perro1.raza)     