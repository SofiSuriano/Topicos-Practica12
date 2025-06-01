import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def agregar_detalle(conn, id_producto, id_venta, cantidad, precio):
    cursor = conn.cursor()
    query = "INSERT INTO detalleventa (idProductos, idVentas, cantidad, precioUnitario) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id_producto, id_venta, cantidad, precio))
    conn.commit()
    cursor.close()

def eliminar_detalle(conn, id_detalle, page, contenedor_detalles):
    cursor = conn.cursor()
    query = "DELETE FROM detalleventa WHERE idDetalleVenta = %s"
    cursor.execute(query, (id_detalle,))
    conn.commit()
    cursor.close()
    mostrar_detalles(conectar_db(), contenedor_detalles, page)

def mostrar_detalles(conn, contenedor_detalles, page):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT dv.idDetalleVenta, p.nombre, v.idVentas, dv.cantidad, dv.precioUnitario
        FROM detalleventa dv
        JOIN productos p ON dv.idProductos = p.idProductos
        JOIN ventas v ON dv.idVentas = v.idVentas
    """)
    detalles = cursor.fetchall()
    cursor.close()

    contenedor_detalles.controls.clear()

    for d in detalles:
        contenedor_detalles.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID Detalle: {d[0]}", size=14, weight="bold"),
                    ft.Text(f"Producto: {d[1]}", size=16),
                    ft.Text(f"ID Venta: {d[2]}", size=16),
                    ft.Text(f"Cantidad: {d[3]}", size=16),
                    ft.Text(f"Precio Unitario: ${d[4]}", size=16),
                    ft.ElevatedButton("Eliminar", bgcolor="pink", color="white",
                        on_click=lambda e, id=d[0]: eliminar_detalle(conectar_db(), id, page, contenedor_detalles))
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )
    page.update()

def vista_detalleventa(page: ft.Page):
    page.clean()
    page.title = "Gestión de Detalle de Ventas"
    page.bgcolor = "#F8F9FF"
    page.scroll = ft.ScrollMode.AUTO

    contenedor_detalles = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT idProductos, nombre FROM productos")
    productos = cursor.fetchall()
    cursor.execute("SELECT idVentas FROM ventas")
    ventas = cursor.fetchall()
    cursor.close()
    conn.close()

    dropdown_productos = ft.Dropdown(label="Producto")
    for p in productos:
        dropdown_productos.options.append(ft.dropdown.Option(str(p[0]), p[1]))

    dropdown_ventas = ft.Dropdown(label="ID Venta")
    for v in ventas:
        dropdown_ventas.options.append(ft.dropdown.Option(str(v[0])))

    txtCantidad = ft.TextField(label="Cantidad", bgcolor="white")
    txtPrecio = ft.TextField(label="Precio Unitario", bgcolor="white")

    def on_agregar(e):
        if dropdown_productos.value and dropdown_ventas.value and txtCantidad.value and txtPrecio.value:
            try:
                int(txtCantidad.value)
                float(txtPrecio.value)
                agregar_detalle(
                    conectar_db(),
                    dropdown_productos.value,
                    dropdown_ventas.value,
                    txtCantidad.value,
                    txtPrecio.value
                )
                txtCantidad.value = txtPrecio.value = ""
                mostrar_detalles(conectar_db(), contenedor_detalles, page)
                page.snack_bar = ft.SnackBar(ft.Text("✅ Detalle de venta agregado correctamente."))
            except:
                page.snack_bar = ft.SnackBar(ft.Text("⚠️ Cantidad o precio inválido."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            dropdown_productos,
            dropdown_ventas,
            txtCantidad,
            txtPrecio,
            ft.ElevatedButton("Agregar Detalle de Venta", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Detalles", on_click=lambda e: mostrar_detalles(conectar_db(), contenedor_detalles, page), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de detalle de ventas", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_detalles,
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
