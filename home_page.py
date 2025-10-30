import flet as ft
from pathlib import Path

import team_section
import faq_page
import about_us

import ferramentas_eletricas_page
import ferramentas_manuais_page
import acessorios_page

from dicionarios import produtos_organizados

from function_cards_products import cards_produtos, criar_content_produtos 

def main(page: ft.Page):
    page.clean()
    page.title = 'Menu Principal - FerramentaFácil Express'

    page.fonts = {
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }
    
    page.window.maximized = True 
    page.window.width = None
    page.window.height = None
    
    page.bgcolor = '#FFFFFF'
    page.scroll = ft.ScrollMode.AUTO

    def next_image(e):
        nonlocal index
        index = (index + 1) % len(imagens)
        switcher.content = ft.Image(
            src=imagens[index],
            fit=ft.ImageFit.COVER,
            border_radius=10,
            expand=True,
        )
        switcher.transition = ft.AnimatedSwitcherTransition.FADE

        switcher.update()
    
    def previous_image(e):
        nonlocal index
        index = (index - 1) % len(imagens)
        switcher.content = ft.Image(
            src=imagens[index],
            fit=ft.ImageFit.COVER,
            border_radius=10,
            expand=True,
        )
        switcher.transition = ft.AnimatedSwitcherTransition.FADE

        switcher.update()


    login_tela = ft.AlertDialog(
        title=ft.Text(
            'LOGIN',
            weight=ft.FontWeight.BOLD,
            color='#FFFFFF',
            font_family='Open Sans'
        ),
        content=ft.Container(
            ft.Column(
                [
                    ft.Column(
                        [
                            ft.Text(
                                'Nome do Usuário:',
                                color='#FFFFFF',
                            ),

                            ft.TextField(
                                hint_text='Usuário',
                                color='#FFFFFF',
                                border=ft.InputBorder.UNDERLINE,
                                border_color='#FFFFFF',
                                focused_border_color='#FFFC00',
                                focused_color='#FFFC00',
                                filled=False,
                                hint_style=ft.TextStyle(
                                    color='#FFFFFF',
                                ),
                            ),
                        ],
                        spacing=0,
                    ),
                    
                    ft.Column(
                        [
                            ft.Text(
                                'E-mail:',
                                color='#FFFFFF',
                            ),

                            ft.TextField(
                                hint_text='Digite o seu endereço de Email',
                                color='#FFFFFF',
                                border=ft.InputBorder.UNDERLINE,
                                border_color='#FFFFFF',
                                focused_border_color='#FFFC00',
                                focused_color='#FFFC00',
                                filled=False,
                                hint_style=ft.TextStyle(
                                    color='#FFFFFF'
                                ),

                            ),
                        ],
                    ),

                    ft.Column(
                        [
                            ft.Text(
                                'Senha:',
                                color='#FFFFFF'
                            ),

                            ft.TextField(
                                hint_text='×××××××',
                                color='#FFFFFF',
                                border=ft.InputBorder.UNDERLINE,
                                border_color='#FFFFFF',
                                password=True,
                                can_reveal_password=True,
                                max_length=10,
                                focused_border_color='#FFFC00',
                                focused_color='#FFFC00',
                                filled=False,
                                hint_style=ft.TextStyle(
                                    color='#FFFFFF'
                                )
                            ),
                        ],
                    ), 
                    ft.Container(
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    'ENTRAR', 
                                    on_click=lambda e: page.close(login_tela),
                                    bgcolor="#00E1FF",
                                    color='#FFFFFF',
                                    height=40,
                                    width=230,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        margin=ft.margin.only(top=20)            
                    ),
                ],
            ),
            height=320,
            width=300,
        ),
        bgcolor='#002CA3',
        shape=ft.RoundedRectangleBorder(radius=18.0),
    )

    header = ft.Container(
        content=ft.ResponsiveRow(
            [   
                ft.Column(
                    [], col={"xs": 0, "sm": 1}
                ),
                
                ft.Column(
                    [
                        ft.ResponsiveRow(
                            [
                                ft.Column(
                                    [
                                        ft.GestureDetector(
                                            ft.Image(
                                                src='Flet - Loja Online Versão 1.3.8/assets/imagens/logo_empresa_p_header2.png',  
                                                fit=ft.ImageFit.CONTAIN,
                                            ),
                                            on_tap=lambda e: None,
                                            mouse_cursor=ft.MouseCursor.CLICK,                                       
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 2, "lg": 2, "xl": 2, "xxl": 2},
                                ),
                                ft.Column(
                                    [
                                        ft.TextField(
                                            hint_text='Buscar produtos, marcas e muito mais...', 
                                            bgcolor='#FFFFFF', 
                                            border_radius=8,
                                            height=40,
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 7.3, "lg": 7.3, "xl": 7.3, "xxl": 7.3},
                                ),
                                ft.Row(
                                    [
                                        ft.GestureDetector(
                                            ft.Image(
                                                src='Flet - Loja Online Versão 1.3.8/assets/imagens/icone_login.png',
                                                width=30,
                                                height=30,
                                            ),
                                            on_tap=lambda e: page.open(login_tela),
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        ),
                                        ft.Column(
                                            [
                                                ft.GestureDetector(
                                                    content=ft.Text(
                                                        'Olá!',
                                                        size=12,
                                                        color='#000000',
                                                    ),
                                                    on_tap=lambda e: page.open(login_tela),
                                                    mouse_cursor=ft.MouseCursor.CLICK,
                                                ),
                                                ft.GestureDetector(
                                                    ft.Text(
                                                        'Entre / Registre-se', 
                                                        weight=ft.FontWeight.BOLD,
                                                        size=12,
                                                    ),
                                                    on_tap=lambda e:page.open(login_tela),
                                                    mouse_cursor=ft.MouseCursor.CLICK
                                                ),
                                            ],
                                            spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),  
                                    ],       
                                    col={"xs": 12, "sm": 6, "md": 1.7, "lg": 1.7, "xl": 1.7, "xxl": 1.7},
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    [
                                        
                                        ft.GestureDetector(
                                            ft.Image(
                                                src='Flet - Loja Online Versão 1.3.8/assets/imagens/icone_carrinho.png',
                                                width=30,
                                                height=30,
                                            ),
                                            on_tap=lambda e: None,
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        ),
                                        ft.Column(
                                            [
                                                ft.GestureDetector(
                                                    content=ft.Text(
                                                        '(Produtos...)', 
                                                        size=12,
                                                        bgcolor='#FFFFFF',
                                                        weight=ft.FontWeight.BOLD,
                                                    ),
                                                    on_tap=lambda e: None,
                                                    mouse_cursor=ft.MouseCursor.CLICK,
                                                ),
                                                ft.GestureDetector(
                                                    ft.Text(
                                                        'Carrinho',
                                                        weight=ft.FontWeight.BOLD,
                                                        size=12,
                                                        color='#000000'
                                                    ),
                                                    on_tap=lambda e: None,
                                                    mouse_cursor=ft.MouseCursor.CLICK
                                                ),
                                            ],
                                            spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ],
                                    col={"xs": 12, "sm": 6, "md": 1, "lg": 1, "xl": 1, "xxl": 1},
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                            ],
                            spacing=20,
                        ),
                    ],
                    col={"xs": 12, "sm": 10},  
                ),

                ft.Column(
                    [], col={"xs": 0, "sm": 1},
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor='#F2FF00',
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=30, right=30, top=20, bottom=20),
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
                                                        on_tap=lambda e:None,
                                                        mouse_cursor=ft.MouseCursor.CLICK,

                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
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
                                    horizontal_alignment=ft.CrossAxisAlignment.END,
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

    hero_section = ft.Container(
    content=ft.ResponsiveRow(
        [
            ft.Column(
                [], col={"xs": 0, "sm": 1}
            ),

            ft.Column(
                [
                    ft.Image(
                        src='Flet - Loja Online Versão 1.3.8/assets/imagens/hero_section_content.png',
                        height=600,
                    ),
                ],
                col={"xs": 12, "sm": 10},
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),

            ft.Column(
                [], col={"xs": 0, "sm": 1},
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ),
    alignment=ft.alignment.center,
    margin=ft.margin.symmetric(vertical=20),
    bgcolor='#9D1C1C'
)
    
    estrutura_cards = cards_produtos(produtos_organizados['Ferramentas Elétricas'])
    cards_content = criar_content_produtos(estrutura_cards)


    base_dir = Path(__file__).parent

    pasta_imagens = base_dir / "assets" / "imagens" / "imagens_carousel"

    imagens = [str(img) 
               for img in pasta_imagens.glob("*") 
               if img.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif")
    ]

    if not imagens:
        page.add(ft.Text("Nenhuma imagem encontrada no diretório."))
        return

    index = 0

    switcher = ft.AnimatedSwitcher(
        content=ft.Image(
            src=imagens[index],
            fit=ft.ImageFit.COVER,
            border_radius=10,
        ),
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=600,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        expand=True,
    )

    carousel_image = ft.Container(
        content=switcher,
        height=400,
        expand=True,
        border_radius=8,
        alignment=ft.alignment.center,
    )

    carousel_buttons = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.CHEVRON_LEFT,
                    tooltip=ft.Tooltip(
                        message='Anterior'
                    ),
                    icon_color='#FF5100',
                    icon_size=30,
                    on_click=previous_image,
                ),
                ft.IconButton(
                    icon=ft.Icons.CHEVRON_RIGHT,
                    tooltip=ft.Tooltip(
                        message='Próximo',
                    ),
                    icon_color='#FF5100',
                    icon_size=30,
                    on_click=next_image,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=10, right=10),
        bgcolor=None,
    )

    carousel_content = ft.Stack(
        [carousel_image, carousel_buttons],
        expand=True,
        alignment=ft.alignment.center,
    )

    carousel = ft.ResponsiveRow(
        [
            ft.Column(
                [], 
                col={"xs": 0, "sm": 1},
            ),
            ft.Column(
                [
                    carousel_content,
                ],
                col={"xs": 12, "sm": 10},
            ),
            ft.Column(
                [], 
                col={"xs": 0, "sm": 1},
            ),
        ],
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

    juntar_header = ft.Column(
        [header, navbar],
        spacing=0
    )

    page.add(
        ft.Column(
            [
                juntar_header,
                hero_section,
                cards_content,
                carousel,
                ft.Container(
                    footer,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=15),
                ),
            ],
            expand=True,
        ),
    )
    
    page.update()

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")