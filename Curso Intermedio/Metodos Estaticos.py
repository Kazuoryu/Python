class persona():
    def __init__(self): #metodo inicial
        pass
    def brincar(self): #metodo 
        print("Salto")

    @classmethod #metodo de clase
    def correr(cls):
        print ("A la velocidad de la luz")
    @staticmethod
    def nadar(): #metodo statico
        print("Muy rapido")
Diego = persona()
Diego.nadar()
Diego.correr()
Diego.brincar()
