import flet as ft

import home_page

def main(page: ft.Page):
    from ui_components import footer_content, navbar_content

    page.clean()
    page.title = 'Sobre Nós - FerramentaFácil Express'

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
                    "Sobre Nós - FerramentaFácil Express", 
                    style=ft.TextThemeStyle.HEADLINE_LARGE, 
                    text_align=ft.TextAlign.CENTER,
                    col={"xs": 12},
                    color='#FFFFFF',
                    weight=ft.FontWeight.BOLD
                ),
            ],
        ),
        bgcolor="#12D400",
        padding=ft.padding.only(top=20, bottom=20),
    )

    navbar = navbar_content(page)

    regiao_superior = ft.Container(
        ft.Column(
            [
                header, navbar
            ],
            spacing=0,
        ),
    )

    def about_us_content(title: str, body_text: str, image_src, imagem_a_esquerda: bool):
        text_content = ft.Column(
            [
                ft.Text(
                    title,
                    weight=ft.FontWeight.BOLD,
                    color='#000000',
                    size=36,
                ),
                ft.Container(height=20),
                ft.Text(
                    body_text,
                    color=ft.Colors.BLACK87,
                    size=16,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=10,
        )

        image_content = ft.Container(
            ft.Image(
                src=image_src,
                fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(10),
            ),
            alignment=ft.alignment.center,
        )

        if imagem_a_esquerda == True:
            conteudo_principal = [image_content, text_content]
            container_text_content = ft.Container(
                content=conteudo_principal[1],
                padding=ft.padding.only(left=20),
            )
            container_image_content = ft.Container(
                content=conteudo_principal[0],
                padding=ft.padding.only(right=20),
            )
        else:
            conteudo_principal = [text_content, image_content]
            container_text_content = ft.Container(
                content=conteudo_principal[0],
                padding=ft.padding.only(right=20),
            )
            container_image_content = ft.Container(
                content=conteudo_principal[1],
                padding=ft.padding.only(left=20),
            )
        
        content_row = ft.ResponsiveRow(
            [
                ft.Column(
                    [
                        container_text_content if not imagem_a_esquerda else container_image_content
                    ],
                    col={"xs": 12, "sm": 6},
                ),
                ft.Column(
                    [
                        container_image_content if not imagem_a_esquerda else container_text_content
                    ],
                    col={"xs": 12, "sm": 6},
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing={"sm": 40},
            run_spacing={"xs": 40},
        )

        section_content = ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Column(
                        [

                        ],
                        col={"xs": 0, "sm": 1},
                    ),
                    ft.Column(
                        [content_row],
                        col={"xs": 12, "sm": 10},
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        [

                        ],
                        col={"xs": 0, "sm": 1},
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(top=80, bottom=80, left=20, right=20),
        )

        return section_content

    secao_um = about_us_content(
        title='Sobre a Ferramenta Fácil Express',
        body_text='Bem-vindo à Ferramenta Fácil Express, a sua parceira de confiança no fornecimento de ferramentas de alta qualidade para todo o Brasil.\nNascemos com uma missão clara: descomplicar o acesso a ferramentas essenciais, garantindo que profissionais, entusiastas do "faça você mesmo" e grandes indústrias tenham em mãos exatamente o que precisam, onde quer que estejam no território nacional.',
        image_src='Flet - Loja Online Versão 1.3.8/assets/imagens/imagens_about_us/sobre_nos.png',
        imagem_a_esquerda=True,
    )

    secao_dois = about_us_content(
        title='O Brasil ao Alcance de Sua Mão',
        body_text='Entendemos que o sucesso de um projeto depende da qualidade e da disponibilidade imediata dos instrumentos certos. Por isso, a Ferramenta Fácil Express não se limita a um catálogo; somos uma solução logística e de suprimentos que garante:\n\n• Variedade e Qualidade: Oferecemos uma seleção rigorosa de ferramentas manuais, elétricas, hidráulicas e equipamentos de segurança das melhores marcas do mercado, priorizando a durabilidade e a performance.\n\n• Variedade e Qualidade: Oferecemos uma seleção rigorosa de ferramentas manuais, elétricas, hidráulicas e equipamentos de segurança das melhores marcas do mercado, priorizando a durabilidade e a performance.\n\n• Foco no Cliente: Nosso atendimento é especializado e pronto para auxiliar você a encontrar a solução perfeita para o seu desafio.',
        image_src='Flet - Loja Online Versão 1.3.8/assets/imagens/imagens_about_us/no_brasil.png',
        imagem_a_esquerda=False,
    )

    secao_tres = about_us_content(
        title='Nosso Compromisso',
        body_text='Mais do que vender ferramentas, nós entregamos potencial. Queremos ser o elo que conecta a sua necessidade ao equipamento ideal.\n\nCom a Ferramenta Fácil Express, a facilidade está no nome, e a qualidade, em cada entrega.\n\nConte conosco para equipar o seu trabalho, seja ele qual for, com agilidade e segurança, sem sair de casa ou do canteiro de obras.',
        image_src='Flet - Loja Online Versão 1.3.8/assets/imagens/imagens_about_us/nosso_compromisso.png',
        imagem_a_esquerda=True,
    )

    secao_quatro = about_us_content(
        title='Nossa Missão',
        body_text='Fornecer, com facilidade e agilidade, as melhores ferramentas e equipamentos para todo o território brasileiro, garantindo o sucesso e a segurança dos projetos de nossos clientes, desde o pequeno reparo até a grande obra.',
        image_src='Flet - Loja Online Versão 1.3.8/assets/imagens/imagens_about_us/nossa_missao.png',
        imagem_a_esquerda=False,
    )

    secao_cinco = about_us_content(
        title='Nossa Visão',
        body_text='Ser reconhecida como a plataforma líder e mais confiável do Brasil na distribuição de ferramentas, destacando-se pela excelência logística, variedade do catálogo e pelo atendimento que simplifica a vida de nossos clientes.',
        image_src='Flet - Loja Online Versão 1.3.8/assets/imagens/imagens_about_us/nossa_visao.png',
        imagem_a_esquerda=True,
    )

    secao_seis = about_us_content(
        title='Nossos Valores',
        body_text='• Facilidade no Acesso: Tornar a compra e a entrega de ferramentas um processo simples e desburocratizado.\n• Compromisso com o Cliente: Focar na satisfação plena, oferecendo suporte especializado e soluções rápidas.\n• Qualidade e Confiabilidade: Trabalhar apenas com produtos de alta performance e marcas que inspiram confiança.\n• Abrangência Nacional: Honrar nosso compromisso de levar soluções a todos os cantos do Brasil, com responsabilidade e pontualidade.',
        image_src='Flet - Loja Online Versão 1.3.8/assets/imagens/imagens_about_us/nossos_valores.png',
        imagem_a_esquerda=False,
    )

    footer = footer_content(page) 

    page.add(
        ft.Column(
            [
                regiao_superior,
                secao_um,
                secao_dois,
                secao_tres,
                secao_quatro,
                secao_cinco,
                secao_seis,
                footer,
            ],
        ),
    )

    page.update()

if __name__ == '__main__':
    ft.app(main, assets_dir="assets")