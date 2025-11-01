import flet as ft

from dicionarios import produtos_organizados

# Módulos para os cards de produto
def cards_produtos (lista_produtos: list):
    cards_de_produtos = []

    for produto in lista_produtos:
        if produto.get('imagem_url'):
            imagem_card = ft.Row(
                [
                    ft.Image(
                        src=produto['imagem_url'],
                        fit=ft.ImageFit.COVER,
                        height=150,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        else:
            imagem_card = ft.Container(
                content=ft.Icon(
                    ft.Icons.CONSTRUCTION,
                    size=80,
                    color="#E63333",
                ),
                alignment=ft.alignment.center,
                height=150,
                bgcolor="#382F2F",
            )
    
        imagem_content = ft.Container(
            content=imagem_card,
            border_radius=8,
        )

        product_footer = ft.Row(
            controls=[
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Text(
                                f'R$ {produto['preco']:.2f}',
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="#000000"
                            ),
                            ft.Text(
                                f'Em Estoque ({produto['estoque']})',
                                size=14,
                                color="#0F7909",
                                weight=ft.FontWeight.W_600,
                            )
                        ],
                        spacing=5,
                    ),
                    expand=True
                ),
                
                ft.ElevatedButton(
                    text='Comprar',
                    icon=ft.Icons.SHOPPING_CART_OUTLINED,
                    style=ft.ButtonStyle(
                        padding=ft.padding.symmetric(vertical=10, horizontal=15),
                        shape=ft.RoundedRectangleBorder(radius=8),
                        text_style=ft.TextStyle(
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ),
                    on_click=lambda e:None,
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        card_content = ft.Container(
            content=ft.Column(
                controls=[
                    imagem_content,

                    ft.Text(
                        produto['nome'],
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),

                    ft.Text(
                        f'Marca: {produto['marca']} • ID: {produto['id']}',
                        size=14,
                        color='#8A000000',
                        weight=ft.FontWeight.W_500,
                    ),

                    ft.Divider(
                        height=1,
                        thickness=1,
                        color='#8A000000'
                    ),

                    product_footer,
                ],
                spacing=11,
            ),
            padding=ft.padding.all(15),
            bgcolor='#FFFFFF',
            border_radius=12,
            border=ft.border.all(
                1, 
                '#FFE0E0E0'
            ),
            shadow=ft.BoxShadow(
                blur_radius=5,
                color='#1F000000',
            ),
            col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
        )

        cards_de_produtos.append(card_content)
    
    return ft.ResponsiveRow(
        controls=cards_de_produtos,
        run_spacing={"xs": 20, "sm": 20, "md": 30},
        alignment=ft.MainAxisAlignment.CENTER,
    )

def criar_content_produtos (content_page: ft.Control):
    conteudo = ft.Column(
        [
            content_page,
        ],
        col={"xs": 12, "sm": 10},
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.ResponsiveRow(
        controls=[
            ft.Container(
                col={"xs": 0, "sm": 1}
            ),

            conteudo,

            ft.Container(
                col={"xs": 0, "sm": 1},
            ),
        ],
        run_spacing=50,
    )

# Módulos do header, do Navber e do conteúdo de login 
def login_content (page):
    campo_usuario = ft.TextField(
        hint_text='Usuário',
        color='#FFFFFF',
        border=ft.InputBorder.UNDERLINE,
        border_color='#FFFFFF',
        focused_border_color='#FFFC00',
        focused_color='#FFFC00',
        filled=False,
        hint_style=ft.TextStyle(color='#FFFFFF'),
    )
    
    campo_email = ft.TextField(
        hint_text='Digite o seu endereço de Email',
        color='#FFFFFF',
        border=ft.InputBorder.UNDERLINE,
        border_color='#FFFFFF',
        focused_border_color='#FFFC00',
        focused_color='#FFFC00',
        filled=False,
        hint_style=ft.TextStyle(color='#FFFFFF'),
    )

    campo_senha = ft.TextField(
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
        hint_style=ft.TextStyle(color='#FFFFFF'),
    )

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
                            ft.Text('Nome do Usuário:', color='#FFFFFF'),
                            campo_usuario,
                        ],
                        spacing=0,
                    ),
                    ft.Column(
                        [
                            ft.Text('E-mail:', color='#FFFFFF'),
                            campo_email,
                        ],
                    ),
                    ft.Column(
                        [
                            ft.Text('Senha:', color='#FFFFFF'),
                            campo_senha,
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
        bgcolor='#4073FF',
        shape=ft.RoundedRectangleBorder(radius=18.0),
    )
    
    return login_tela

def header_content (page, login_dialogue):
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
                                            on_tap=lambda e: page.open(login_dialogue),
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
                                                    on_tap=lambda e: page.open(login_dialogue),
                                                    mouse_cursor=ft.MouseCursor.CLICK,
                                                ),
                                                ft.GestureDetector(
                                                    ft.Text(
                                                        'Entre / Registre-se', 
                                                        weight=ft.FontWeight.BOLD,
                                                        size=12,
                                                    ),
                                                    on_tap=lambda e:page.open(login_dialogue),
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

    return header

def navbar_content (page):
    import acessorios_page, faq_page, ferramentas_eletricas_page, ferramentas_manuais_page, home_page
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

    return navbar

# Modúlo do Hero Section
def hero_section_content (page):
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

    return hero_section

# Módulo do Footer
def footer_content (page):  
    import about_us, team_section
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

    return footer