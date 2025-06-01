import flet as ft
import mysql.connector
from datetime import datetime
import winsound

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suri@no281005",
        database="pasteleriasolyluna"
    )

def obtener_clientes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT idClientes, nombre, telefono, correo FROM clientes")
    datos = cursor.fetchall()
    conn.close()
    return datos

def obtener_empleados():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT idEmpleados, nombre FROM empleados")
    datos = cursor.fetchall()
    conn.close()
    return datos

def buscar_producto_por_codigo(codigo):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT idProductos, nombre, precio FROM productos WHERE codigoBarras = %s", (codigo,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def vista_ventas(page: ft.Page):
    page.clean()
    page.scroll = ft.ScrollMode.ALWAYS
    page.bgcolor = "#F8F9FF"
    page.title = "Gestión de Ventas"

    # ---------------- CLIENTES -------------------
    clientes = obtener_clientes()
    dropdown_clientes = ft.Dropdown(
        label="Seleccionar Cliente",
        width=300,
        options=[ft.dropdown.Option(key="1", text="Cliente General")]
    )

    cliente_info = ft.Text("Cliente: Cliente General", size=16, color="deeppink")
    cliente_datos = ft.Column([])

    for c in clientes:
        if str(c[0]) != "1":
            dropdown_clientes.options.append(ft.dropdown.Option(key=str(c[0]), text=f"{c[1]} ({c[0]})"))

    def actualizar_cliente(e):
        seleccionado = next((c for c in clientes if str(c[0]) == dropdown_clientes.value), None)
        if seleccionado:
            cliente_info.value = f"Cliente: {seleccionado[1]}"
            cliente_datos.controls = [
                ft.Text(f"📞 Teléfono: {seleccionado[2]}"),
                ft.Text(f"📧 Correo: {seleccionado[3]}")
            ]
        else:
            cliente_info.value = "Cliente: Cliente General"
            cliente_datos.controls = []
        page.update()

    dropdown_clientes.on_change = actualizar_cliente
    dropdown_clientes.value = "1"

    # ---------------- EMPLEADOS -------------------
    empleados = obtener_empleados()
    dropdown_empleados = ft.Dropdown(label="Empleado", width=300)
    for e in empleados:
        dropdown_empleados.options.append(ft.dropdown.Option(key=str(e[0]), text=e[1]))

    dropdown_pago = ft.Dropdown(
        label="Método de Pago",
        options=[ft.dropdown.Option("Efectivo"), ft.dropdown.Option("Tarjeta"), ft.dropdown.Option("Transferencia")],
        width=300
    )

    # ---------------- PRODUCTOS -------------------
    codigo_input = ft.TextField(label="Código de Barras", bgcolor="white", width=300)
    total_text = ft.Text("Total: $0.00", size=20, weight="bold", color="deeppink")

    filas_articulos = []
    contenedor_scroll = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    scroll_productos = ft.Container(
        content=contenedor_scroll,
        height=250,
        width=700,
        bgcolor="#FFF0F5",
        border_radius=12,
        padding=10
    )

    def calcular_total():
        total = 0
        for fila in filas_articulos:
            try:
                cantidad = int(fila["cantidad"].value)
                precio = float(fila["precio"].value)
                subtotal = cantidad * precio
                fila["subtotal"].value = f"Subtotal: ${subtotal:.2f}"
                total += subtotal
            except:
                pass
        total_text.value = f"Total: ${total:.2f}"
        page.update()

    def eliminar_fila(fila_control):
        contenedor_scroll.controls.remove(fila_control["row"])
        filas_articulos.remove(fila_control)
        calcular_total()
        page.update()

    def agregar_producto_por_codigo(e=None):
        codigo = codigo_input.value.strip()
        if not codigo:
            return
        producto = buscar_producto_por_codigo(codigo)
        if producto:
            winsound.Beep(1000, 150)
            id_producto, nombre, precio_unitario = producto
            cantidad = ft.TextField(value="1", width=60)
            precio = ft.TextField(value=str(precio_unitario), disabled=True, width=80)
            subtotal = ft.Text(f"Subtotal: ${precio_unitario:.2f}", width=150)

            fila = {
                "id": id_producto,
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal
            }

            cantidad.on_change = lambda e: calcular_total()

            eliminar_btn = ft.IconButton(
                icon=ft.icons.DELETE,
                icon_color="deeppink",
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=lambda e: eliminar_fila(fila)
            )

            row = ft.Row([
                ft.Text(nombre, width=180),
                precio,
                cantidad,
                subtotal,
                eliminar_btn
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

            fila["row"] = row
            filas_articulos.append(fila)
            contenedor_scroll.controls.append(row)

            codigo_input.value = ""
            calcular_total()
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("❌ Producto no encontrado."))
            page.snack_bar.open = True
            page.update()
            codigo_input.value = ""

    def registrar_venta(e):
        if not dropdown_clientes.value or not dropdown_empleados.value or not dropdown_pago.value:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Llena todos los campos."))
            page.snack_bar.open = True
            page.update()
            return

        if not filas_articulos:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Agrega al menos un producto."))
            page.snack_bar.open = True
            page.update()
            return

        conn = conectar_db()
        cursor = conn.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total = sum(int(f["cantidad"].value) * float(f["precio"].value) for f in filas_articulos)

        cursor.execute(
            "INSERT INTO ventas (fechaVenta, montoTotal, metodoPago, idClientes, idEmpleados) VALUES (%s, %s, %s, %s, %s)",
            (fecha, total, dropdown_pago.value, dropdown_clientes.value, dropdown_empleados.value)
        )
        conn.commit()
        id_venta = cursor.lastrowid

        for f in filas_articulos:
            cursor.execute(
                "INSERT INTO detalleventa (idProductos, idVentas, cantidad, precioUnitario) VALUES (%s, %s, %s, %s)",
                (f["id"], id_venta, f["cantidad"].value, f["precio"].value)
            )

        conn.commit()
        conn.close()

        filas_articulos.clear()
        contenedor_scroll.controls.clear()
        calcular_total()

        page.snack_bar = ft.SnackBar(ft.Text("✅ Venta registrada con éxito."))
        page.snack_bar.open = True
        page.update()

    def limpiar_todo(e):
        filas_articulos.clear()
        contenedor_scroll.controls.clear()
        codigo_input.value = ""
        dropdown_clientes.value = "1"
        dropdown_empleados.value = None
        dropdown_pago.value = None
        cliente_info.value = "Cliente: Cliente General"
        cliente_datos.controls = []
        calcular_total()
        page.update()

    codigo_input.on_submit = agregar_producto_por_codigo

    logo = ft.Row(
        controls=[ft.Image(src="fotos/image (3).png", width=160)],
        alignment=ft.MainAxisAlignment.CENTER
    )

    formulario = ft.Container(
        content=ft.Column([
            dropdown_clientes,
            cliente_info,
            cliente_datos,
            dropdown_empleados,
            dropdown_pago,
            codigo_input,
            ft.ElevatedButton("Agregar Artículo", on_click=agregar_producto_por_codigo, bgcolor="#FF85B2", color="white"),
            total_text,
            ft.Row([
                ft.ElevatedButton("Registrar Venta", on_click=registrar_venta, bgcolor="#F06292", color="white"),
                ft.ElevatedButton("🔄 Limpiar Todo", on_click=limpiar_todo, bgcolor="#F06292", color="white")
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=25,
        bgcolor="#FFCDEA",
        border_radius=12,
        width=420
    )

    productos_section = ft.Container(
        content=ft.Column([
            ft.Text("🧁 Productos agregados", size=22, weight="bold", color="deeppink"),
            scroll_productos
        ], spacing=10),
        bgcolor="#FFF0F5",
        border_radius=12,
        padding=15,
        width=720
    )

    layout = ft.Container(
        content=ft.Column(
            controls=[
                logo,
                ft.Text("📋 Registro de Ventas", size=26, weight="bold", color="deeppink"),
                formulario,
                productos_section
            ],
            spacing=30,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS
        ),
        alignment=ft.alignment.center,
        expand=True
    )

    return layout
