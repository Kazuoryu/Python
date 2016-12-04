class persona(): #nombre clase
    edad=18 #variable de clase
    def __init__(self,nombre,nacionalidad): #variables de instancia
        self.nombre = nombre                #y definicion de la funcion
        self.nacionalidad = nacionalidad
    def nadar(self):
        print("Estoy nadando")

persona1 = persona("Diego","Español") #persona1
print(persona.edad)
print(persona1.nombre)
print(persona1.nacionalidad)

persona1.nadar() #Siempre que se llama a un metodo hay que llamarlo con el objeto y la funcion

