import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def agregar_cliente(conn, nombre, telefono, correo):
    cursor = conn.cursor()
    query = "INSERT INTO clientes (nombre, telefono, correo) VALUES (%s, %s, %s)"
    cursor.execute(query, (nombre, telefono, correo))
    conn.commit()
    cursor.close()

def eliminar_cliente(conn, id_cliente, page):
    cursor = conn.cursor()
    query = "DELETE FROM clientes WHERE idClientes = %s"
    cursor.execute(query, (id_cliente,))
    conn.commit()
    cursor.close()
    mostrar_clientes(conectar_db(), page) 

def mostrar_clientes(conn, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    

    for item in page.controls:
        if isinstance(item, ft.Column) and item.key == "clientes_mostrados":
            page.controls.remove(item)

    columna_resultado = ft.Column(spacing=10, key="clientes_mostrados")

    for cliente in clientes:
        columna_resultado.controls.append(
            ft.Row([
                ft.Text(f"ID: {cliente[0]} - Nombre: {cliente[1]} - Teléfono: {cliente[2]} - Correo: {cliente[3]}"),
                ft.ElevatedButton(
                    "Eliminar", 
                    color="white", 
                    bgcolor="pink",
                    on_click=lambda e, id=cliente[0]: eliminar_cliente(conectar_db(), id, page)
                )
            ])
        )

    page.controls.append(columna_resultado)  
    page.update()

def main(page: ft.Page):
    page.title = "Catálogo de Clientes"
    page.bgcolor = "#F8F9FF"  

    logo = ft.Row(
        controls=[ft.Image(src="fotos/image (3).png", width=180, height=180, fit=ft.ImageFit.CONTAIN)],
        alignment=ft.MainAxisAlignment.CENTER
    )


    lblNombre = ft.Text("Nombre", color="deeppink", size=22)
    txtNombre = ft.TextField(border_color="white", bgcolor="white")

    lblTelefono = ft.Text("Teléfono", color="deeppink", size=22)
    txtTelefono = ft.TextField(border_color="white", bgcolor="white")

    lblCorreo = ft.Text("Correo Electrónico", color="deeppink", size=22)
    txtCorreo = ft.TextField(border_color="white", bgcolor="white")


    btnAgregar = ft.ElevatedButton(
        "Agregar Cliente",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: agregar_cliente(conectar_db(), txtNombre.value, txtTelefono.value, txtCorreo.value)
    )
    
    btnMostrar = ft.ElevatedButton(
        "Mostrar Clientes",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: mostrar_clientes(conectar_db(), page)
    )


    formulario = ft.Container(
        content=ft.Column(
            controls=[
                lblNombre, txtNombre,
                lblTelefono, txtTelefono,
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
