# Repositorio
# https://github.com/SofiSuriano/Topicos-Practica12

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

def eliminar_cliente(conn, id_cliente, page, contenedor_clientes):
    cursor = conn.cursor()
    query = "DELETE FROM clientes WHERE idClientes = %s"
    cursor.execute(query, (id_cliente,))
    conn.commit()
    cursor.close()
    mostrar_clientes(conectar_db(), page, contenedor_clientes)

def mostrar_clientes(conn, page, contenedor_clientes):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()

    contenedor_clientes.controls.clear()

    for cliente in clientes:
        contenedor_clientes.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {cliente[0]}", size=14, weight="bold"),
                    ft.Text(f"Nombre: {cliente[1]}", size=16),
                    ft.Text(f"Teléfono: {cliente[2]}", size=16),
                    ft.Text(f"Correo: {cliente[3]}", size=16),
                    ft.ElevatedButton("Eliminar", bgcolor="pink", color="white",
                        on_click=lambda e, id=cliente[0]: eliminar_cliente(conectar_db(), id, page, contenedor_clientes))
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )
    page.update()


def vista_clientes(page: ft.Page):
    page.clean()
    page.title = "Gestión de Clientes"
    page.bgcolor = "#F8F9FF"
    page.scroll = ft.ScrollMode.AUTO

    contenedor_clientes = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    txtNombre = ft.TextField(label="Nombre", bgcolor="white")
    txtTelefono = ft.TextField(label="Teléfono", bgcolor="white")
    txtCorreo = ft.TextField(label="Correo Electrónico", bgcolor="white")

    def on_agregar(e):
        if txtNombre.value and txtTelefono.value and txtCorreo.value:
            agregar_cliente(conectar_db(), txtNombre.value, txtTelefono.value, txtCorreo.value)
            txtNombre.value = txtTelefono.value = txtCorreo.value = ""
            mostrar_clientes(conectar_db(), page, contenedor_clientes)
            page.snack_bar = ft.SnackBar(ft.Text("✅ Cliente agregado correctamente."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            txtNombre,
            txtTelefono,
            txtCorreo,
            ft.ElevatedButton("Agregar Cliente", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Clientes", on_click=lambda e: mostrar_clientes(conectar_db(), page, contenedor_clientes), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de clientes", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_clientes,
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
