archivo= "prueba.txt"
print(f"---Contenido de {archivo}---")
with open("prueba.txt", "r") as file:
    contenido = file.read()
print(contenido)