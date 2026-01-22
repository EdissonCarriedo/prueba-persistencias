with open("prueba1.txt", "a") as file:
    archivo_creado= "prueba1.txt"
    file.write(" ")
    entrada = input("introduce un texto: ")
    file.write(entrada)
    print(f"archivo creado es {archivo_creado} con exito")
