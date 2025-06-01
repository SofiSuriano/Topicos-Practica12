import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def agregar_sucursal(conn, direccion, telefono, correo):
    cursor = conn.cursor()
    query = "INSERT INTO sucursales (direccion, telefono, correoElectronico) VALUES (%s, %s, %s)"
    cursor.execute(query, (direccion, telefono, correo))
    conn.commit()
    cursor.close()

def eliminar_sucursal(conn, id_sucursal, page, contenedor_sucursales):
    cursor = conn.cursor()
    query = "DELETE FROM sucursales WHERE idSucursales = %s"
    cursor.execute(query, (id_sucursal,))
    conn.commit()
    cursor.close()
    mostrar_sucursales(conectar_db(), contenedor_sucursales, page)

def mostrar_sucursales(conn, contenedor_sucursales, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sucursales")
    sucursales = cursor.fetchall()
    cursor.close()

    contenedor_sucursales.controls.clear()

    for s in sucursales:
        contenedor_sucursales.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {s[0]}", size=14, weight="bold"),
                    ft.Text(f"Dirección: {s[1]}", size=16),
                    ft.Text(f"Teléfono: {s[2]}", size=16),
                    ft.Text(f"Correo: {s[3]}", size=16),
                    ft.ElevatedButton("Eliminar", bgcolor="pink", color="white",
                        on_click=lambda e, id=s[0]: eliminar_sucursal(conectar_db(), id, page, contenedor_sucursales))
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )
    page.update()

def vista_sucursales(page: ft.Page):
    page.clean()
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = "Gestión de Sucursales"
    page.bgcolor = "#F8F9FF"

    contenedor_sucursales = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    txtDireccion = ft.TextField(label="Dirección", bgcolor="white")
    txtTelefono = ft.TextField(label="Teléfono", bgcolor="white")
    txtCorreo = ft.TextField(label="Correo Electrónico", bgcolor="white")

    def on_agregar(e):
        if txtDireccion.value and txtTelefono.value and txtCorreo.value:
            agregar_sucursal(conectar_db(), txtDireccion.value, txtTelefono.value, txtCorreo.value)
            txtDireccion.value = txtTelefono.value = txtCorreo.value = ""
            mostrar_sucursales(conectar_db(), contenedor_sucursales, page)
            page.snack_bar = ft.SnackBar(ft.Text("✅ Sucursal agregada correctamente."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            txtDireccion,
            txtTelefono,
            txtCorreo,
            ft.ElevatedButton("Agregar Sucursal", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Sucursales", on_click=lambda e: mostrar_sucursales(conectar_db(), contenedor_sucursales, page), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de sucursales", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_sucursales,
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
