import flet as ft

from dicionarios import produtos_organizados

def cards_produtos (lista_produtos: list):
    cards_de_produtos = []

    for produto in lista_produtos:
        if produto.get('imagem_url'):
            imagem_card = ft.Image(
                src=produto['imagem_url'],
                fit=ft.ImageFit.COVER,
                height=150,
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


