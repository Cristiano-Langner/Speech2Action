from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch

# Initialize the TTS pipeline
synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

# Load the speaker embedding
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

# Reads the text from the file response_text.txt
try:
    with open("response_text.txt", "r", encoding="utf-8") as file:
        text_to_speak = file.read().strip()
        if not text_to_speak:
            raise ValueError("O arquivo está vazio. Adicione algum texto para ser sintetizado.")
except FileNotFoundError:
    print("Arquivo 'response_text.txt' não encontrado.")
    text_to_speak = "O arquivo de texto não foi encontrado. Por favor, verifique se ele existe no diretório."
except ValueError as e:
    print(e)
    text_to_speak = "O arquivo está vazio. Adicione algum texto para ser sintetizado."

# Performs speech synthesis
speech = synthesiser("Hello, my dog is cooler than you!", forward_params={"speaker_embeddings": speaker_embedding})

# Save the generated audio to a WAV file
sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])