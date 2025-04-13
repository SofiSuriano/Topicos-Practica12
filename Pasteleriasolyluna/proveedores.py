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

def eliminar_proveedor(conn, id_proveedor, page):
    cursor = conn.cursor()
    query = "DELETE FROM proveedores WHERE idProveedores = %s"
    cursor.execute(query, (id_proveedor,))
    conn.commit()
    cursor.close()
    mostrar_proveedores(conectar_db(), page)  

def mostrar_proveedores(conn, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proveedores")
    proveedores = cursor.fetchall()
    cursor.close()
    
    for item in page.controls:
        if isinstance(item, ft.Column) and item.key == "proveedores_mostrados":
            page.controls.remove(item)

    columna_resultado = ft.Column(key="proveedores_mostrados", spacing=10)

    for proveedor in proveedores:
        columna_resultado.controls.append(
            ft.Row([
                ft.Text(f"ID: {proveedor[0]} - Nombre: {proveedor[1]} - Teléfono: {proveedor[2]} - Dirección: {proveedor[3]} - Correo: {proveedor[4]}"),
                ft.ElevatedButton(
                    "Eliminar", 
                    color="white", 
                    bgcolor="pink",
                    on_click=lambda e, id=proveedor[0]: eliminar_proveedor(conectar_db(), id, page)
                )
            ])
        )

    page.controls.append(columna_resultado)  
    page.update()

def main(page: ft.Page):
    page.title = "Catálogo de Proveedores"
    page.bgcolor = "#F8F9FF" 

    logo = ft.Row(
        controls=[ft.Image(src="fotos/image (3).png", width=180, height=180, fit=ft.ImageFit.CONTAIN)],
        alignment=ft.MainAxisAlignment.CENTER
    )


    lblNombre = ft.Text("Nombre", color="deeppink", size=22)
    txtNombre = ft.TextField(border_color="white", bgcolor="white")

    lblTelefono = ft.Text("Teléfono", color="deeppink", size=22)
    txtTelefono = ft.TextField(border_color="white", bgcolor="white")

    lblDireccion = ft.Text("Dirección", color="deeppink", size=22)
    txtDireccion = ft.TextField(border_color="white", bgcolor="white")

    lblCorreo = ft.Text("Correo Electrónico", color="deeppink", size=22)
    txtCorreo = ft.TextField(border_color="white", bgcolor="white")


    btnAgregar = ft.ElevatedButton(
        "Agregar Proveedor",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: agregar_proveedor(conectar_db(), txtNombre.value, txtTelefono.value, txtDireccion.value, txtCorreo.value)
    )
    
    btnMostrar = ft.ElevatedButton(
        "Mostrar Proveedores",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: mostrar_proveedores(conectar_db(), page)
    )

    formulario = ft.Container(
        content=ft.Column(
            controls=[
                lblNombre, txtNombre,
                lblTelefono, txtTelefono,
                lblDireccion, txtDireccion,
                lblCorreo, txtCorreo,
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
            controls=[logo, formulario],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
        )
    )

ft.app(target=main)
