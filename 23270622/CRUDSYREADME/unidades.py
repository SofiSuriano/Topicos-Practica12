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

def eliminar_unidad(conn, id_unidad, page, contenedor_unidades):
    cursor = conn.cursor()
    query = "DELETE FROM unidades WHERE idUnidades = %s"
    cursor.execute(query, (id_unidad,))
    conn.commit()
    cursor.close()
    mostrar_unidades(conectar_db(), contenedor_unidades, page)

def mostrar_unidades(conn, contenedor_unidades, page):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM unidades")
    unidades = cursor.fetchall()
    cursor.close()

    contenedor_unidades.controls.clear()

    for u in unidades:
        contenedor_unidades.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {u[0]}", size=14, weight="bold"),
                    ft.Text(f"Unidad: {u[1]}", size=16),
                    ft.ElevatedButton("Eliminar", bgcolor="pink", color="white",
                        on_click=lambda e, id=u[0]: eliminar_unidad(conectar_db(), id, page, contenedor_unidades))
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )
    page.update()

def vista_unidades(page: ft.Page):
    page.clean()
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = "Gestión de Unidades"
    page.bgcolor = "#F8F9FF"

    contenedor_unidades = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    txtUnidad = ft.TextField(label="Nombre de la unidad", bgcolor="white")

    def on_agregar(e):
        if txtUnidad.value.strip():
            agregar_unidad(conectar_db(), txtUnidad.value)
            txtUnidad.value = ""
            mostrar_unidades(conectar_db(), contenedor_unidades, page)
            page.snack_bar = ft.SnackBar(ft.Text("✅ Unidad agregada correctamente."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Ingresa el nombre de la unidad."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            txtUnidad,
            ft.ElevatedButton("Agregar Unidad", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Unidades", on_click=lambda e: mostrar_unidades(conectar_db(), contenedor_unidades, page), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de unidades", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_unidades,
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
