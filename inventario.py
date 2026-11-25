
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    except mysql.connector.Error as error:
        print("Error de conexión:", error)
        return None


def listar_productos():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT p.id_producto, p.nombre, c.nombre,
                   p.precio, p.stock
            FROM productos p
            LEFT JOIN categorias c
            ON p.id_categoria = c.id_categoria
        """)
        print("\n--- LISTA DE PRODUCTOS ---")
        for fila in cursor.fetchall():
            print(fila)
        cursor.close()
        conexion.close()


def buscar_producto():
    nombre = input("Nombre del producto: ")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM productos WHERE nombre LIKE %s",
            (f"%{nombre}%",)
        )
        for producto in cursor.fetchall():
            print(producto)
        cursor.close()
        conexion.close()


def registrar_producto():
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    categoria = int(input("ID de categoría: "))

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO productos
            (nombre, descripcion, precio, stock, id_categoria)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, descripcion, precio, stock, categoria))
        conexion.commit()
        print("Producto registrado correctamente.")
        cursor.close()
        conexion.close()


def actualizar_stock():
    producto = int(input("ID del producto: "))
    stock = int(input("Nuevo stock: "))

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET stock = %s WHERE id_producto = %s",
            (stock, producto)
        )
        conexion.commit()
        print("Stock actualizado.")
        cursor.close()
        conexion.close()


def productos_stock_bajo():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT nombre, stock FROM productos WHERE stock < 10"
        )
        print("\n--- PRODUCTOS CON STOCK BAJO ---")
        for producto in cursor.fetchall():
            print(producto)
        cursor.close()
        conexion.close()


def modificar_precio():
    producto = int(input("ID del producto: "))
    precio = float(input("Nuevo precio: "))

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET precio = %s WHERE id_producto = %s",
            (precio, producto)
        )
        conexion.commit()
        print("Precio actualizado.")
        cursor.close()
        conexion.close()


def menu():
    while True:
        print("\n================================")
        print("       SISTEMA DE INVENTARIO")
        print("================================")
        print("1. Listar productos")
        print("2. Buscar producto")
        print("3. Registrar producto")
        print("4. Actualizar stock")
        print("5. Productos con stock bajo")
        print("6. Modificar precio")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            registrar_producto()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            productos_stock_bajo()
        elif opcion == "6":
            modificar_precio()
        elif opcion == "7":
            print("¡Gracias por utilizar el sistema!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
