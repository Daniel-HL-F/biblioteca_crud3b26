import flet as ft

def main_Window(page: ft.Page):
    #Configurar pagina 
    page.title = "Sistema de gestion de Biblioteca"
    page.window_width = 1100
    page.window_height = 700
    page.padding =  0
    page.bgcolor = "#10661e"

    # Elemento del  contenedor principal
    titulo = ft.Text(
        "Sistema de Gestion de Biblioteca",
        size = 24,
        weight = ft.FrontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Selccione una opcion del menu",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    #CREACION DEL CONTENEDOR PRINCIPAL
    contenido = ft.Container(
        content = ft.Column(
            controls = [
                titulo,
                subtitulo
            ],
            spacing = 10,
        ),
        padding = 30,
        expand = True
    )

    #Creacion del menu lateral
    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.colors.BLUE_GREY_900,
        paddaing = 20,
        content = ft.Column(
            controls =[
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FrontWeight.BLOD,
                    color = ft.Color.WHITE
                ),
                ft.Text(
                    "Sistema de Gestion",
                    size = 12,
                    color = ft.Color.WHITE
                ),
                ft.Divider(color=ft.Colors.BLUE_GREY_700),
               
                #Botones
                ft.ElevatedButton(
                    "Libros",
                    icon = ft.Icons.BOOK,
                    width = 180
                ),
                
                ft.ElevatedButton(
                    "Usuarios",
                    icon = ft.Icons.PERSON,
                    width = 180
                ),

                ft.ElevatedButton(
                    "Prestamo",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180
                ),

                ft.ElevatedButton(
                    "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180
                ),
            ],
            spacing=15
        )
    )

    # Layout de la pajina = toda la estructura de la pajina
    layout = ft.Row(
        controls=[
            menu_lateral,
            contenido
        ],
        expand=True
    )

    page.add(layout)