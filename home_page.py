import flet as ft

import team_section
import faq_page
import about_us

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

    header_2 = ft.Container(
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
                                                src='imagens/logo_empresa_p_header2.png',  
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
                                                src='imagens/icone_login.png',
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
                                                src='imagens/icone_carrinho.png',
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

    header = ft.Container(
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Image(
                            src='imagens/logo_empresa_p_header2.png', 
                            width=220, 
                            height=80, 
                            fit=ft.ImageFit.CONTAIN,
                        ),

                        ft.TextField(
                            hint_text='Buscar produtos, marcas e muito mais...', 
                            bgcolor='#FFFFFF', 
                            border_radius=8,
                            width=700,
                            height=40,
                        ),

                        ft.Row(
                            [
                                ft.GestureDetector(
                                    ft.Image(
                                        src='imagens/icone_login.png',
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
                                                color='#000000',
                                            ),
                                            on_tap=lambda e:page.open(login_tela),
                                            mouse_cursor=ft.MouseCursor.CLICK
                                        )
                                    ],
                                    spacing=0,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                        ),
                        ft.Row(
                            [
                                ft.Image(
                                    src='imagens/icone_carrinho.png', 
                                    width=30,
                                    height=30,
                                ),

                                ft.Column(
                                    [
                                        ft.Text(
                                            '(Produtos...)', 
                                            size=12,
                                            bgcolor='#FFFFFF',
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(
                                            'Carrinho',
                                            weight=ft.FontWeight.BOLD,
                                            size=12,
                                            color='#000000',
                                        ),
                                    ],
                                    spacing=0,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                        ),
                    ],
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="#F2FF00",
        height=80,
        padding=ft.padding.only(left=60, right=60),
        alignment=ft.alignment.center
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
                                        ft.GestureDetector(
                                            ft.Text(
                                                'Home',
                                                weight=ft.FontWeight.BOLD,
                                                color='#FFFFFF',
                                                font_family='Verdana',
                                                size=13,
                                            ),
                                            on_tap=lambda e: None,
                                            mouse_cursor=ft.MouseCursor.CLICK,                                       
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1},
                                ),
                                ft.Column(
                                    [
                                        ft.GestureDetector(
                                            ft.Text(
                                                'Categorias',
                                                weight=ft.FontWeight.BOLD,
                                                color='#FFFFFF',
                                                font_family='Verdana',
                                                size=13,
                                            ),
                                            on_tap=lambda e: None,
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1},
                                ),
                                ft.Column(
                                    [
                                        ft.GestureDetector(
                                            ft.Text(
                                                'Produtos',
                                                weight=ft.FontWeight.BOLD,
                                                color='#FFFFFF',
                                                font_family='Verdana',
                                                size=13,
                                            ),
                                            on_tap=lambda e: None,
                                            mouse_cursor=ft.MouseCursor.CLICK,    
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1},
                                ),
                                ft.Column(
                                    [
                                        ft.GestureDetector(
                                            ft.Text(
                                                'Ofertas',
                                                weight=ft.FontWeight.BOLD,
                                                color='#FFFFFF',
                                                font_family='Verdana',
                                                size=13,
                                            ),
                                            on_tap=lambda e: None,
                                            mouse_cursor=ft.MouseCursor.CLICK,
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    col={"xs": 12, "sm": 6, "md": 1},
                                ),

                                ft.Column(
                                    [

                                    ],
                                    col={"xs": 0, "sm": 0, "md": 7}

                                ),
                                ft.Column(
                                    [
                                        ft.GestureDetector(
                                            ft.Text(
                                                'Ajuda',
                                                weight=ft.FontWeight.BOLD,
                                                color='#FFFFFF',
                                                font_family='Verdana',
                                                size=13,
                                            ),
                                            on_tap=lambda e: faq_page.main(page),
                                            mouse_cursor=ft.MouseCursor.CLICK,
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
        padding=ft.padding.only(left=30, right=30, top=15, bottom=15),
    )

    hero_section = ft.Container(
        content=ft.Stack(
            [
                
                ft.Container(
                    content=ft.Image(
                        src='imagens/LayoutLogin.png',
                        height=500,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                    
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                'Bem-vindos à FerramentaFácil Express',
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color='#FFFFFF',
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                'As melhores ferramentas com entrega expressa!',
                                size=18,
                                color='#FFFFFF',
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                ),
            ],
        ),
        height=500,  
        bgcolor='#F8F9FA',
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=0, bottom=20)
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
                                                            src='imagens/facebook_logo.png', 
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
                                                            src='imagens/instagram_logo.png', 
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
                                                            src='imagens/youtube_logo.png', 
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
                                                            src='imagens/twitter_logo.png', 
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
                header_2,
                hero_section,
                ft.Container(
                    footer,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20),
                ),
            ],
            expand=True,
        ),
    )
    
    page.update()

if __name__ == '__main__':
    ft.app(target=main)