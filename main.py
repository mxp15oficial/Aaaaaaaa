import os
import requests
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# URL do servidor externo que você deseja buscar os dados
API_URL = os.getenv("SERVIDOR_EXTERNO_URL", "https://api.exemplo.com/dados")

# Token ou chave de autorização obtida de forma segura
AUTH_TOKEN = os.getenv("TOKEN_AUTORIZACAO", "seu_token_aqui")

def buscar_dados_servidor():
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        print(f"Conectando ao servidor: {API_URL}...")
        resposta = requests.get(API_URL, headers=headers)
        
        # Verifica se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            print("Dados obtidos com sucesso!")
            return resposta.json()
        else:
            print(f"Erro na requisição. Código de status: {resposta.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com o servidor: {e}")
        return None

if __name__ == "__main__":
    dados = buscar_dados_servidor()
    if dados:
        print(dados)
