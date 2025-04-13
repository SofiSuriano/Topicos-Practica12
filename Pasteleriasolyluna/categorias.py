import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def agregar_categoria(conn, nombre, descripcion):
    cursor = conn.cursor()
    query = "INSERT INTO categorias (nombre, descripcion) VALUES (%s, %s)"
    cursor.execute(query, (nombre, descripcion))
    conn.commit()
    cursor.close()

def eliminar_categoria(conn, id_categoria, page):
    cursor = conn.cursor()
    query = "DELETE FROM categorias WHERE idCategorias = %s"
    cursor.execute(query, (id_categoria,))
    conn.commit()
    cursor.close()
    mostrar_categorias(conectar_db(), page)  


def mostrar_categorias(conn, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    cursor.close()


    for item in page.controls:
        if isinstance(item, ft.Column) and item.key == "categorias_mostradas":
            page.controls.remove(item)

    columna_resultado = ft.Column(key="categorias_mostradas", spacing=10)

    for categoria in categorias:
        columna_resultado.controls.append(
            ft.Row([
                ft.Text(f"ID: {categoria[0]} - Nombre: {categoria[1]} - Descripción: {categoria[2]}"),
                ft.ElevatedButton(
                    "Eliminar", 
                    color="white", 
                    bgcolor="pink",
                    on_click=lambda e, id=categoria[0]: eliminar_categoria(conectar_db(), id, page)
                )
            ])
        )

    page.controls.append(columna_resultado)
    page.update()

def main(page: ft.Page):
    page.title = "Catálogo de Categorías"
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

    lblNombre = ft.Text("Nombre", color="deeppink", size=22)
    txtNombre = ft.TextField(border_color="white", bgcolor="white")

    lblDescripcion = ft.Text("Descripción", color="deeppink", size=22)
    txtDescripcion = ft.TextField(border_color="white", bgcolor="white")


    btnAgregar = ft.ElevatedButton(
        "Agregar Categoría",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: agregar_categoria(conectar_db(), txtNombre.value, txtDescripcion.value)
    )


    btnMostrar = ft.ElevatedButton(
        "Mostrar Categorías",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: mostrar_categorias(conectar_db(), page)
    )


    formulario = ft.Container(
        content=ft.Column(
            controls=[
                lblNombre,
                txtNombre,
                lblDescripcion,
                txtDescripcion,
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
