import random
print("¡Hola mundo!")

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_Lenght = int(input("Ingrese la longitud de la contraseña: "))
password = ""
for i in range(password_Lenght):
    password += random.choice(caracteres)
print(password)
