import flet as ft

import home_page
import team_section
import about_us
import faq_page

import ferramentas_eletricas_page
import ferramentas_manuais_page
import acessorios_page

from dicionarios import produtos_organizados

from ui_components import cards_produtos, criar_content_produtos, navbar_content, footer_content

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

    estrutura_cards = cards_produtos(produtos_organizados['Acessórios'])
    cards_content = criar_content_produtos(estrutura_cards)

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