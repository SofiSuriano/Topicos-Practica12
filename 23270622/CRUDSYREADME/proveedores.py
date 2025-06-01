import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def agregar_proveedor(conn, nombre, telefono, direccion, correo):
    cursor = conn.cursor()
    query = "INSERT INTO proveedores (nombre, telefono, direccion, correoElectronico) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nombre, telefono, direccion, correo))
    conn.commit()
    cursor.close()

def eliminar_proveedor(conn, id_proveedor, page, contenedor_proveedores):
    cursor = conn.cursor()
    query = "DELETE FROM proveedores WHERE idProveedores = %s"
    cursor.execute(query, (id_proveedor,))
    conn.commit()
    cursor.close()
    mostrar_proveedores(conectar_db(), contenedor_proveedores, page)

def mostrar_proveedores(conn, contenedor_proveedores, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proveedores")
    proveedores = cursor.fetchall()
    cursor.close()

    contenedor_proveedores.controls.clear()

    for p in proveedores:
        contenedor_proveedores.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {p[0]}", size=14, weight="bold"),
                    ft.Text(f"Nombre: {p[1]}", size=16),
                    ft.Text(f"Teléfono: {p[2]}", size=16),
                    ft.Text(f"Dirección: {p[3]}", size=16),
                    ft.Text(f"Correo: {p[4]}", size=16),
                    ft.ElevatedButton("Eliminar", bgcolor="pink", color="white",
                        on_click=lambda e, id=p[0]: eliminar_proveedor(conectar_db(), id, page, contenedor_proveedores))
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )
    page.update()

def vista_proveedores(page: ft.Page):
    page.clean()
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = "Gestión de Proveedores"
    page.bgcolor = "#F8F9FF"

    contenedor_proveedores = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    txtNombre = ft.TextField(label="Nombre", bgcolor="white")
    txtTelefono = ft.TextField(label="Teléfono", bgcolor="white")
    txtDireccion = ft.TextField(label="Dirección", bgcolor="white")
    txtCorreo = ft.TextField(label="Correo Electrónico", bgcolor="white")

    def on_agregar(e):
        if txtNombre.value and txtTelefono.value and txtDireccion.value and txtCorreo.value:
            agregar_proveedor(conectar_db(), txtNombre.value, txtTelefono.value, txtDireccion.value, txtCorreo.value)
            txtNombre.value = txtTelefono.value = txtDireccion.value = txtCorreo.value = ""
            mostrar_proveedores(conectar_db(), contenedor_proveedores, page)
            page.snack_bar = ft.SnackBar(ft.Text("✅ Proveedor agregado correctamente."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            txtNombre,
            txtTelefono,
            txtDireccion,
            txtCorreo,
            ft.ElevatedButton("Agregar Proveedor", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Proveedores", on_click=lambda e: mostrar_proveedores(conectar_db(), contenedor_proveedores, page), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de proveedores", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_proveedores,
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
