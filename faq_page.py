import flet as ft

from dicionarios import faq_informacoes

from ui_components import navbar_content, footer_content

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

    navbar_faq = navbar_content(page)

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

    footer_faq = footer_content(page)

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