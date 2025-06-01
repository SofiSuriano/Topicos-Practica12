import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def agregar_producto(conn, nombre, precio, codigo, stock):
    cursor = conn.cursor()
    query = "INSERT INTO productos (nombre, precio, codigoBarras, stock) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nombre, precio, codigo, stock))
    conn.commit()
    cursor.close()

def eliminar_producto(conn, id_producto, page, contenedor_productos):
    cursor = conn.cursor()
    query = "DELETE FROM productos WHERE idProductos = %s"
    cursor.execute(query, (id_producto,))
    conn.commit()
    cursor.close()
    mostrar_productos(conectar_db(), contenedor_productos, page)

def mostrar_productos(conn, contenedor_productos, page):
    cursor = conn.cursor()
    cursor.execute("SELECT idProductos, nombre, precio, codigoBarras, stock FROM productos")
    productos = cursor.fetchall()
    cursor.close()

    contenedor_productos.controls.clear()

    for p in productos:
        contenedor_productos.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {p[0]}", size=14, weight="bold"),
                    ft.Text(f"Nombre: {p[1]}", size=16),
                    ft.Text(f"Precio: ${p[2]}", size=16),
                    ft.Text(f"Código de Barras: {p[3]}", size=16),
                    ft.Text(f"Stock: {p[4]}", size=16),
                    ft.ElevatedButton("Eliminar", bgcolor="pink", color="white",
                        on_click=lambda e, id=p[0]: eliminar_producto(conectar_db(), id, page, contenedor_productos))
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )
    page.update()

def vista_productos(page: ft.Page):
    page.clean()
    page.title = "Gestión de Productos"
    page.bgcolor = "#F8F9FF"
    page.scroll = ft.ScrollMode.ALWAYS

    contenedor_productos = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    txtNombre = ft.TextField(label="Nombre del producto", bgcolor="white")
    txtPrecio = ft.TextField(label="Precio ($)", bgcolor="white")
    txtCodigo = ft.TextField(label="Código de barras", bgcolor="white")
    txtStock = ft.TextField(label="Stock", bgcolor="white")

    def on_agregar(e):
        if txtNombre.value and txtPrecio.value and txtCodigo.value and txtStock.value:
            try:
                float(txtPrecio.value)
                int(txtStock.value)
                agregar_producto(conectar_db(), txtNombre.value, txtPrecio.value, txtCodigo.value, txtStock.value)
                txtNombre.value = txtPrecio.value = txtCodigo.value = txtStock.value = ""
                mostrar_productos(conectar_db(), contenedor_productos, page)
                page.snack_bar = ft.SnackBar(ft.Text("✅ Producto agregado correctamente."))
            except:
                page.snack_bar = ft.SnackBar(ft.Text("⚠️ Precio o stock inválido."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            txtNombre,
            txtPrecio,
            txtCodigo,
            txtStock,
            ft.ElevatedButton("Agregar Producto", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Productos", on_click=lambda e: mostrar_productos(conectar_db(), contenedor_productos, page), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de productos", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_productos,
                bgcolor="#F0F4FF",
                border_radius=10,
                padding=10,
                alignment=ft.alignment.center,
                width=420
            )
        ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS
        ),
        alignment=ft.alignment.center,
        expand=True
    )

    return layout

