# Repositorio
# https://github.com/SofiSuriano/Topicos-Practica12

import flet as ft

from ventas import vista_ventas
from productos import vista_productos
from clientes import vista_clientes
from empleados import vista_empleados
from proveedores import vista_proveedores
from detalleventa import vista_detalleventa
from categorias import vista_categorias
from unidades import vista_unidades
from sucursales import vista_sucursales


def menu_lateral(navegar_a):
    opciones = [
        ("Inicio", "/"),
        ("Ventas", "/ventas"),
        ("Clientes", "/clientes"),
        ("Productos", "/productos"),
        ("Empleados", "/empleados"),
        ("Proveedores", "/proveedores"),
        ("Detalle Venta", "/detalleventa"),
        ("Categorías", "/categorias"),
        ("Unidades", "/unidades"),
        ("Sucursales", "/sucursales")
    ]

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("🌸 Menú", size=22, weight="bold", color="white"),
                *[
                    ft.ElevatedButton(
                        text=texto,
                        width=160,
                        bgcolor="#FF85B2",
                        color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                        on_click=lambda e, r=ruta: navegar_a(r)
                    ) for texto, ruta in opciones
                ]
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.START
        ),
        padding=20,
        bgcolor="#F06292",
        width=200
    )


def bienvenida_layout(navegar_a):
    return ft.Row(
        controls=[
            menu_lateral(navegar_a),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Image(src="fotos/image (3).png", width=160),
                        ft.Text("Bienvenid@ a Sol y Luna 🧁", size=30, weight="bold", color="#D81B60"),
                        ft.Text("Selecciona una opción del menú para comenzar", size=18, color="black")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
                expand=True,
                bgcolor="#FFF8FC",
                padding=30
            )
        ],
        expand=True
    )


def main(page: ft.Page):
    page.title = "Sistema de Gestión - Sol y Luna"
    page.bgcolor = "#FFF8FC"
    page.scroll = ft.ScrollMode.ALWAYS
    page.window_maximized = True

    def route_change(e):
        page.views.clear()
        ruta = page.route

        if ruta == "/":
            page.views.append(ft.View("/", controls=[bienvenida_layout(page.go)], bgcolor="#FFF8FC"))

        elif ruta == "/ventas":
            page.views.append(ft.View("/ventas", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_ventas(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))
            

        elif ruta == "/clientes":
            page.views.append(ft.View("/clientes", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_clientes(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))
            
        elif ruta == "/productos":
            page.views.append(ft.View("/productos", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_productos(page)
        ], expand=True)
    ], bgcolor="#FFF8FC")) 
            

        elif ruta == "/empleados":
            page.views.append(ft.View("/empleados", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_empleados(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))
            

        elif ruta == "/proveedores":
            page.views.append(ft.View("/proveedores", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_proveedores(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))
            
        elif ruta == "/detalleventa":
            page.views.append(ft.View("/detalleventa", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_detalleventa(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))

        elif ruta == "/categorias":
            page.views.append(ft.View("/categorias", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_categorias(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))
            
        elif ruta == "/unidades":
            page.views.append(ft.View("/unidades", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_unidades(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))
            
        elif ruta == "/sucursales":
            page.views.append(ft.View("/sucursales", controls=[
        ft.Row([
            menu_lateral(page.go),
            vista_sucursales(page)
        ], expand=True)
    ], bgcolor="#FFF8FC"))
            
        else:
            page.views.append(ft.View(route=ruta, controls=[ft.Text("⚠️ Página no encontrada", size=25, color="red")]))

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
