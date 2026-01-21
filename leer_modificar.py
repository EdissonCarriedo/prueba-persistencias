# Mostrar el contenido del archivo con números de línea
archivo = "datos.txt"
print(f"----Contenido del archivo {archivo} ----")
with open(archivo, "r") as f:
    for num, linea in enumerate(f, start=1):
        print(f"{num}: {linea}", end="")

# Pedir la línea a modificar
linea_elegida = int(input("\nSelecciona el número de línea a modificar: "))

# Leer todas las líneas
with open(archivo, "r") as f:
    lineas = f.readlines()

# Verificar que la línea exista
if 1 <= linea_elegida <= len(lineas):
    nuevo_texto = input("Ingresa el nuevo texto: ")
    lineas[linea_elegida - 1] = nuevo_texto + "\n"

    # Guardar cambios
    with open(archivo, "w") as f:
        f.writelines(lineas)

    print(" Línea modificada correctamente")
else:
    print(" Linea no existe")
