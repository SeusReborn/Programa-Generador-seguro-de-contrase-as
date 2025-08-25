# generador_contrasenas.py
import secrets
import string

def generar_contrasena(longitud=12):
    """Genero una contraseña segura con:
       1 mayúscula, 1 minúscula, 1 dígito y 1 símbolo."""
    mayus = string.ascii_uppercase
    minus = string.ascii_lowercase
    digitos = string.digits
    simbolos = "!@#$%&*-_?."
    
    # Aseguro al menos uno de cada tipo
    base = [
        secrets.choice(mayus),
        secrets.choice(minus),
        secrets.choice(digitos),
        secrets.choice(simbolos),
    ]
    # Completo hasta la longitud deseada
    universo = mayus + minus + digitos + simbolos
    while len(base) < longitud:
        base.append(secrets.choice(universo))
    
    # Mezcla segura
    secrets.SystemRandom().shuffle(base)
    return "".join(base)

def pedir_dato(texto):
    """Pide un dato y valida que contenga solo letras."""
    while True:
        valor = input(texto).strip()
        if valor.isalpha():
            return valor
        else:
            print("Solo se permiten letras, intenta de nuevo.")

def main():
    nombre = pedir_dato("¿Cuál es tu nombre? ")
    apellido = pedir_dato("¿Cuál es tu apellido? ")
    
    contrasena = generar_contrasena(12)
    print(f"\nListo, {nombre} {apellido}. Tu contraseña segura es:\n{contrasena}")

if __name__ == "__main__":
    main()
