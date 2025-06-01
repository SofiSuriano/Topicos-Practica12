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

def eliminar_categoria(conn, id_categoria, page, contenedor_categorias):
    cursor = conn.cursor()
    query = "DELETE FROM categorias WHERE idCategorias = %s"
    cursor.execute(query, (id_categoria,))
    conn.commit()
    cursor.close()
    mostrar_categorias(conectar_db(), contenedor_categorias, page)

def mostrar_categorias(conn, contenedor_categorias, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    cursor.close()

    contenedor_categorias.controls.clear()

    for categoria in categorias:
        contenedor_categorias.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {categoria[0]}", size=14, weight="bold"),
                    ft.Text(f"Nombre: {categoria[1]}", size=16),
                    ft.Text(f"Descripción: {categoria[2]}", size=16),
                    ft.ElevatedButton(
                        "Eliminar", 
                        bgcolor="pink", 
                        color="white",
                        on_click=lambda e, id=categoria[0]: eliminar_categoria(conectar_db(), id, page, contenedor_categorias)
                    )
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )
    page.update()


def vista_categorias(page: ft.Page):
    page.clean()
    page.title = "Gestión de Categorías"
    page.bgcolor = "#F8F9FF"
    page.scroll = ft.ScrollMode.AUTO

    contenedor_categorias = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    txtNombre = ft.TextField(label="Nombre", bgcolor="white")
    txtDescripcion = ft.TextField(label="Descripción", bgcolor="white")

    def on_agregar(e):
        if txtNombre.value and txtDescripcion.value:
            agregar_categoria(conectar_db(), txtNombre.value, txtDescripcion.value)
            txtNombre.value = txtDescripcion.value = ""
            mostrar_categorias(conectar_db(), contenedor_categorias, page)
            page.snack_bar = ft.SnackBar(ft.Text("✅ Categoría agregada correctamente."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            txtNombre,
            txtDescripcion,
            ft.ElevatedButton("Agregar Categoría", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Categorías", on_click=lambda e: mostrar_categorias(conectar_db(), contenedor_categorias, page), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de categorías", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_categorias,
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
