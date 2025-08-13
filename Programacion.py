# generador_contrasenas.py
import secrets
import string

def generar_contrasena(longitud=12):
    """Genera una contraseña segura garantizando al menos:
       1 mayúscula, 1 minúscula, 1 dígito y 1 símbolo."""
    mayus = string.ascii_uppercase
    minus = string.ascii_lowercase
    digitos = string.digits
    simbolos = "!@#$%&*-_?."
