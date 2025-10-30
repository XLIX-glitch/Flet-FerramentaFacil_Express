import flet as ft

import home_page
import team_section
import about_us
import faq_page

import ferramentas_eletricas_page
import ferramentas_manuais_page
import acessorios_page

from dicionarios import produtos_organizados

from function_cards_products import cards_produtos, criar_content_produtos

def main(page: ft.Page):
    page.clean()
    page.title = 'Categoria "Ferramentas Manuais" - FerramentaFácil Express'

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
                    "Categoria de Produtos - Ferramentas Manuais", 
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

    navbar = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Column(
                        [

                        ]
                    ),
                    col={"xs": 0, "sm": 1}
                ),
                
                ft.Column(
                    [
                        ft.ResponsiveRow(
                            [
                                ft.Column(
                                    [
                                        ft.MenuBar(
                                            style=ft.MenuStyle(
                                                mouse_cursor={
                                                    ft.ControlState.HOVERED: ft.MouseCursor.CLICK
                                                },
                                                alignment=ft.alignment.center,
                                                bgcolor='#102739',
                                                elevation=0,
                                            ),
                                            controls=[
                                                ft.SubmenuButton(
                                                    ft.GestureDetector(
                                                        content=ft.Text(
                                                            'Home',
                                                            weight=ft.FontWeight.BOLD,
                                                            color='#FFFFFF',
                                                            font_family='Verdana',
                                                            size=13,
                                                        ),
                                                        on_tap=lambda e:home_page.main(page),
                                                        mouse_cursor=ft.MouseCursor.CLICK,

                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1},
                                ),
                                ft.Column(
                                    [
                                        ft.MenuBar(
                                            style=ft.MenuStyle(
                                                mouse_cursor={
                                                    ft.ControlState.HOVERED: ft.MouseCursor.CLICK
                                                },
                                                alignment=ft.alignment.center,
                                                bgcolor='#102739',
                                                elevation=0,
                                            ),
                                            controls=[
                                                ft.SubmenuButton(
                                                    content=ft.Text(
                                                        'Categorias',
                                                        weight=ft.FontWeight.BOLD,
                                                        color='#FFFFFF',
                                                        font_family='Verdana',
                                                        size=13
                                                    ),
                                                    controls=[
                                                        ft.MenuItemButton(
                                                            content=ft.Text(
                                                                'Ferramentas Elétricas',
                                                            ),
                                                            on_click=lambda e: ferramentas_eletricas_page.main(page),
                                                        ),
                                                        ft.MenuItemButton(
                                                            content=ft.Text(
                                                                'Ferramentas Manuais'
                                                            ),
                                                            on_click=lambda e: ferramentas_manuais_page.main(page),
                                                        ),
                                                        ft.MenuItemButton(
                                                            content=ft.Text(
                                                                'Acessórios'
                                                            ),
                                                            on_click=lambda e: acessorios_page.main(page),
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1.3},
                                ),
                                ft.Column(
                                    [
                                        ft.MenuBar(
                                            style=ft.MenuStyle(
                                                mouse_cursor={
                                                    ft.ControlState.HOVERED: ft.MouseCursor.CLICK
                                                },
                                                alignment=ft.alignment.center,
                                                bgcolor='#102739',
                                                elevation=0,
                                            ),
                                            controls=[
                                                ft.SubmenuButton(
                                                    ft.GestureDetector(
                                                        content=ft.Text(
                                                            'Produtos',
                                                            weight=ft.FontWeight.BOLD,
                                                            color='#FFFFFF',
                                                            font_family='Verdana',
                                                            size=13,
                                                        ),
                                                        on_tap=lambda e:None,
                                                        mouse_cursor=ft.MouseCursor.CLICK,

                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1.1},
                                ),
                                ft.Column(
                                    [
                                        ft.MenuBar(
                                            style=ft.MenuStyle(
                                                mouse_cursor={
                                                    ft.ControlState.HOVERED: ft.MouseCursor.CLICK
                                                },
                                                alignment=ft.alignment.center,
                                                bgcolor='#102739',
                                                elevation=0,
                                            ),
                                            controls=[
                                                ft.SubmenuButton(
                                                    ft.GestureDetector(
                                                        content=ft.Text(
                                                            'Ofertas',
                                                            weight=ft.FontWeight.BOLD,
                                                            color='#FFFFFF',
                                                            font_family='Verdana',
                                                            size=13,
                                                        ),
                                                        on_tap=lambda e:None,
                                                        mouse_cursor=ft.MouseCursor.CLICK,

                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1},
                                ),

                                ft.Column(
                                    [

                                    ],
                                    col={"xs": 0, "sm": 0, "md": 6.6}

                                ),
                                ft.Column(
                                    [
                                        ft.MenuBar(
                                            style=ft.MenuStyle(
                                                mouse_cursor={
                                                    ft.ControlState.HOVERED: ft.MouseCursor.CLICK
                                                },
                                                alignment=ft.alignment.center,
                                                bgcolor='#102739',
                                                elevation=0,
                                            ),
                                            controls=[
                                                ft.SubmenuButton(
                                                    ft.GestureDetector(
                                                        content=ft.Text(
                                                            'Ajuda',
                                                            weight=ft.FontWeight.BOLD,
                                                            color='#FFFFFF',
                                                            font_family='Verdana',
                                                            size=13,
                                                        ),
                                                        on_tap=lambda e:faq_page.main(page),
                                                        mouse_cursor=ft.MouseCursor.CLICK,

                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 12, "md": 1}
                                )
                            ],
                            spacing=20,
                        ),
                    ],
                    col={"xs": 12, "sm": 10},  
                ),

                ft.Column(
                    [
                        
                    ],
                    col={"xs": 0, "sm": 1},
                ),
            ],
        ),
        bgcolor='#102739',
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=30, right=30, top=8, bottom=8),
    )

    estrutura_cards = cards_produtos(produtos_organizados['Ferramentas Manuais'])
    cards_content = criar_content_produtos(estrutura_cards)

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

    juntar_header = ft.Container(
        ft.Column(
            [
                header, navbar
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