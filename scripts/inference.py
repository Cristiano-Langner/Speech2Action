from transformers import pipeline

def inference_text():
    inicial_prompt = (
    "Você é um assistente especializado em automação de tarefas no computador.\n"
    "Responda sempre no formato estrito: AÇÃO:[tipo_de_ação];[detalhes].\n"
    "Se não entender o comando ou for uma ação inválida, diga: AÇÃO:Nenhuma_ação.\n"
    "As únicas ações válidas são: Criar_pasta, Abrir_navegador, Responder_pergunta.\n"
    "Exemplo:\n"
    "Comando do usuário: Crie uma pasta chamada Teste.\n"
    "Resposta: AÇÃO:Criar_pasta;nome=Teste\n"
    "Comando do usuário: Abra o navegador no site google.com.\n"
    "Resposta: AÇÃO:Abrir_navegador;url=https://google.com\n"
    "Comando do usuário: Quantos segundos tem um minuto?\n"
    "Resposta: AÇÃO:Responder_pergunta;Um minuto tem 60 segundos.\n"
    "Comando do usuário: \n"
    "Resposta: AÇÃO:Nenhuma_ação\n"
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