# Generador de Contraseñas Seguras (Python)

**Fecha:** 19 de agosto de 2025

## Objetivo del programa
Crear un programa sencillo en Python que solicite **dos datos al usuario (nombre y apellido)** y, a continuación, **genere una contraseña segura** aleatoria que cumpla criterios mínimos de robustez (mayúsculas, minúsculas, dígitos y símbolos).


## Principales funcionalidades del código

1. **Entrada de datos**
   - El programa solicita **Nombre** y **Apellido** mediante `input()` y limpia espacios con `.strip()`.
   - Estos datos **no** se usan dentro de la contraseña . Solo se muestran en un saludo.

2. **Generación de contraseña segura**
   - Uso del módulo estándar **`secrets`** para aleatoriedad **criptográficamente segura** (preferible a `random` para contraseñas).
   - Uso de **`string`** para obtener conjuntos de caracteres: letras mayúsculas, minúsculas y dígitos.
   - Se garantiza como mínimo: **1 mayúscula + 1 minúscula + 1 dígito + 1 símbolo**.
   - Longitud configurable (por defecto **12** caracteres).

3. **Mezcla final sin patrones**
   - Se aplica un **barajado tipo Fisher–Yates** usando `secrets.randbelow(...)` para evitar que los primeros cuatro caracteres sean siempre de tipos fijos (mayúscula, minúscula, dígito, símbolo).
