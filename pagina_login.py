import flet as ft
import pyrebase

firebaseConfig = { 
  'apiKey': 'AIzaSyCBTuS458t2fEOwSVaXDQgvy6Ufd7fV5vI',
  'authDomain': 'ferramentafacil-express.firebaseapp.com',
  'projectId': 'ferramentafacil-express',
  'storageBucket': 'ferramentafacil-express.firebasestorage.app',
  'databaseURL': 'https://ferramentafacil-express.firebaseio.com',
  'messagingSenderId': '204295788549',
  'appId': '1:204295788549:web:38703bfc435255aec1e46c',
  'measurementId': 'G-H8QYNETWQL'
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def main(page: ft.Page):
    modo_login = True
    
    titulo_texto = ft.Text(
        value='Login',
        size=32,
        weight=ft.FontWeight.BOLD,
        color="#FFFFFF",
    )

    usuario = ft.TextField(
        hint_text='Email',
        label='Email',
        width=280,
        border_color="#FFFFFF",
        color="#FFFFFF",
        label_style=ft.TextStyle(
            color="#FFFFFF"
        ),
    )
    
    senha = ft.TextField(
        hint_text='Senha',
        label='Senha',
        width=280,
        border_color="#FFFFFF",
        color="#FFFFFF",
        label_style=ft.TextStyle(color="#FFFFFF"),
        password=True,
        can_reveal_password=True,
    )
    
    botao_principal = ft.ElevatedButton(
        text='Entrar',
        color="#000000",
        bgcolor="#FFF6F6",
        width=280,
        height=40,
        on_click=lambda e: btn_action(e)
    )

    link_cadastro = ft.TextButton(
        text='Ainda não tem uma conta? Cadastre-se!',
        style=ft.ButtonStyle(
            color="#FFFFFF",
        ),
        on_click=lambda e: toggle_mode(e)
    )
    
    def toggle_mode(e):
        nonlocal modo_login
        modo_login = not modo_login
        if modo_login:
            titulo_texto.value = 'Login'
            botao_principal.text = 'Entrar'
            link_cadastro.text = 'Ainda não tem uma conta? Cadastre-se!'
        else:
            titulo_texto.value = 'Cadastrar-se'
            botao_principal.text = 'Cadastrar-se'
            link_cadastro.text = 'Já tem uma conta? Faça login!'
        page.update()
    
    def btn_action(e):
        user_email = usuario.value
        user_password = senha.value
        
        if modo_login:
            try:
                auth.sign_in_with_email_and_password(user_email, user_password)
                print('Login bem-sucedido!')  
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            'Logado com sucesso!',
                            color="#FFFFFF",
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#09FF00",
                        action='OK',
                        action_color="#FFFFFF",
                        duration=3000,
                    )
                )
                usuario.value = ""
                senha.value = ""

                page.close(login_page)

            except Exception as ex:
                print(f'Erro de login: {ex}')
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            'Email ou senha inválidos',
                            color='#FFFFFF',
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#FF0000",
                        action='OK',
                        action_color='#FFFFFF',
                        duration=3000,
                    )
                )
                usuario.value = ""
                senha.value = ""
        else:
            try:
                auth.create_user_with_email_and_password(user_email, user_password)
                print('Cadastro bem-sucedido!')  
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            'Conta criada com sucesso!',
                            color="#3C3C3C",
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#09FF00",
                        action='OK',
                        action_color="#3C3C3C",
                        duration=3000,
                    )
                )
                usuario.value = ""
                senha.value = ""

                page.close(login_page)

            except Exception as ex:
                print(f'Erro de cadastro: {ex}')
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            'Erro ao criar conta (email já existe ou inválido)',
                            color="#FFFFFF",
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#FF0000",
                        action='OK',
                        action_color="#FFFFFF",
                        duration=3000,
                    )
                )
                usuario.value = ""
                senha.value = ""

    login_page = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column(
                [
                    titulo_texto,
                    usuario,
                    senha,
                    botao_principal,
                    link_cadastro,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            height=450,  
            width=350,
            bgcolor="#000000", 
            padding=20,
        ), 
        modal=True,
        bgcolor="#000000",
    )
    
    return login_page