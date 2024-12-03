from transformers import pipeline

def inference_text():
    inicial_prompt = (
        "Você é um assistente especializado em automação de tarefas no computador. "
        "Responda no formato estrito: `AÇÃO: [tipo_de_ação];[detalhes]`. "
        "Se não entender o comando, diga: `AÇÃO: Nenhuma ação.`\n\n"
        "Exemplos:\n"
        "Usuário: Criar uma pasta chamada 'Documentos'.\n"
        "Resposta: AÇÃO: Criar_pasta;nome=Documentos\n\n"
        "Usuário: Abrir o site google.com no navegador.\n"
        "Resposta: AÇÃO: Abrir_navegador;url=https://google.com\n\n"
        "Usuário: Excluir o arquivo 'teste.txt'.\n"
        "Resposta: AÇÃO: Excluir_arquivo;nome=teste.txt\n\n"
    ) 
    
    # Open the file containing the prompt text and read its content
    with open("recognized_text.txt", "r", encoding="utf-8") as file:
        transcription = file.read().strip()
    
    input_text = f"{inicial_prompt}\nComando do usuário: {transcription}\nResposta:"

    pipe = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct")
    result = pipe(input_text, max_new_tokens=150)
    
    generated_text = result[0]["generated_text"]
    action = generated_text.split("Resposta:")[-1].strip()
    
    return action