import flet as ft
from pathlib import Path

from dicionarios import produtos_organizados

def main(page: ft.Page):
    from ui_components import cards_produtos, criar_content_produtos, login_content, header_content, footer_content, navbar_content, hero_section_content
    
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

    login_tela = login_content(page)
    header = header_content(page, login_tela)
    navbar = navbar_content(page)
    hero_section = hero_section_content(page)
    
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

    footer = footer_content(page)

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