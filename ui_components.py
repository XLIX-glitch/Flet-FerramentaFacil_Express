import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated")
warnings.filterwarnings("ignore", category=UserWarning, module="gcloud")

import flet as ft
import random

from pagina_login import main

import database

def obter_todos_produtos():
    produtos_organizados = database.buscar_produtos_do_banco()  
    todos_produtos = []
    for categoria in produtos_organizados.values():
        todos_produtos.extend(categoria)
    return todos_produtos

def cards_de_produto(lista_produtos: list, em_promocao=False, on_atualizar=None):
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
                alignment=ft.MainAxisAlignment.CENTER,
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
            border_radius=10,
        )

        if len(produto['descricao']) > 100:
            descricao_curta = produto['descricao'][:100] + "..."
        else:
            descricao_curta = produto['descricao']
        
        if em_promocao and 'preco_promocional' in produto:
            preco_atual = produto['preco_promocional']
            preco_antigo = produto['preco']
            preco_display = ft.Column(
                controls=[
                    ft.Text(
                        f'R$ {preco_antigo:.2f}',
                        size=16,
                        color="#888888",
                        style=ft.TextStyle(
                            decoration=ft.TextDecoration.LINE_THROUGH,
                        ),
                    ),
                    ft.Text(
                        f'R$ {preco_atual:.2f}',
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="#E63333"
                    ),
                ],
                spacing=2,
            )
        else:
            preco_display = ft.Text(
                f'R$ {produto["preco"]:.2f}',
                size=26,
                weight=ft.FontWeight.BOLD,
                color="#000000"
            )
        
        def handle_comprar_click(e, produto_id):
            database.comprar_produto(produto_id)
            if on_atualizar:
                on_atualizar()

        product_footer = ft.Row(
            controls=[
                ft.Container(
                    ft.Column(
                        controls=[
                            preco_display,
                            ft.Text(
                                f'Em Estoque ({produto["estoque"]})',
                                size=14,
                                color="#0F7909",
                                weight=ft.FontWeight.W_600,
                            )
                        ],
                        spacing=5,
                    ),
                    expand=True,
                ),

                ft.ElevatedButton(
                    text='Comprar',
                    icon=ft.Icons.SHOPPING_CART_OUTLINED,
                    style=ft.ButtonStyle(
                        padding=ft.padding.symmetric(vertical=12, horizontal=18),
                        shape=ft.RoundedRectangleBorder(radius=10),
                        text_style=ft.TextStyle(
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#007BFF",
                        color="#FFFFFF",
                    ),
                    on_click=lambda e, produto_id=produto['id']: handle_comprar_click(e, produto_id),
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        hover_shadow = ft.BoxShadow(
            blur_radius=15,
            spread_radius=2,
            color="#3F000000",
            offset=ft.Offset(0, 8)
        )
        normal_shadow = ft.BoxShadow(
            blur_radius=8,
            spread_radius=1,
            color="#1F000000",
            offset=ft.Offset(0, 4),
        )

        card_content = ft.Container(
            content=ft.Column(
                controls=[
                    imagem_content,

                    ft.Text(
                        produto['nome'],
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        color="#333333"
                    ),

                    ft.Text(
                        descricao_curta,
                        size=14,
                        color="#666666",
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),

                    ft.Text(
                        f'Marca: {produto["marca"]} • ID: {produto["id"]}',
                        size=14,
                        color='#8A000000',
                        weight=ft.FontWeight.W_500,
                    ),

                    ft.Divider(
                        height=1,
                        thickness=1,
                        color="#8A000000",
                    ),

                    product_footer,
                ],
                spacing=12,
            ),
            padding=ft.padding.all(18),
            bgcolor="#FFFFFF",
            border_radius=15,
            border=ft.border.all(
                1,
                "#E0E0E0"
            ),
            shadow=normal_shadow,
            col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
            on_hover=lambda e: setattr(e.control, 'shadow', hover_shadow if e.data == 'true' else normal_shadow) or e.control.update()
        )

        cards_de_produtos.append(card_content)
    
    return ft.ResponsiveRow(
        controls=cards_de_produtos,
        run_spacing={"xs": 20, "sm": 20, "md": 30},
        alignment=ft.MainAxisAlignment.CENTER,
    )

def criar_content_produtos(content_page: ft.Control):
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
                
# Módulos do header e do Navber
def header_content(page):
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
                                            on_tap=lambda e: page.open(main(page)),
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
                                                    on_tap=lambda e: page.open(main(page)),
                                                    mouse_cursor=ft.MouseCursor.CLICK,
                                                ),
                                                ft.GestureDetector(
                                                    ft.Text(
                                                        'Entre / Registre-se', 
                                                        weight=ft.FontWeight.BOLD,
                                                        size=12,
                                                    ),
                                                    on_tap=lambda e: page.open(main(page)),
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
        bgcolor="#FFEA00",
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=30, right=30, top=20, bottom=20),
    )

    return header

def navbar_content(page):
    import acessorios_page, faq_page, ferramentas_eletricas_page, ferramentas_manuais_page, home_page, about_us
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
                                                            'Ofertas',
                                                            weight=ft.FontWeight.BOLD,
                                                            color='#FFFFFF',
                                                            font_family='Verdana',
                                                            size=13,
                                                        ),
                                                        on_tap=lambda e: None,
                                                        mouse_cursor=ft.MouseCursor.CLICK
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
                                                            'Sobre',
                                                            weight=ft.FontWeight.BOLD,
                                                            color='#FFFFFF',
                                                            font_family='Verdana',
                                                            size=13,
                                                        ),
                                                        on_tap=lambda e: about_us.main(page),
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
def hero_section_content(page):
    hero_section = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Column(
                    [], col={"xs": 0, "sm": 1}
                ),

                ft.Column(
                    [
                        ft.Image(
                            src='Flet - Loja Online Versão 1.3.8/assets/imagens/banner_hero_section.png',
                            height=650,
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
        margin=ft.margin.only(top=0),
        bgcolor='#102739',
        height=650,
    )

    return hero_section

# Módulo do Footer
def footer_content(page):  
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

                                        ft.GestureDetector(
                                            content=ft.Text(
                                                'Paulo Henrique Ferreira Marques', 
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

# Módulos para a criação de cada sessão do Home Page (Últimos lançamentos, Promoções Relâmpagos e Mais Populares)
def sessao_lancamentos(num_produtos=4, on_atualizar=None):
    todos_produtos = obter_todos_produtos()
    produtos_selecionados = random.sample(todos_produtos, min(num_produtos, len(todos_produtos)))

    layout_lancamentos = ft.Column(
        controls=[
            ft.Container(
               ft.Container(
                    col={"xs":0, "sm": 0, "md": 1}
               ), 
            ),
            ft.Container(
                content=ft.Text(
                    'Últimos Lançamentos',
                    size=26,
                    weight=ft.FontWeight.BOLD,
                    color="#000000"
                ),
                alignment=ft.alignment.center_left,
            ),
            criar_content_produtos(cards_de_produto(produtos_selecionados, on_atualizar=on_atualizar)),
        ],
        spacing=20
    )

    return ft.Container(
            content=layout_lancamentos,
            padding=ft.padding.only(left=20, top=0, right=20, bottom=20),
            alignment=ft.alignment.center,
            expand=True
    )

def sessao_promocoes(num_produtos=4, on_atualizar=None):
    todos_produtos = obter_todos_produtos()
    produtos_selecionados = random.sample(todos_produtos, min(num_produtos, len(todos_produtos)))

    for produto in produtos_selecionados:
        desconto = random.choice([0.25, 0.40, 0.50])
        produto['preco_promocional'] = round(produto['preco'] * (1 - desconto), 2)

    layout_promocoes = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text(
                    'Promoções Relâmpagos',
                    size=26,
                    weight=ft.FontWeight.BOLD,
                    color="#000000"
                ),
                alignment=ft.alignment.center_left,
            ),
            criar_content_produtos(cards_de_produto(produtos_selecionados, em_promocao=True, on_atualizar=on_atualizar)),
        ],
        spacing=20,
    )

    return ft.Container(
            content=layout_promocoes,
            padding=ft.padding.only(left=20, top=0, right=20, bottom=20),
            alignment=ft.alignment.center,
            expand=True
    )

def sessao_destaques(num_produtos=4, on_atualizar=None):
    todos_produtos = obter_todos_produtos()
    produtos_selecionados = random.sample(todos_produtos, min(num_produtos, len(todos_produtos)))

    layout_destaques = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text(
                    'Mais Populares',
                    size=26,
                    weight=ft.FontWeight.BOLD,
                    color="#000000",
                ),
                alignment=ft.alignment.center_left,
            ),
            criar_content_produtos(cards_de_produto(produtos_selecionados, on_atualizar=on_atualizar)),
        ],
        spacing=20,
    )

    return ft.Container(
            content=layout_destaques,
            padding=ft.padding.only(left=20, top=0, right=20, bottom=20),
            alignment=ft.alignment.center,
            expand=True
    )