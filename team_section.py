import flet as ft

import home_page
from dicionarios import equipe_dados

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
                                'MEMBROS DA NOSSA EQUIPE',
                                color="#575757",
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
                    padding=ft.padding.only(top=20, bottom=20)
                ),
            ],
            spacing=0,
        ),
        padding=ft.padding.only(bottom=3),
    )

    cards_equipe = []
    for membro, infos in equipe_dados.items():
        cards_equipe.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.CircleAvatar(
                            foreground_image_src=infos['imagem'],
                            radius=50,
                        ),
                        ft.Text(
                            infos['nome'],
                            weight=ft.FontWeight.BOLD,
                            color="#000000",
                            size=16,
                        ),
                        ft.Text(
                            infos['funcao'],
                            weight=ft.FontWeight.BOLD,
                            color='#DD6E15',
                            size=14,
                        ),
                        ft.Text(
                            infos['frase'],
                            size=13,
                            italic=True,
                            color='#000000',
                        ),
                        ft.Text(
                            infos['telefone'],
                            size=13,
                            color='#000000',
                        ),
                        ft.Text(
                            infos['e-mail'],
                            size=13,
                            color='#000000',
                        ),
                        ft.Text(
                            infos['github'],
                            size=13,
                            color='#000000',
                        ),
                    ],
                    height=370,
                    run_spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    
                ),
                bgcolor="#FFFFFF",
                border_radius=8,
                shadow=ft.BoxShadow(blur_radius=3),
                padding=ft.padding.all(10),
                col={"xs": 12, "sm": 6, "md": 6, "lg": 4},
                margin=ft.margin.only(left=30, right=30, bottom=10)
            ),
        )

        container_cards_equipe = ft.ResponsiveRow(
            cards_equipe,
            spacing=20,
            run_spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    botao_retornar = ft.Container(
        ft.ResponsiveRow(
            [
                ft.ElevatedButton(
                    'RETORNAR AO MENU', 
                    on_click=lambda e: home_page.main(page),
                    bgcolor="#102739",
                    width=150,
                    height=50,
                    col={"xs": 12, "sm": 6, "md": 4, "lg": 2} 
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.add(
        ft.Column(
            [
                header,
                ft.Divider(thickness=3, color="#000000"),
                container_cards_equipe,
                botao_retornar,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")