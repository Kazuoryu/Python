def crearArchivo(): #creamos un metodo
    archivo=open("Datos.txt","w") #creamos atributo que crea un archivo de escritura
    archivo.close() #como por ahora no haremos nada mas lo cerramos

def escribirArchivo():
    archivo=open("Datos.txt","a")
    archivo.write("Diego Gonzalez\n")
    archivo.write("64567878545454\n")
    archivo.close

def leerArchivo():
    archivo=open("Datos.txt","r")
    linea=archivo.readline()
    while linea!="":
        print (linea)
        linea=archivo.readline()
    archivo.close()
leerArchivo()

print ("Operacion Realizada")

