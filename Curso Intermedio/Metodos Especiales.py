class clase ():
    def __new__(cls):
        print("new")
        return super().__new__(cls)
    def __init__(self): #El init es un metodo especial debido a los guiones
        print("Init")

c=clase()


    
    #El init solo se inicia si recive una instancia por eso
#hay que poner el super si lo quitamos solo devolvera el new
