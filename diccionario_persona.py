# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "María Rodríguez",
    "edad": 28,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniera de Software"
}

# Modificar el valor de la ciudad
informacion_personal["ciudad"] = "Quito"

# Agregar o modificar la profesión
informacion_personal["profesion"] = "Desarrolladora Web"

# Verificar si existe la clave "telefono"
if "telefono" not in informacion_personal:
    # Agregar un número de teléfono si no existe
    informacion_personal["telefono"] = "0996987541"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)