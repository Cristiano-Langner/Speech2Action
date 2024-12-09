import os
import webbrowser

def execute_action(action):
    # Verifica o formato básico da ação
    if not action.startswith("AÇÃO:") or ";" not in action:
        return "Comando inválido ou mal formatado. Nenhuma ação realizada."
    
    # Divide o comando em tipo de ação e detalhes
    try:
        tipo_acao, detalhes = action[5:].split(";", 1)  # Remove "AÇÃO:" e divide por ";"
    except ValueError:
        return "Comando mal formatado. Nenhuma ação realizada."

    # Normaliza os dados para evitar problemas de capitalização
    tipo_acao = tipo_acao.strip().lower()
    detalhes = detalhes.strip()

    # Identifica e executa ações específicas
    if tipo_acao == "criar_pasta":
        folder_name = detalhes.split("=")[-1]
        return create_folder(folder_name)
    elif tipo_acao == "abrir_navegador":
        url = detalhes.split("=")[-1]
        return open_browser(url)
    elif tipo_acao == "responder_pergunta":
        return detalhes  # Apenas retorna a resposta
    else:
        return "Ação não reconhecida ou inválida."

def create_folder(folder_name):
    """
    Cria uma pasta no diretório atual.
    """
    try:
        if not folder_name:
            return "Nome da pasta não fornecido. Ação não realizada."
        os.makedirs(folder_name, exist_ok=True)
        return f"Pasta '{folder_name}' criada com sucesso."
    except Exception as e:
        return f"Erro ao criar pasta: {e}"

def open_browser(url):
    """
    Abre um navegador com a URL fornecida.
    """
    try:
        if not url:
            return "URL não fornecida. Ação não realizada."
        webbrowser.open(url)
        return f"Navegador aberto com a URL: {url}"
    except Exception as e:
        return f"Erro ao abrir o navegador: {e}"
