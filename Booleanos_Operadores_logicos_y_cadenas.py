
#CADENAS
#comillas simples \n salto de linea
cads = 'texto entre \n comillas simples '
#comillas dobles \t es una tabulacion
cadd = "texto entre \t comillas"
print (cadd)
print (cads)

#cadena larga respeta toda la estructura sin tener que poner \n o \t
cadc = """\n Texto linea 1
linea 2
linea 3
linea 4
.
.
.
linea N"""
print (cadc)

#repeticion y concatenacion
cad = "\n cadena" *3
cad2 = "\n cadena 2"
cadc = cad+cad2
print (cadc)
#BOOLEANO TRUE O FALSE
bT = True
bF = False
#Operadores Logicos
bAnd = True and False
bOr = True or False
bNot = not True
print (bAnd)
print (bOr)
print (bNot)