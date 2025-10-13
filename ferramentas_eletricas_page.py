import flet as ft

import home_page
import team_section
import about_us

from dicionarios import produtos_organizados

from function_cards_products import cards_produtos, criar_content_produtos

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

    estrutura_cards = cards_produtos(produtos_organizados['Ferramentas Elétricas'])
    cards_content = criar_content_produtos(estrutura_cards)

    texto_teste = ft.Container(
        ft.Row(
            [
                ft.Text(
                    'Esta é a página da Categoria de Ferramentas Elétricas!',
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    footer = ft.ResponsiveRow(
        [
            ft.Container(
                ft.Column(
                    [

                    ],
                ),
                col={"xs": 0, "sm": 0, "md": 1, "lg": 1},
            ),

            ft.Container(
                content=ft.Column(
                    [
                        ft.ResponsiveRow(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            'Sobre a Loja',
                                            weight=ft.FontWeight.BOLD,
                                            color='#FFFFFF',
                                            font_family='Verdana',
                                            size=15,
                                        ),

                                        ft.GestureDetector(
                                            content=ft.Text(
                                                'Aqui você encontra ferramentas de qualidade para todas as suas necessidades!',
                                                color='#FFFFFF',
                                                font_family='Verdana',
                                                size=10,
                                            ),
                                            on_tap=lambda e: about_us.main(page),
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        )

                                    ],
                                    col={"xs": 12, "sm": 6, "md": 3, "lg": 3},
                                ),

                                ft.Column(
                                    [
                                        ft.Text(
                                            'Integrantes do Projeto',
                                            weight=ft.FontWeight.BOLD,
                                            color='#FFFFFF',
                                            font_family='Verdana',
                                            size=15,
                                        ),

                                        ft.GestureDetector(
                                            content=ft.Text(
                                                'Diego José Araújo Santos', 
                                                color='#FFFFFF', 
                                                font_family='Verdana', 
                                                size=10,
                                            ),
                                            on_tap=lambda e: team_section.main(page),
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        ),

                                        ft.GestureDetector(
                                            content=ft.Text(
                                                'Diego Samuel Soares Pereira de Araujo', 
                                                color='#FFFFFF', 
                                                font_family='Verdana', 
                                                size=10,
                                            ),
                                            on_tap=lambda e: team_section.main(page),
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        ),

                                        ft.GestureDetector(
                                            content=ft.Text(
                                                'Thalys Rafael de Brito Batalha', 
                                                color='#FFFFFF', 
                                                font_family='Verdana', 
                                                size=10,
                                            ), 
                                            on_tap=lambda e: team_section.main(page),
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        ),
                                    ],
                                    col={"xs": 12, "sm": 6, "md": 3, "lg": 3}
                                ),

                                ft.Column(
                                    [
                                        ft.Text(
                                            'Nossas Redes Sociais',
                                            weight=ft.FontWeight.BOLD,
                                            color='#FFFFFF',
                                            font_family='Verdana',
                                            size=15,
                                        ),

                                        ft.ResponsiveRow(
                                            [
                                                ft.Row(
                                                    [
                                                        ft.Image(
                                                            src='Flet - Loja Online Versão 1.3.8/assets/imagens/facebook_logo.png', 
                                                            width=24, 
                                                            height=24, 
                                                            fit=ft.ImageFit.CONTAIN,
                                                        ),

                                                        ft.Text(
                                                            'Facebook: /ferramentafacilexpress', 
                                                            color='#FFFFFF', 
                                                            font_family='Verdana', 
                                                            size=10,                  
                                                        ),
                                                    ],
                                                    col={"xs": 0,"xl": 12}
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.Image(
                                                            src='Flet - Loja Online Versão 1.3.8/assets/imagens/instagram_logo.png', 
                                                            width=24, 
                                                            height=24, 
                                                            fit=ft.ImageFit.CONTAIN,
                                                        ),
                                                        ft.Text(
                                                            'Instagram: @ferramentafacilexpress', 
                                                            color='#FFFFFF', 
                                                            font_family='Verdana', 
                                                            size=10,
                                                        ),
                                                    ],
                                                    col={"xs": 0, "xl": 12}
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.Image(
                                                            src='Flet - Loja Online Versão 1.3.8/assets/imagens/youtube_logo.png', 
                                                            width=24, 
                                                            height=24, 
                                                            fit=ft.ImageFit.CONTAIN,
                                                        ),
                                                        ft.Text(
                                                            'YouTube: FerramentaFácil Express', 
                                                            color='#FFFFFF', 
                                                            font_family='Verdana', 
                                                            size=10,
                                                        ),
                                                    ],
                                                    col={"xs": 0, "xl": 12}
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.Image(
                                                            src='Flet - Loja Online Versão 1.3.8/assets/imagens/twitter_logo.png', 
                                                            width=24, 
                                                            height=24, 
                                                            fit=ft.ImageFit.CONTAIN,
                                                        ),
                                                        ft.Text(
                                                            'X: @facilexpressbr', 
                                                            color='#FFFFFF', 
                                                            font_family='Verdana', 
                                                            size=10,
                                                        ),
                                                    ],
                                                    col={"xs": 0, "xl": 12}
                                                ),
                                            ],
                                        ),
                                    ],
                                    col={"xs": 12, "sm": 6, "md": 3, "lg": 3}
                                ),

                                ft.Column(
                                    [
                                        ft.Text(
                                            'Entre em Contato Conosco',
                                            weight=ft.FontWeight.BOLD,
                                            color='#FFFFFF',
                                            font_family='Verdana',
                                            size=15,
                                        ),

                                        ft.Text(
                                            'Email: contato@ferramentafacilexpress.com', 
                                            color='#FFFFFF', 
                                            font_family='Verdana', 
                                            size=10,
                                        ),

                                        ft.Text(
                                            'Telefone: (84) 99999-9999', 
                                            color='#FFFFFF', 
                                            font_family='Verdana', 
                                            size=10,
                                        ),
                                    ],
                                    col={"xs": 12, "sm": 6, "md": 3, "lg": 3}
                                ),
                            ],
                        ),

                        ft.Container(
                            content=ft.Text(
                                '© 2025 - Projeto de POO Integrado - IFRN - Versão 1.0',
                                color='#FFFFFF',
                                font_family='Verdana',
                                size=10,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(top=20),
                        ),
                    ],
                ),
                bgcolor='#102739',
                alignment=ft.alignment.center,
                padding=ft.padding.only(left=30, right=30, top=24, bottom=24),
                border_radius=ft.border_radius.all(6),
                margin=ft.margin.only(top=20, bottom=10),
                col={"xs": 12, "sm": 12, "md": 10, "lg": 10}
            ),

            ft.Container(
                ft.Column(
                    [

                    ],
                ),
                col={"xs": 0,"sm": 0, "md": 1, "lg": 1},
            ),
        ],
        spacing=0,
    )

    page.add(
        ft.Column(
            [
                header,
                texto_teste,
                cards_content,
                footer,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")