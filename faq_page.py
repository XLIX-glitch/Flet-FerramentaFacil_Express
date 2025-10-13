import flet as ft

import home_page
import team_section
import faq_page
import about_us

import ferramentas_eletricas_page
import ferramentas_manuais_page
import acessorios_page

from dicionarios import faq_informacoes

def main(page: ft.Page):
    page.clean()
    page.title = 'Frequently Asked Questions - FerramentaFácil Express'
    
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
                    "Perguntas Frequentes", 
                    style=ft.TextThemeStyle.HEADLINE_LARGE, 
                    text_align=ft.TextAlign.CENTER,
                    col={"xs": 12},
                    color='#FFFFFF',
                    weight=ft.FontWeight.BOLD
                ),
            ],
        ),
        bgcolor="#FF5100",
        padding=ft.padding.only(top=20, bottom=20)
    )

    navbar_faq = ft.Container(
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
                                                        on_tap=lambda e: home_page.main(page),
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
                                    col={"xs": 0, "sm": 0, "md": 6.7}

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

    estruturado_faq = []
    for categoria, perguntas in faq_informacoes.items():
        estruturado_faq.append(
            ft.Container(
                ft.Row(
                    [
                        ft.Text(
                            value=categoria,
                            size=23,
                            weight=ft.FontWeight.BOLD,
                            color="#002153",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                margin=ft.margin.only(top=15, bottom=15),
                bgcolor='blue',
            ),
        )

        lista_paineis = []
        for a in perguntas:
            lista_paineis.append(
                ft.ExpansionPanel(
                    can_tap_header=True,
                    header=ft.Container(
                        ft.ListTile(
                            title=ft.Text(
                                a['pergunta'],
                                weight=ft.FontWeight.BOLD,
                                size=17,
                                color='#000000',
                            ),
                            mouse_cursor=ft.MouseCursor.CLICK,
                        ),
                        margin=ft.margin.only(top=10, bottom=10),
                    ),
                    content=ft.Container(
                        ft.Text(
                            a['resposta'],
                            text_align=ft.TextAlign.JUSTIFY,
                            color='#000000',
                        ),
                        padding=ft.padding.all(15)
                    ),
                ),
            )
        
        estruturado_faq.append(
            ft.ExpansionPanelList(
                controls=lista_paineis,
                elevation=4,
                expand_icon_color='#808080',
                spacing=30,
                divider_color='#000000'
            ),
        )

        container_faq = ft.Column(
            estruturado_faq,
        )

    body = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Column([]), col={"xs": 0,"sm": 0, "md": 1, "lg": 1},
                ),     

                ft.Container(
                    ft.Column(
                        [
                            ft.ResponsiveRow(
                                [
                                    container_faq,
                                ],
                            ),
                        ],
                    ),
                    col={"xs": 12, "sm": 12, "md": 10, "lg": 10}
                ),

                ft.Container(
                    ft.Column([]), col={"xs": 0,"sm": 0, "md": 1, "lg": 1},
                ),
            ],
        ),
        margin=ft.margin.only(bottom=10)
    )

    footer_faq = ft.ResponsiveRow(
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
                                    col={"xs": 12, "sm": 6, "md": 3, "lg": 3},
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

    regiao_superior = ft.Container(
        ft.Column(
            [
                header, navbar_faq
            ],
            spacing=0,
        ),
    )

    page.add(
        ft.Column(
            [
                regiao_superior,
                body,
                footer_faq,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")