import random

minusculas = list("abcdefghijklmnopqrstuvwxyz")
mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numeros = list("0123456789")
especiales = list("!@#$%&*?")

caracteres = minusculas + mayusculas + numeros + especiales

print("=== GENERADOR DE CONTRASEÑAS ===")

while True:
    try:
        longitud = int(input("Introduce la longitud de la contraseña: "))
        if longitud >= 3:
            break
        print("La longitud mínima es 3, para poder incluir mayúscula, minúscula y número.\n")
    except ValueError:
        print("Debes introducir un número entero.\n")

# Una de cada tipo obligatorio
contrasena = [
    random.choice(minusculas),
    random.choice(mayusculas),
    random.choice(numeros)
]

# El resto, de cualquier tipo
for i in range(longitud - 3):
    contrasena.append(random.choice(caracteres))

# Mezclar para que las obligatorias no queden siempre al principio
random.shuffle(contrasena)

print("Contraseña generada:", "".join(contrasena))
