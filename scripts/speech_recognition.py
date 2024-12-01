import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

def recognize_speech(input_audio_file):
    # Set device and data type
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # Model ID
    model_id = "openai/whisper-large-v3"

    # Load the model with specified settings
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)

    # Load the processor
    processor = AutoProcessor.from_pretrained(model_id)

    # Create the pipeline
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
    )

    # Process the audio file and recognize speech
    result = pipe(input_audio_file, generate_kwargs={"language": "portuguese"})
    recognized_text = result["text"]

    # Save the recognized text to a .txt file
    with open("recognized_text.txt", "w", encoding="utf-8") as file:
        file.write(recognized_text)
    
    print(f"Recognized text saved to 'recognized_text.txt'.")
    
    return recognized_text