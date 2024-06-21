import json, time, msvcrt, os
libros=[]
def opc_menu (lista_numeros):
    while True:
        try:
            opc=int(input("Ingrese un número del menú: "))
            if opc in lista_numeros:
                os.system("cls")
                return opc
            print("Error! Debe ingresar un número del menú!")
        except:
            print("Error! Debe ingresar un número entero!")

def opc_1 ():
    print("\tAGREGAR UN LIBRO:\n")
    titulo=validacion_titulo()
    autor=validacion_autor()
    year=validacion_year()
    genero=validacion_genero()
    libro={
        "titulo":titulo,
        "autor":autor,
        "anhio":year,
        "genero":genero
    }
    libros.append(libro)
    print("Libro agregado con éxito!")

def opc_2 ():
    if validacion_cantidad():
        print("\tLISTA DE LIBROS:\n")
        for l in libros:
            print(f"Título: {l['titulo']}")
            print(f"Autor: {l['autor']}")
            print(f"Año: {l['anhio']}")
            print(f"Género literario: {l['genero']}\n\n")

def opc_3 ():
    if validacion_cantidad():
        print("\tBUSCAR LIBRO POR TÍTULO")
        titulo=input("Ingrese el titulo del libro que busca: ")
        for l in libros:
            if l["titulo"]==titulo:
                break
        if l["titulo"]==titulo:
            print("\tLIBRO ENCONTRADO:\n")
            print(f"Título: {l['titulo']}")
            print(f"Autor: {l['autor']}")
            print(f"Año: {l['anhio']}")
            print(f"Género literario: {l['genero']}\n")
        else:
            print("No se ha encontrado el libro indicado.")

def opc_4():
    if validacion_cantidad():
        print("\tACTUALIZAR INFORMACIÓN DE UN LIBRO:\n")
        titulo=input("Ingrese el titulo del libro que desea actualizar: ")
        for l in libros:
            if l["titulo"]==titulo:
                break
        if l["titulo"]==titulo:
            titulo=validacion_actualizar_titulo()
            if titulo!=None:
                l["titulo"]=titulo
                print("Título cambiado con éxito!")
            autor=validacion_actualizar_autor()
            if autor !=None:
                l["autor"]=autor
                print("Autor cambiado con éxito!")
            year=validacion_actualizar_year()
            if year!=None:
                l["anhio"]=year
                print("Año de publicación cambiado con éxito!")
 
            genero=validacion_actualizar_genero()
            if genero!=None:
                l["genero"]=genero
                print("Género literario cambiado con éxito!")
        else:
            print("No se ha encontrado el libro ingresado.")

def opc_5():
    print("\tGUARDAR LIBROS EN ARCHIVO JSON\n")
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    with open (f"{nombre_archivo}.json","w",newline="") as archivo:
        for l in libros:
            json.dump(l,archivo)
    print("Archivo creado con éxito!")

def opc_6 ():
    print("Hasta la próxima!")
    exit()

def validacion_titulo():
    while True:
        texto=input("Ingrese el título: ")
        if len(texto)>=3:
            return texto
        else:
            print("Error! Debe ingresar mínimo 3 caracteres!")
            time.sleep(2)

def validacion_actualizar_titulo():
    while True:
        texto=input("Ingrese el nuevo título (presione enter para omitir la actualización de este item): ")
        if texto=="":
            print("No se ha actualizado el título.")
            time.sleep(2)
            break
        elif len(texto)>=3:
            return texto
        else:
            print("Error! Debe ingresar mínimo 3 caracteres!")
            time.sleep(2)

def validacion_actualizar_autor():
    while True:
        autor=input("Ingrese el nuevo autor (presione enter para omitir la actualización de este item): ")
        if autor=="":
            print("No se ha actualizado el autor.")
            time.sleep(2)
            break
        elif len(autor)>=2:
            return autor
        else:
            print("Error! Debe ingresar mínimo 2 caracteres!")
            time.sleep(2)            

def validacion_actualizar_year():
    while True:
        try:
            year=input("Ingrese el nuevo año de publicación (presione enter para omitir la actualización de este item): ")
            if year=="":
                print("No se ha actualizado el año de publicación.")
                time.sleep(2)
                break
            elif year<1:
                print("Error! Debe ingresar un año mayor a 0!")
                time.sleep(2)
            else:
                return year
        except:
            print("Error! Debe ingresar un número entero!")
            time.sleep(2)

def validacion_actualizar_genero():
    while True:
        genero=input("Ingrese el nuevo género literario (presione enter para omitir la actualización de este item): ")
        if genero=="":
            print("No se ha actualizado el género literario.")
            time.sleep(2)
            break
        elif len(genero)>=3:
            return genero
        else:
            print("Error! Debe ingresar mínimo 3 caracteres!")
            time.sleep(2)            

def validacion_autor():
    while True:
        autor=input("Ingrese al autor: ")
        if len(autor)>=3:
            return autor
        else:
            print("Error! Debe ingresar mínimo 2 caracteres!")
            time.sleep(2)

def validacion_year():
    while True:
        try:
            year=int(input("Ingrese el año de publicación: "))
            if year<=0:
                print("Error! Debe ingresar un número mayor a 0!")
                time.sleep(2)
            else:
                return year
        except:
            print("Error! Debe ingresar un número entero!")
            time.sleep(2)

def validacion_genero():
    while True:
        genero=input("Ingrese el género literario: ")
        if len(genero)>=3:
            return genero
        else:
            print("Error! Debe escribir más de 3 caracteres!")
            
def validacion_cantidad():
    if len(libros)==0:
        print("No hay libros agregados! Presione 1 en el menú para empezar a agregar.")
        return False
    return True

def validacion_titulo_lista():
    titulo=validacion_titulo()
    for l in libros:
        if l["titulo"]==titulo:
            break
    if l["titulo"]==titulo:
        return True
    else:
        print("No se ha encontrado el libro ingresado")
        return False
    

