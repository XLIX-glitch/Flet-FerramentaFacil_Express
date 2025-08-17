import flet as ft

import home_page

def main(page: ft.Page):
    page.clean()
    page.title = 'About Us (Sobre Nós) - FerramentaFácil Express'

    page.fonts = {
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }

    page.window.maximized = True 
    page.window.width = None
    page.window.height = None

    page.bgcolor = '#FFFFFF'
    page.scroll = ft.ScrollMode.AUTO

    botao_retornar = ft.Container(
        ft.ResponsiveRow(
            [
                ft.ElevatedButton(
                    'RETORNAR AO MENU', 
                    on_click=lambda e: home_page.main(page),
                    bgcolor="#102739",
                    width=150,
                    height=50,
                    col={"xs": 12, "sm": 6, "md": 4, "lg": 2} 
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.add(
        ft.Column(
            [
                botao_retornar,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(target=main)