from transformers import pipeline

def inference_text():
    # Open the file containing the prompt text and read its content
    with open("recognized_text.txt", "r", encoding="utf-8") as file:
        transcription = file.read().strip()

    messages = [
        {"role": "user", "content": transcription},
    ]
    pipe = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct")
    result = pipe(messages, max_new_tokens=100)
    print(result)