class persona: #clase
    nBrazos=0 #atributos
    nPiernas=0
    cabello=True
    cCabello="Defecto"
    hambre=0

    def __init__(self): #definimos los valores que tendran al principio
                        #nuestros atributos
        self.nBrazos=2
        self.nPiernas=2
        
    def dormir(): #metodo
        pass
    def comer(self): #modifica el atributo hambre de a mi mismo
        self.hambre=0

class hombre:
    nombre="Defecto"
    sexo="M"
    def cambiarNombre(self,nombre): #modifica el atributo nombre que
        self.nombre=nombre #ademas recibe un nombre como parametro

class mujer:
    nombre="Defecto"
    sexo="F"

