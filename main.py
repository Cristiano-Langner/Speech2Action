from scripts.record_audio import record_audio
from scripts.speech_recognition import recognize_speech
from scripts.inference import inference_text
from scripts.actions import execute_action
import warnings
import logging

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning)  # To ignore user warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)  # To ignore deprecation warnings
warnings.filterwarnings("ignore", category=FutureWarning)  # To ignore future warnings
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("torch").setLevel(logging.ERROR)

def main():
    try:
        while True:
            # Step 1: Record audio from microphone and save as MP3
            print("---------------------------------------------------")
            print("Starting audio recording...")
            output_file = "recording.mp3"
            record_duration = 5  # duration of the recording in seconds
            record_audio(output_file, duration=record_duration)
            print("\n")

            # Step 2: Process the recorded audio and recognize speech
            print("Starting speech recognition...")
            speech_text = recognize_speech(output_file)
            print(f"Recognized speech: {speech_text}")
            print("\n")
            
            # Step 3: Inference the recognized text
            print("Starting inference...")
            action = inference_text()
            print(f"Inference text: {action}")
            print("\n")
            
            # Step 4: Performing actions
            print("Performing action...")
            result = execute_action(action)
            print(f"Result: {result}")

            # Ask the user if they want to continue or stop
            user_input = input("Do you want to record again? (y/n): ").strip().lower()
            print("\n")

            if user_input != 'y':
                print("Exiting the program.")
                break  # Exit the loop and stop the program
            
    except KeyboardInterrupt:
        print("\nInterrupted by user. Ending the program.")
        
if __name__ == "__main__":
    main()