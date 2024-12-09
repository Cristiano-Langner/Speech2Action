import os
import webbrowser

def execute_action(action):
    # Check the basic format of the action
    if not action.startswith("AÇÃO:") or ";" not in action:
        return "Comando inválido ou mal formatado. Nenhuma ação realizada."

    # Split the command into action type and details
    try:
        tipo_acao, detalhes = action[5:].split(";", 1)  # Remove "AÇÃO:" e divide por ";"
    except ValueError:
        return "Comando mal formatado. Nenhuma ação realizada."

    # Normalizes data to avoid capitalization issues
    tipo_acao = tipo_acao.strip().lower()
    detalhes = detalhes.strip()

    # Identifies and executes specific actions
    if tipo_acao == "criar_pasta":
        folder_name = detalhes.split("=")[-1]
        return create_folder(folder_name)
    elif tipo_acao == "abrir_navegador":
        url = detalhes.split("=")[-1]
        return open_browser(url)
    elif tipo_acao == "responder_pergunta":
        return detalhes
    else:
        return "Ação não reconhecida ou inválida."
# Creates a folder in the current directory
def create_folder(folder_name):
    try:
        if not folder_name:
            return "Nome da pasta não fornecido. Ação não realizada."
        os.makedirs(folder_name, exist_ok=True)
        return f"Pasta '{folder_name}' criada com sucesso."
    except Exception as e:
        return f"Erro ao criar pasta: {e}"

# Opens a browser with the given URL
def open_browser(url):
    try:
        if not url:
            return "URL não fornecida. Ação não realizada."
        webbrowser.open(url)
        return f"Navegador aberto com a URL: {url}"
    except Exception as e:
        return f"Erro ao abrir o navegador: {e}"