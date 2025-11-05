import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated")
warnings.filterwarnings("ignore", category=UserWarning, module="gcloud")

import flet as ft
import pyrebase

firebaseConfig = { 
  'apiKey': "AIzaSyCBTuS458t2fEOwSVaXDQgvy6Ufd7fV5vI",
  'authDomain': "ferramentafacil-express.firebaseapp.com",
  'projectId': "ferramentafacil-express",
  'storageBucket': "ferramentafacil-express.firebasestorage.app",
  'databaseURL': "https://ferramentafacil-express.firebaseio.com",
  'messagingSenderId': "204295788549",
  'appId': "1:204295788549:web:38703bfc435255aec1e46c",
  'measurementId': "G-H8QYNETWQL"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 20
    
    is_login_mode = True
    
    titulo_texto = ft.Text(
        value="Login",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE
    )

    usuario = ft.TextField(
        hint_text="Email",
        label="Email",
        width=280,
        border_color=ft.Colors.WHITE,
        color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE)
    )
    
    senha = ft.TextField(
        hint_text="Senha",
        label="Senha",
        width=280,
        border_color=ft.Colors.WHITE,
        color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        password=True,
        can_reveal_password=True
    )
    
    botao_principal = ft.ElevatedButton(
        text="Entrar",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLACK,
        width=280,
        height=40,
        on_click=lambda e: btn_action(e)
    )

    link_cadastro = ft.TextButton(
        text="Ainda não tem uma conta? Cadastre-se!",
        on_click=lambda e: toggle_mode(e)
    )
    
    def toggle_mode(e):
        nonlocal is_login_mode
        is_login_mode = not is_login_mode
        if is_login_mode:
            titulo_texto.value = "Login"
            botao_principal.text = "Entrar"
            link_cadastro.text = "Ainda não tem uma conta? Cadastre-se!"
        else:
            titulo_texto.value = "Cadastrar-se"
            botao_principal.text = "Cadastrar"
            link_cadastro.text = "Já tem uma conta? Faça login!"
        page.update()
    
    def btn_action(e):
        user_email = usuario.value
        user_password = senha.value
        
        if is_login_mode:
            
            try:
                auth.sign_in_with_email_and_password(user_email, user_password)
                print("Login bem-sucedido!")  
                
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            "Logado com sucesso!",
                            color="#3C3C3C",
                            weight=ft.FontWeight.BOLD,
                            ),
                        bgcolor="#09FF00",
                        action="OK",
                        action_color="#3C3C3C",
                        duration=3000,
                    )
                )
                
                usuario.value = ""
                senha.value = ""
                
            except Exception as ex:
                print(f"Erro de login: {ex}")
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            "Email ou senha inválidos",
                            color="#FFFFFF",
                            weight=ft.FontWeight.BOLD,
                            ),
                        bgcolor="#FF0000",
                        action="OK",
                        action_color="#FFFFFF",
                        duration=3000,
                    )
                )
                
                usuario.value = ""
                senha.value = ""
                
        else:

            try:
                auth.create_user_with_email_and_password(user_email, user_password)
                print("Cadastro bem-sucedido!")  
                
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            "Conta criada com sucesso!",
                            color="#3C3C3C",
                            weight=ft.FontWeight.BOLD,
                            ),
                        bgcolor="#09FF00",
                        action="OK",
                        action_color="#3C3C3C",
                        duration=3000,
                    )
                )
                
                usuario.value = ""
                senha.value = ""
                
            except Exception as ex:
                print(f"Erro de cadastro: {ex}")
                page.open(
                    ft.SnackBar(
                        content=ft.Text(
                            "Erro ao criar conta (email já existe ou inválido)",
                            color="#FFFFFF",
                            weight=ft.FontWeight.BOLD,
                            ),
                        bgcolor="#FF0000",
                        action="OK",
                        action_color="#FFFFFF",
                        duration=3000,
                    )
                )
                
                usuario.value = ""
                senha.value = ""

        page.update()

    page.add(
        titulo_texto,
        usuario,
        senha,
        botao_principal,
        link_cadastro
    )

if __name__ == "__main__":
    ft.app(target=main)