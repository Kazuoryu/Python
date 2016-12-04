#En caso de que solo llamemos 1 operador la funcion no daria
#error porque le hemos dicho en caso de que no se pueda 
def sumar (num1,num2=0):
    resultado = num1 + num2
    return resultado
valor = sumar(5)
print (valor)
