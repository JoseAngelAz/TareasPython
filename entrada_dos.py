nombre = input("Digita tu nombre:\n ")
edad = int(input("Digita tu edad: \n"))
promedio = float(input("Digita tu promedio:\n "))
respuesta = input("Eres del grupo 3 (SI/NO)\n") == "si"

print("Hola, tu nombre es:", nombre)
print("Tu edad es:", edad)
print("Tu promedio es:", promedio)
print("Bienvenid@", respuesta)