import flet as ft

from dicionarios import produtos_organizados

from ui_components import navbar_content, footer_content, cards_de_produto, criar_content_produtos

def main(page: ft.Page):
    page.clean()
    page.title = 'Categoria "Acessórios" - FerramentaFácil Express'

    page.fonts = {
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }

    page.window.maximized = True 
    page.window.width = None
    page.window.height = None

    page.bgcolor = '#FFFFFF'
    page.scroll = ft.ScrollMode.AUTO

    header = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Text(
                    "Categoria de Produtos - Acessórios", 
                    style=ft.TextThemeStyle.HEADLINE_LARGE, 
                    text_align=ft.TextAlign.CENTER,
                    col={"xs": 12},
                    color='#FFFFFF',
                    weight=ft.FontWeight.BOLD
                ),
            ],
        ),
        bgcolor="#0059D4",
        padding=ft.padding.only(top=20, bottom=20)
    )

    navbar = navbar_content(page)

    estruturas_cards = cards_de_produto(produtos_organizados['Acessórios'])
    cards_content = criar_content_produtos(estruturas_cards)

    footer = footer_content(page)

    juntar_header = ft.Container(
        ft.Column(
            [
                header, navbar,
            ],
            spacing=0,
        )
    )

    page.add(
        ft.Column(
            [   
                juntar_header,
                cards_content,
                footer,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")