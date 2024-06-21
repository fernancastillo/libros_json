from fun_06_19_practica_ejercicio_json import *
os.system("cls")
while True:
    print("\tMENÚ:\n")
    print("1. Agregar un libro")
    print("2. Mostrar libros")
    print("3. Buscar libro por título")
    print("4. Actualizar información de un libro")
    print("5. Guardar libros en un archivo JSON")
    print("6. Salir")
    opc=opc_menu([1,2,3,4,5,6])
    if opc==1:
        opc_1()
    elif opc==2:
        opc_2()
    elif opc==3:
        opc_3()
    elif opc==4:
        opc_4()
    elif opc==5:
        opc_5()
    else:
        opc_6()
    print(">>Presione una tecla para continuar<<")
    msvcrt.getch()
    os.system("cls")