from supabase import create_client, Client

# Configurações do Supabase
SUPABASE_URL = "https://htyclsojvonggdesvcin.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh0eWNsc29qdm9uZ2dkZXN2Y2luIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjY5MjA1MzUsImV4cCI6MjA4MjQ5NjUzNX0.Zl4qSI8XvWn6X9IS7PcIs-18kl5H526UvAfD0SkoSJ4"  # Use a 'service_role' ou 'anon key' do seu painel

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_produtos_organizados():
    try:
        response = supabase.table("produtos").select("*").execute()

        lista_produtos = response.data

        produtos_organizados = {}

        for produto in lista_produtos:
            produto_mapeado = {
                'id': produto['id'],
                'nome': produto['nome'],
                'marca': produto['marca'],
                'descricao': produto['descricao'],
                'preco': float(produto['preco']), 
                'estoque': produto['estoque'],
                'imagem_url': produto['image_url'],
                'categoria': produto.get('categoria', 'Outros'),
            }

            categoria = p['categoria']
            if categoria not in produtos_organizados:
                produtos_organizados[categoria] = []
            
            produtos_organizados[categoria].append(produto_dict)

        return produtos_organizados

    except Exception as e:
        print(f"Erro ao buscar dados no Supabase: {e}")
        return {}

def buscar_produtos_do_banco():
    try:
        response = supabase.table("produtos").select("*").execute()
        produtos = response.data
        
        produtos_organizados = {}
        for produto in produtos:
            categoria = produto.get('categoria', 'Outros')  
            if categoria not in produtos_organizados:
                produtos_organizados[categoria] = []
            produtos_organizados[categoria].append(produto)
        return produtos_organizados
    except Exception as e:
        print(f"Erro ao buscar produtos: {e}")
        return {}  

def obter_todos_produtos():
    produtos_organizados = buscar_produtos_do_banco()  
    todos_produtos = []
    for categoria in produtos_organizados.values():
        todos_produtos.extend(categoria)
    return todos_produtos

def comprar_produto(produto_id):
    try:
        response = supabase.table("produtos").select("estoque").eq("id", produto_id).single().execute()
        produto = response.data

        if produto and produto['estoque'] > 0:
            novo_estoque = produto['estoque'] - 1
            supabase.table("produtos").update({"estoque": novo_estoque}).eq("id", produto_id).execute()
            print(f"Produto {produto_id} comprado com sucesso! Novo estoque: {novo_estoque}")
        else:
            print(f"Produto {produto_id} está fora de estoque ou não encontrado.")

    except Exception as e:
        print(f"Erro ao processar a compra: {e}")


# Área de Teste
if __name__ == "__main__":
    print("Conectando ao Supabase e buscando produtos...")
    resultado = buscar_produtos_organizados()
    
    if resultado:
        print("Sucesso! Produtos recuperados.")
        primeira_cat = list(resultado.keys())[0]
        print(f"Categoria: {primeira_cat}")
        print(f"Primeiro produto: {resultado[primeira_cat][0]['nome']}")
    else:
        print("Nenhum dado encontrado ou erro na conexão.")