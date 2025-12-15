import flet as ft
from pathlib import Path

def main(page: ft.Page):
    from ui_components import header_content, footer_content, navbar_content, hero_section_content
    from ui_components import sessao_destaques, sessao_lancamentos, sessao_promocoes
    
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
    
    def sessao_avaliacoes(page):
        avaliacoes = [
            ('Carlos Manoel', 'A entrega foi muito rápida e o processo de compra no site foi simples e intuitivo, adorei a experiência!', 5),
            ('Emanuelle Souza', 'O visual do site é moderno, bem estruturado e transmite profissionalismo. Dá vontade de olhar cada canto.', 5),
            ('Vinícius Carvalho', 'Achei o preço justo pelo desempenho e qualidade. A relação custo-benefício me surprendeu.', 4),
            ('Lucas Almeida', 'Gostei muito da organização das informações, encontrei o que precisava em poucos cliques.', 5)
        ]

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

        def hover_sombra(e):
            e.control.shadow = hover_shadow if e.data == "true" else normal_shadow
            e.control.update()

        cards_avaliacoes = []
        for nome, comentario, nota in avaliacoes:
            estrelas = ft.Row(
                [ft.Icon(name=ft.Icons.STAR, color="#FFEA00") for _ in range(nota)] +
                [ft.Icon(name=ft.Icons.STAR_BORDER, color="#CCCCCC") for _ in range(5 - nota)],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=2
            )

            conteudo = ft.Container(
                content=ft.Column(
                    [
                        estrelas,
                        ft.Text(
                            f'{comentario}', 
                            italic=True,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            f'- {nome}',
                            color="#777777",
                            size=12,
                        ),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor='#FFFFFF',
                border_radius=10,
                padding=15,
                shadow=normal_shadow,
                on_hover=hover_sombra,
                col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
            )
            
            cards_avaliacoes.append(conteudo)

        layout = ft.Column(
            [
                ft.Container(
                    ft.Text(
                        'Comentários dos Clientes',
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="#000000",
                    ),
                    alignment=ft.alignment.center_left,      
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Column(
                                []
                            ),
                            col={"xs": 0, "sm": 0, "md": 1, "lg": 1},
                        ),

                        ft.Container(
                            ft.ResponsiveRow(
                                cards_avaliacoes,
                                alignment=ft.MainAxisAlignment.CENTER,
                                run_spacing=15,
                                spacing=15,
                            ),
                            col={"xs": 12, "sm": 12, "md": 10, "lg": 10},
                        ),

                        ft.Container(
                            ft.Column(
                                []
                            ),
                            col={"xs": 0, "sm": 0, "md": 1, "lg": 1},
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        return ft.Container(
            content=layout,
            padding=ft.padding.only(left=20, top=0, right=20, bottom=20),
            alignment=ft.alignment.center,
            expand=True
        )

    header = header_content(page)
    navbar = navbar_content(page)
    hero_section = hero_section_content(page)

    sessao_mais_populares = sessao_destaques()
    sessao_ultimos_lancamentos = sessao_lancamentos()
    sessao_promocoes_relampagos = sessao_promocoes()

    sessao_comentarios = sessao_avaliacoes(page)

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
        height=500,
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
                        message='Anterior',
                    ),
                    icon_color='#FF5100',
                    icon_size=40,
                    on_click=previous_image,
                ),
                ft.IconButton(
                    icon=ft.Icons.CHEVRON_RIGHT,
                    tooltip=ft.Tooltip(
                        message='Próximo',
                    ),
                    icon_color='#FF5100',
                    icon_size=40,
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

    footer = footer_content(page)

    juntar_header = ft.Column(
        [header, navbar, hero_section],
        spacing=0
    )

    page.add(
        ft.Column(
            [
                juntar_header,
                ft.Divider(thickness=1, height=20, color="#8F000000"),
                carousel,
                ft.Column(
                    controls=[
                        sessao_mais_populares,
                        
                        sessao_ultimos_lancamentos,
                        
                        sessao_promocoes_relampagos,
                        
                        sessao_comentarios,
                    ],
                    spacing=50,
                ),
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