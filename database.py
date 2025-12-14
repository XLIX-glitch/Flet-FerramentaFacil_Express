import flet as ft
import psycopg2
from psycopg2 import OperationalError

DB_NAME = "ferramenta_facil_express_db"
DB_USER = "ferramenta_facil_express_db_user"
DB_PASSWORD = "Vy2RfJZX1cy4nC7hFFaMpEIykGzNwCDA"
DB_HOST = "dpg-d4ji8d24d50c73cmjer0-a.oregon-postgres.render.com"
DB_PORT = "5432"

def criar_conexao():
    connection = None
    try:
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexão bem-sucedida ao banco de dados PostgreSQL")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu ao tentar conectar ao banco de dados")
    return connection

if __name__ == "__main__":
    conexao = criar_conexao()
    if conexao:
        conexao.close()
        print("Conexão fechada.")
    else:
        print("Falha ao estabelecer conexão.")

def buscar_produtos_organizados():
    conexao = criar_conexao()
    
    if conexao is None:
        print("Não foi possível conectar para buscar produtos.")
        return {}

    produtos_organizados = {}

    try:
        cursor = conexao.cursor()
        
        query = """
            SELECT id, nome, marca, categoria, descricao, preco, estoque, image_url 
            FROM produtos
        """
        cursor.execute(query)
        linhas = cursor.fetchall()

        for linha in linhas:
            
            p_id, p_nome, p_marca, p_categoria, p_descricao, p_preco, p_estoque, p_img_url = linha

            produto_dict = {
                'id': p_id,
                'nome': p_nome,
                'marca': p_marca,
                'descricao': p_descricao,
                'preco': float(p_preco), 
                'estoque': p_estoque,
                'imagem_url': p_img_url 
            }

            if p_categoria not in produtos_organizados:
                produtos_organizados[p_categoria] = []
            
            produtos_organizados[p_categoria].append(produto_dict)

        cursor.close()
        conexao.close()
        return produtos_organizados

    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        if conexao:
            conexao.close()
        return {}

if __name__ == "__main__":
    print("Testando busca de produtos...")
    resultado = buscar_produtos_organizados()
    
    if resultado:
        print("Sucesso! Produtos recuperados.")

        primeira_cat = list(resultado.keys())[0]
        print(f"Categoria: {primeira_cat}")
        print(f"Primeiro produto: {resultado[primeira_cat][0]['nome']}")
        print(f"URL da imagem: {resultado[primeira_cat][0]['imagem_url']}")
    else:
        print("O dicionário retornou vazio. Verifique a conexão ou se há dados na tabela.")