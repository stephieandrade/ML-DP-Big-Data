import sqlite3


def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''
        CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)
        ''')
    except sqlite3.OperationalError:
        print("La tabla categorias se ha creado correctamente")
    else:
        print("La tabla categorias ya existe.")

    try:
        cursor.execute('''
        CREATE TABLE plato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL, 
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        ''')
    except sqlite3.OperationalError:
        print("La tabla platos se ha creado correctamente")
    else:
        print("La tabla platos ya existe.")

    conexion.close()


def agregar_categoria():
    categoria = input("Nombre de la nueva categoria: \n")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(categoria))
    conexion.commit()
    conexion.close()


def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria")
    for categoria in categorias:
        print("[{}] {}]".format(categoria[0], categoria[1]))
    categoria_usuario = int(input("> "))
    plato = input("Nombre del nuevo plato: \n")
    cursor.execute("INSERT INTO plato VALUES(null,'{}', '{}')".format(
        categoria_usuario, plato))

    conexion.commit()
    conexion.close()


def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria")
    for categoria in categorias:
        print("[{}, {}]".format(categoria[0], categoria[1]))
    plato_usuario = int(input("> "))
    platos = cursor.execute(
        "SELECT * FROM plato WHERE categoria_id = {}". format(plato_usuario)).fetchall()
    for plato in platos:
        print("\t{}".format(plato[2]))

    conexion.close()


# crea la bdd
crear_bd()

# menu
while True:
    print("Bienvenido al gestor del restaurante")
    opcion = input(
        "\n introduce una opcion:\n[1]Agregar una categoria \n[2]Agregar un plato \n[3]Mostrar menu \n[4]Salir del programa")
    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        break
    else:
        print("opcion incorrecta")
