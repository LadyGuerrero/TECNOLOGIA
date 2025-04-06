# Programa simplificado para operaciones con archivos de texto en Python

# 1. Escritura de Archivo de Texto
print("Escribiendo archivo de texto...")
archivo = open("my_notes.txt", "w")
# Usamos write() para escribir las tres líneas
archivo.write("Nota 1: Recordar comprar ingredientes para la cena.\n")
archivo.write("Nota 2: Llamar al médico para agendar cita.\n")
archivo.write("Nota 3: Entregar el informe final del proyecto.\n")
archivo.close()  # Cerramos el archivo después de escribir
print("Archivo escrito correctamente")

# 2. Lectura de Archivo de Texto
print("\nLeyendo archivo de texto...")
archivo = open("my_notes.txt", "r")
print("Contenido del archivo:")
# Usamos readline() para leer línea por línea
linea = archivo.readline()
while linea:
    print(linea, end="")
    linea = archivo.readline()  # Leemos la siguiente línea
archivo.close()  # Cerramos el archivo después de leer
print("\nArchivo cerrado")