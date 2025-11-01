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

    texto_teste = ft.Container(
        ft.Row(
            [
                ft.Text(
                    'Esta vai ser a página de About Us!',
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

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
                texto_teste,
                botao_retornar,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")

    # Teste para login - Ignorar!
    # ft.MenuBar(
    #                                         style=ft.MenuStyle(
    #                                             mouse_cursor={
    #                                                 ft.ControlState.HOVERED: ft.MouseCursor.CLICK
    #                                             },
    #                                             alignment=ft.alignment.center,
    #                                             bgcolor='#102739',
    #                                             elevation=0,
    #                                         ),
    #                                         controls=[
    #                                             ft.SubmenuButton(
    #                                                 content=ft.Text(
    #                                                     'Categorias',
    #                                                     weight=ft.FontWeight.BOLD,
    #                                                     color='#FFFFFF',
    #                                                     font_family='Verdana',
    #                                                     size=13
    #                                                 ),
    #                                                 controls=[
    #                                                     ft.MenuItemButton(
    #                                                         content=ft.Text(
    #                                                             'Sua Conta',
    #                                                         ),
    #                                                         on_click=lambda e: ferramentas_eletricas_page.main(page),
    #                                                     ),
    #                                                     ft.MenuItemButton(
    #                                                         content=ft.Text(
    #                                                             'Cadastrar-se'
    #                                                         ),
    #                                                         on_click=lambda e: ferramentas_manuais_page.main(page),
    #                                                     ),
    #                                                     ft.MenuItemButton(
    #                                                         content=ft.Text(
    #                                                             'Desconectar-se'
    #                                                         ),
    #                                                         on_click=lambda e: acessorios_page.main(page),
    #                                                     ),
    #                                                 ]
    #                                             ),
    #                                         ]
    #                                     ),