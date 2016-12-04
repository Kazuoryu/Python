class persona: #clase
    nBrazos=0 #atributos
    nPierna=0
    cabello=True
    cCabello="Defecto"
    hambre=0
    
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

