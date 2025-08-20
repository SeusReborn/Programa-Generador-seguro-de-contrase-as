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
    
    # Aqui selecciono almenos uno de cada tipo
    base = [
        secrets.choice(mayus),
        secrets.choice(minus),
        secrets.choice(digitos),
        secrets.choice(simbolos),
    ]
    # Completo la longitud que deseo
    universo = mayus + minus + digitos + simbolos
    while len(base) < longitud:
        base.append(secrets.choice(universo))
    
    # Mezclo Aleatoriamente
    secrets.SystemRandom().shuffle(base)
    return "".join(base)

def main():
    nombre = input("¿Cuál es tu nombre? ").strip()
    apellido = input("¿Cuál es tu apellido? ").strip()
    
    # Por seguridad, NO uso el nombre ni apellido del usuario
    contrasena = generar_contrasena(12)
    print(f"\nListo, {nombre} {apellido}. Tu contraseña segura es:\n{contrasena}")

if __name__ == "__main__":
    main()
