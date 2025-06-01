import flet as ft
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def agregar_empleado(conn, nombre, puesto, salario, telefono, usuario, contrasena):
    cursor = conn.cursor()
    query = "INSERT INTO empleados (nombre, puesto, salario, telefono, usuario, contrasena) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, puesto, salario, telefono, usuario, contrasena))
    conn.commit()
    cursor.close()

def eliminar_empleado(conn, id_empleado, page, contenedor_empleados):
    cursor = conn.cursor()
    query = "DELETE FROM empleados WHERE idEmpleados = %s"
    cursor.execute(query, (id_empleado,))
    conn.commit()
    cursor.close()
    mostrar_empleados(conectar_db(), page, contenedor_empleados)

def mostrar_empleados(conn, page, contenedor_empleados):
    cursor = conn.cursor()
    cursor.execute("SELECT idEmpleados, nombre, puesto, salario, telefono, usuario FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()

    contenedor_empleados.controls.clear()

    for emp in empleados:
        contenedor_empleados.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {emp[0]}", size=14, weight="bold"),
                    ft.Text(f"Nombre: {emp[1]}", size=16),
                    ft.Text(f"Puesto: {emp[2]}", size=16),
                    ft.Text(f"Salario: ${emp[3]}", size=16),
                    ft.Text(f"Teléfono: {emp[4]}", size=16),
                    ft.Text(f"Usuario: {emp[5]}", size=16),
                    ft.ElevatedButton("Eliminar", bgcolor="pink", color="white",
                        on_click=lambda e, id=emp[0]: eliminar_empleado(conectar_db(), id, page, contenedor_empleados))
                ]),
                padding=15,
                bgcolor="#FFE6F0",
                border_radius=10,
                width=400
            )
        )

    page.update()

def vista_empleados(page: ft.Page):
    page.clean()
    page.title = "Gestión de Empleados"
    page.bgcolor = "#F8F9FF"
    page.scroll = ft.ScrollMode.AUTO

    contenedor_empleados = ft.Column(scroll=ft.ScrollMode.AUTO)

    logo = ft.Row([ft.Image(src="fotos/image (3).png", width=150)], alignment=ft.MainAxisAlignment.CENTER)

    txtNombre = ft.TextField(label="Nombre", bgcolor="white")
    txtPuesto = ft.TextField(label="Puesto", bgcolor="white")
    txtSalario = ft.TextField(label="Salario ($)", bgcolor="white")
    txtTelefono = ft.TextField(label="Teléfono", bgcolor="white")
    txtUsuario = ft.TextField(label="Usuario", bgcolor="white")
    txtContrasena = ft.TextField(label="Contraseña", bgcolor="white", password=True)

    def on_agregar(e):
        if all([txtNombre.value, txtPuesto.value, txtSalario.value, txtTelefono.value, txtUsuario.value, txtContrasena.value]):
            try:
                float(txtSalario.value)
                agregar_empleado(
                    conectar_db(),
                    txtNombre.value,
                    txtPuesto.value,
                    txtSalario.value,
                    txtTelefono.value,
                    txtUsuario.value,
                    txtContrasena.value
                )
                txtNombre.value = txtPuesto.value = txtSalario.value = txtTelefono.value = txtUsuario.value = txtContrasena.value = ""
                mostrar_empleados(conectar_db(), page, contenedor_empleados)
                page.snack_bar = ft.SnackBar(ft.Text("✅ Empleado agregado correctamente."))
            except:
                page.snack_bar = ft.SnackBar(ft.Text("⚠️ El salario debe ser numérico."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
        page.snack_bar.open = True
        page.update()

    formulario = ft.Container(
        content=ft.Column([
            txtNombre,
            txtPuesto,
            txtSalario,
            txtTelefono,
            txtUsuario,
            txtContrasena,
            ft.ElevatedButton("Agregar Empleado", on_click=on_agregar, bgcolor="deeppink", color="pink"),
            ft.ElevatedButton("Mostrar Empleados", on_click=lambda e: mostrar_empleados(conectar_db(), page, contenedor_empleados), bgcolor="deeppink", color="pink")
        ], spacing=10),
        padding=20,
        bgcolor="#FFCDEA",
        border_radius=10,
        width=400
    )

    layout = ft.Container(
        content=ft.Column([
            logo,
            ft.Text("Alta y listado de empleados", size=22, weight="bold"),
            formulario,
            ft.Container(
                content=contenedor_empleados,
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
