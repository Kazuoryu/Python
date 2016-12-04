class persona ():
    def __init__(self):
        pass
 
    def despedir(self):
        print ("Adios")

    @classmethod #Si no añadimos esto dara error a la hora de iniciar el script
    def saludar(cls,nombre): #Definimos un metodo de clase
        print ("Estoy Saludando"+nombre)
persona.saludar("Diego")
