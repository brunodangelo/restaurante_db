import sqlite3

def crear_bd():
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL)")
    except sqlite3.OperationalError:
        print("La Tabla 'categoria' ya existe")
    else:
        print("La tabla 'categoria' se creó con éxito")
    try:
        cursor.execute("CREATE TABLE plato(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL,FOREIGN KEY(categoria_id) REFERENCES categoria(id))")
    except sqlite3.OperationalError:
        print("La Tabla 'plato'  ya existe")
    else:
        print("La tabla 'plato' se creó con éxito")
    conexion.commit()
    conexion.close()

def agregar_categoria():
    categoria=input("Nombre de la categoria a agregar: ")
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(categoria))
    except sqlite3.OperationalError:
        print("La categoria ya existe")
    else:
        print("La categoria se agregó corrextamente")
    conexion.commit()
    conexion.close()

def agregar_plato():
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    categorias=cursor.execute("SELECT * FROM categoria").fetchall()
    print("Escoja una categoria: ")
    for categoria in categorias:
        print("{}- {}".format(categoria[0],categoria[1]))
    opcion=int(input("Opcion: ")) #es el id de la categoria
    plato=input("Nombre del plato: ")
    try:
        cursor.execute("INSERT INTO plato VALUES(null,'{}',{})".format(plato,opcion))
    except sqlite3.IntegrityError:
        print("El plato ya existe")
    else:
        print("El plato se agrego con exito")
    conexion.commit()
    conexion.close()

def mostrar_menu():
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    categorias=cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos=cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("-{}".format(plato[1]))
    conexion.close()

while(True):
    print("1- Crea Base de Datos \n2- Agregar Categoría \n3- Agregar Plato \n4- Mostrar Menú \n5- Salir")
    try:
        opcion=int(input("Opción: "))
        if (1<=opcion<=5):
            print("-----------------------------------")
            if opcion==1:
                crear_bd()
            elif opcion==2:
                agregar_categoria()
            elif opcion==3:
                agregar_plato()
            elif opcion==4:
                mostrar_menu()
            elif opcion==5:
                break
            print("-----------------------------------")
        else:
            print("Introducí una opcion entre 1 y 5")
    except:
        print("Debe introducir un número entre 1 y 5")
