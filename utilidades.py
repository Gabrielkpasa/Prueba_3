import random
#importamos la biblioteca import para asignarle un precio random al producto
def menu():
    #definimos nuestra funcion, en este caso seria menu, en donde va a contener todo el codigo
    while True: #un while, es decir que se repita hasta que el usuario quiera
        print('''Menú de usuario:
        1. Registrar producto
        2. Listar todos los productos
        3. Buscar productos por categoría
        4. Calcular el precio promedio de los productos
        5. Salir del programa y guardar
        ''')#un menu amigable para el usuario
        opcion=int(input("Ingrese la opcion a seguir: "))
        #la opcion a ingresar del usuario
        if opcion==1: #el cuando elija la opcion 1 podra ingresar los productos
            producto=nombreProducto=input("Ingrese el nombre del producto: ")
            categoriaProducto=input("Ingrese la categoria del producto: ")
            cantidadProducto=input("Ingrese la cantidad del producto: ")
            precio=random.randint(10,1000)
            producto={ #el producto final se guarda en un diccionario
                "nombre": nombreProducto,
                "categoria": categoriaProducto,
                "cantidad": cantidadProducto,
                "precio": precio
            }
        elif opcion==2: #cuando el elija la opcion 2 se le listarán los productos ingresados
            for x in producto:
                print(f"producto: \n{nombreProducto}")
                print(f"Categoria: \n{categoriaProducto}")
                print(f"Cantidad: \n{cantidadProducto}")
                print(f"precio: \n{precio}")
        elif opcion==3: #cuando el elija la opcion 3 se le mostraran los productos por categoria, es decir, si el ingresa una categoria de carne se mostrarán
        #todos los productos que contengan carne
            categoriaBuscada=input("ingrese la categoria que desea buscar: ")
            for categoriaProducto in producto:
                print(f"Los productos en esta categoria son {nombreProducto}")

#lamentablemente me comio el tiempo y no pude seguir
