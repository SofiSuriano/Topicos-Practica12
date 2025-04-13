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


def eliminar_sucursal(conn, id_sucursal, page):
    cursor = conn.cursor()
    query = "DELETE FROM sucursales WHERE idSucursales = %s"
    cursor.execute(query, (id_sucursal,))
    conn.commit()
    cursor.close()
    mostrar_sucursales(conectar_db(), page)  


def mostrar_sucursales(conn, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sucursales")
    sucursales = cursor.fetchall()
    cursor.close()


    for item in page.controls:
        if isinstance(item, ft.Column) and item.key == "sucursales_mostradas":
            page.controls.remove(item)

    columna_resultado = ft.Column(key="sucursales_mostradas", spacing=10)


    for sucursal in sucursales:
        columna_resultado.controls.append(
            ft.Row([ 
                ft.Text(f"ID: {sucursal[0]} - Dirección: {sucursal[1]} - Teléfono: {sucursal[2]} - Correo: {sucursal[3]}"),
                ft.ElevatedButton(
                    "Eliminar", 
                    color="white", 
                    bgcolor="pink",
                    on_click=lambda e, id=sucursal[0]: eliminar_sucursal(conectar_db(), id, page)
                )
            ])
        )

    page.controls.append(columna_resultado)
    page.update()

def main(page: ft.Page):
    page.title = "Catálogo de Sucursales"
    page.bgcolor = "#F8F9FF"


    logo = ft.Row(
        controls=[ 
            ft.Image(
                src="fotos/image (3).png",  
                width=180,
                height=180,
                fit=ft.ImageFit.CONTAIN
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    lblDireccion = ft.Text("Dirección", color="deeppink", size=22)
    txtDireccion = ft.TextField(border_color="white", bgcolor="white")

    lblTelefono = ft.Text("Teléfono", color="deeppink", size=22)
    txtTelefono = ft.TextField(border_color="white", bgcolor="white")

    lblCorreo = ft.Text("Correo Electrónico", color="deeppink", size=22)
    txtCorreo = ft.TextField(border_color="white", bgcolor="white")

    btnAgregar = ft.ElevatedButton(
        "Agregar Sucursal",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: agregar_sucursal(conectar_db(), txtDireccion.value, txtTelefono.value, txtCorreo.value)
    )

    btnMostrar = ft.ElevatedButton(
        "Mostrar Sucursales",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: mostrar_sucursales(conectar_db(), page)
    )


    formulario = ft.Container(
        content=ft.Column(
            controls=[
                lblDireccion,
                txtDireccion,
                lblTelefono,
                txtTelefono,
                lblCorreo,
                txtCorreo,
                ft.Row([btnAgregar, btnMostrar], spacing=10)
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=30,
        bgcolor="#FFCDEA",  
        border_radius=12,
        width=600,
        key="formulario"
    )


    page.add(
        ft.Column(
            controls=[
                logo,
                formulario
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
        )
    )

ft.app(target=main)

