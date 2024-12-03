import os
import webbrowser

def execute_action(action):
    if not action.startswith("AÇÃO:") or ";" not in action:
        return "Comando inválido ou mal formatado. Nenhuma ação realizada."
    
    try:
        action_type, details = action.replace("AÇÃO:", "", 1).split(";", 1)
        action_type = action_type.strip().lower()
        details = details.strip()
    except ValueError:
        return "Erro ao interpretar a ação. Nenhuma ação realizada."
    
    if action_type in ["abrir_navegador", "abrir navegador"]:
        if "url=" in details:
            url = details.split("url=", 1)[-1].strip()
            webbrowser.open(url)
            return f"Navegador aberto e acessando {url}."
        else:
            return "URL não especificado na ação. Nenhuma ação realizada."

    elif action_type in ["pesquisar_no_google", "pesquisar no google"]:
        if "query=" in details:
            query = details.split("query=", 1)[-1].strip()
            # Substituir espaços por "+" para formatação correta da URL
            query = query.replace(" ", "+")
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            return f"Navegador aberto com a busca: {query}."
        else:
            return "Query de busca não especificada. Nenhuma ação realizada."

    elif action_type == "Criar_pasta":
        folder_name = "test_folder/" + folder_name
        # Extração do nome da pasta
        if "nome=" in details:
            folder_name = details.split("nome=", 1)[-1].strip()
            os.makedirs(folder_name, exist_ok=True)
            return f"Pasta '{folder_name}' criada com sucesso."
        else:
            return "Nome da pasta não especificado. Nenhuma ação realizada."

    elif action_type == "Excluir_arquivo":
        folder_name = "test_folder/" + folder_name
        # Extração do nome do arquivo
        if "nome=" in details:
            file_name = details.split("nome=", 1)[-1].strip()
            try:
                os.remove(file_name)
                return f"Arquivo '{file_name}' excluído com sucesso."
            except FileNotFoundError:
                return f"Arquivo '{file_name}' não encontrado."
        else:
            return "Nome do arquivo não especificado. Nenhuma ação realizada."

    elif action_type == "Nenhuma ação":
        return "Comando não compreendido ou irrelevante para automação."

    # Ação desconhecida
    return "Ação desconhecida. Nenhuma ação realizada."
