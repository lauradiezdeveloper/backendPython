operacion = input("Elige la operación que quieres realizar: sumar, restar, multiplicar, dividir o potencia")
numero1_str, numero2_str = input("Añade los dos números sobre los que quieres hacer la operación separados por una coma").split(",")

x = int(numero1_str)
y = int(numero2_str)

def Calculadora():
    if operacion == "sumar":
        print(x+y)
    elif operacion == "restar":
        print(x-y)
    elif operacion == "multiplicar":
        print(x*y)
    elif operacion == "dividir":
        print(x//y)
    elif operacion == "potencia":
        print(x**y)

Calculadora()