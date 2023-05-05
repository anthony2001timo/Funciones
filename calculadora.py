#Documentacion en funcion de calculadora:

def sumar(op1,op2):
    """Esta funcion lo que realiza es una suma"""
    print("El resultado de la suma es: ",op1+op2)

def restar(op1,op2):
    """Esta funcion lo que realiza es una resta"""
    print(f"El resultado de la resta es: {op1-op2}")

def multiplicar(op1,op2):
    """Esta funcion realiza la multiplicacion de dos numeros"""
    print(f"El resultado de la multiplicacion es: {op1*op2}")

def dividir(op1,op2):
    """Esta funcion realiza una division"""
    print("El resultado de la division es: ",op1/op2)

help(sumar)
help(restar)
help(multiplicar)
help(dividir)
