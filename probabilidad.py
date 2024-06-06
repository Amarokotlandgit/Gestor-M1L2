import random

variable= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contraseña=int(input("de que cantidad de letras quiere la contraseña"))

password=""

for i in range(contraseña):
    password += random.choice(variable)

print(password)