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
        self.hambre=5

class hombre(persona): #Hombre hereda el metodo y los atributos de persona
    nombre="Defecto"
    sexo="M"
    def cambiarNombre(self,nombre): #modifica el atributo nombre que
        self.nombre=nombre #ademas recibe un nombre como parametro

class mujer(persona): #Mujer hereda el metodo y los atributos de persona
    nombre="Defecto"
    sexo="F"

Diego=hombre() #Creamos un objeto llamado Diego y sera de la clase hombre
Diego.comer() #ejecutamos un metodo con nuestro objeto Diego
print (Diego.hambre) #mostramos el valor de hambre despues de ejecutar el metodo
