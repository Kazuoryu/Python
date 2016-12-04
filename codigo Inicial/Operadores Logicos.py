edad = 17
# ifcondicion es muy importante los espacios un espacio de mas da errores
if edad > 18 and edad < 20:
    print ("Edad es 19")
else:
    print ("edad no es 19")

if edad > 18 or edad < 20:
    print ("es 18 o 20 ")
else:
    print ("no es 18 ni 20")

if edad > 18 and edad < 20 or edad==100:
    print ("es 18, 20 o 100")
else:
    print ("no es 18,20 ni 100")
if not edad > 18: #niega la condicion gracias al NOT
    print ("si es menor")
else:
    print ("no es menor")
