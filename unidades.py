import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )


def agregar_unidad(conn, nombreUnidad):
    cursor = conn.cursor()
    query = "INSERT INTO unidades (nombreUnidad) VALUES (%s)"
    cursor.execute(query, (nombreUnidad,))
    conn.commit()
    cursor.close()


def eliminar_unidad(conn, id_unidad, page):
    cursor = conn.cursor()
    query = "DELETE FROM unidades WHERE idUnidades = %s"
    cursor.execute(query, (id_unidad,))
    conn.commit()
    cursor.close()
    mostrar_unidades(conectar_db(), page)  


def mostrar_unidades(conn, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM unidades")
    unidades = cursor.fetchall()
    cursor.close()


    for item in page.controls:
        if isinstance(item, ft.Column) and item.key == "unidades_mostradas":
            page.controls.remove(item)

    columna_resultado = ft.Column(key="unidades_mostradas", spacing=10)


    for unidad in unidades:
        columna_resultado.controls.append(
            ft.Row([ 
                ft.Text(f"ID: {unidad[0]} - Nombre: {unidad[1]}"),
                ft.ElevatedButton(
                    "Eliminar", 
                    color="white", 
                    bgcolor="pink",
                    on_click=lambda e, id=unidad[0]: eliminar_unidad(conectar_db(), id, page)
                )
            ])
        )


    page.controls.append(columna_resultado)
    page.update()

def main(page: ft.Page):
    page.title = "Catálogo de Unidades"
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

    lblUnidad = ft.Text("Unidad", color="deeppink", size=22)
    txtUnidad = ft.TextField(border_color="white", bgcolor="white")


    btnAgregar = ft.ElevatedButton(
        "Agregar Unidad",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: agregar_unidad(conectar_db(), txtUnidad.value)
    )


    btnMostrar = ft.ElevatedButton(
        "Mostrar Unidades",
        color="black",
        bgcolor="deeppink",
        on_click=lambda e: mostrar_unidades(conectar_db(), page)
    )


    formulario = ft.Container(
        content=ft.Column(
            controls=[
                lblUnidad,
                txtUnidad,
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
