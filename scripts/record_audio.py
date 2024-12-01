import pyaudio
from pydub import AudioSegment

def record_audio(output_mp3_file, duration):
    """
    Records audio from the microphone and saves it as an MP3 file.
    
    :param output_mp3_file: Name of the MP3 file to save
    :param duration: Recording duration in seconds
    """
    audio_format = pyaudio.paInt16  # Audio format (16-bit PCM)
    channels = 1                    # Number of channels (mono)
    sample_rate = 44100             # Sampling rate (44.1 kHz)
    buffer_size = 1024              # Audio buffer size

    audio = pyaudio.PyAudio()

    # Audio stream configuration
    stream = audio.open(format=audio_format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=buffer_size)

    print("Recording...")
    frames = []

    # Audio capture
    for _ in range(0, int(sample_rate / buffer_size * duration)):
        data = stream.read(buffer_size)
        frames.append(data)

    print("Recording finished.")

    # Closing the stream and PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Convert audio bytes to a format usable by pydub
    audio_bytes = b''.join(frames)
    audio_segment = AudioSegment(
        data=audio_bytes,
        sample_width=audio.get_sample_size(audio_format),
        frame_rate=sample_rate,
        channels=channels
    )

    # Save directly as MP3
    audio_segment.export(output_mp3_file, format="mp3")
    print(f"MP3 file saved as {output_mp3_file}.")