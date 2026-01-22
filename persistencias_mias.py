# para leer archivo .txt
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as f:
         return f.read())

# para escribir .txt

def escribir_archivo(nombre_archivo, texto):
    with open(nombre_archivo, "w",) as f:
        f.write(texto)

# para actualizar un .txt

def actualizar_archivo(nombre_archivo, texto):
    with open(nombre_archivo, "a", encoding="utf-8") as f:
        f.write("\n" + texto)

# para borrar un .txt el contenido

def borrar_contenido(nombre_archivo):
    with open(nombre_archivo, "w") as f:
        pass

# eliminar un archivo .txt 

import os

def eliminar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
        print("Archivo eliminado")
    else:
        print("El archivo no existe")
