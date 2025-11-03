import flet as ft

from dicionarios import equipe_dados

from ui_components import footer_content

def main(page: ft.Page):
    page.clean()
    page.title = 'As Mentes por Trás da Eficiência - FerramentaFácil Express'

    page.fonts = {
        "Open Sans": "fonts/OpenSans-Regular.ttf",        
    }
    page.window.maximized = True 
    page.window.width = None
    page.window.height = None

    page.bgcolor = "#FFFFFF"
    page.scroll = ft.ScrollMode.AUTO

    header = ft.Container(
        ft.Column(
            [
                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Text(
                                'Membros da Nossa Equipe',
                                color="#000000",
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextThemeStyle.HEADLINE_LARGE, 
                                font_family='Open Sans',
                                text_align=ft.TextAlign.CENTER,
                                col={"xs": 12},
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    bgcolor='#F2FF00',
                    padding=ft.padding.only(top=20, bottom=20)
                ),

                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Text(
                                'Conheça as pessoas que tornaram esse projeto possível. O motor por trás da criação, demonstrando competência, consistência e trabalho em conjunto.',
                                color='#FFFFFF',
                                weight=ft.FontWeight.BOLD,
                                size=15,
                                text_align=ft.TextAlign.CENTER,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        col={"xs": 0, "lg": 12},
                    ),
                    bgcolor='#102739',
                    padding=ft.padding.only(top=20, bottom=20),
                    shadow=ft.BoxShadow(
                        color='#102739',
                        blur_radius=10,
                    )
                ),
            ],
            spacing=0,
        ),
        padding=ft.padding.only(bottom=3),
    )

    cards_equipe = []
    for membro, infos in equipe_dados.items():
        card = ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        ft.Image(
                            src=infos['imagem'], 
                            fit=ft.ImageFit.CONTAIN
                        ),
                        width=260,
                        height=240,
                        border_radius=10,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    ),
                    ft.Column(
                        [

                        ],
                    ),
                    ft.Text(
                        infos['nome'],
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        infos['e-mail'],
                        size=13,
                        color="#6FCF97",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        infos['frase'],
                        size=13,
                        color='#BBBBBB',
                        italic=True,
                        text_align=ft.TextAlign.CENTER,
                    ),

                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.FACEBOOK,
                                tooltip=ft.Tooltip(
                                    message=infos['facebook']
                                ),
                                icon_color='#BBBBBB',
                                icon_size=18,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SHARE,
                                tooltip=ft.Tooltip(
                                    message=infos['github']
                                ),
                                icon_color='#BBBBBB',
                                icon_size=18,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.PHONE,
                                tooltip=ft.Tooltip(
                                    message=infos['telefone']
                                ),
                                icon_color='#BBBBBB',
                                icon_size=18,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.GROUP,
                                tooltip=ft.Tooltip(
                                    message=infos['funcao']
                                ),
                                icon_color='#BBBBBB',
                                icon_size=18,
                            ),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=7,
            ),
            bgcolor="#7E7B7B", 
            padding=ft.padding.all(20),
            border_radius=10,
            shadow=ft.BoxShadow(
                color="#000000",
                blur_radius=11, 
                spread_radius=2, 
                offset=ft.Offset(0, 4)
            ),
            col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
            margin=ft.margin.symmetric(horizontal=12, vertical=10),
            width=260,
            height=450,
        )
        cards_equipe.append(card)

    container_cards_equipe = ft.ResponsiveRow(
        controls=cards_equipe,
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )
    
    footer = footer_content(page)

    page.add(
        ft.Column(
            [
                header,
                ft.Divider(thickness=3, color="#000000"),
                container_cards_equipe,
                footer,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")