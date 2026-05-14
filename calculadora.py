def multiplicacion (a,b):
    return a*b
def division (a,b):
    if b==0:
        return "Error, division por 0"
    return a/b


num1= int(input("Ingrese el primer numero"))
num2= int(input("Ingrese el segundo numero"))
suma= num1 + num2
resta= num1 - num2
print ("La suma es:")
print (suma)
print("La resta es:")
print (resta)
