#GENERADOR DE CONTRASEÑAS

import random
import string

# Funcion para generar la contraseña  y la longitud de a contraseña
def generate_password(longitud=12):
# Se define la cadena de caracteres que puede estar en la contraseña
    characters = string.ascii_letters + string.digits + string.punctuation
 # Se genera la contraseña con la longitud deseada utilizando random.choice para elegir caracteres aleatorios de la cadena anterior
    contrasena = ''.join(random.choice(characters)for _ in range(longitud))
# Se añade un numero aleatorio entre 1 y 3 para añadir caracteres especiales
    return contrasena

# Pedir al usuario la longitud de la contraseña
longitud_deseada=int(input("Indique los en numero de caracteres de la contrasena: "))

# Generar la contraseña y mostrarla al usuario  # 12 caracteres en este ejemplo
nueva_contrasena=generate_password(longitud_deseada)

# Mostrar la contraseña generada al usuario  # 12 caracteres en este ejemplo
print(f'Esta es tu contrasena --> {nueva_contrasena}')


   
