nombre, edad_str, peso_str = input("Ingresa tu nombre, tu edad y tu peso con decimales, separado por coma").split(",")

edad = int(edad_str)
peso = float(peso_str)


print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Peso", peso, type(peso))