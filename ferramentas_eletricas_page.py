import flet as ft

from dicionarios import produtos_organizados

from ui_components import cards_produtos, criar_content_produtos, navbar_content, footer_content

def main(page: ft.Page):
    page.clean()
    page.title = 'Categoria "Ferramentas Elétricas" - FerramentaFácil Express'

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
                    "Categoria de Produtos - Ferramentas Elétricas", 
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

    estrutura_cards = cards_produtos(produtos_organizados['Ferramentas Elétricas'])
    cards_content = criar_content_produtos(estrutura_cards)

    footer = footer_content(page)

    regiao_superior = ft.Container(
        ft.Column(
            [
                header, navbar
            ],
            spacing=0,
        ),
    )

    page.add(
        ft.Column(
            [
                regiao_superior, 
                cards_content,
                footer,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")