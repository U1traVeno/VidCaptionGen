from faster_whisper import WhisperModel

def transcribe_audio_to_txt(audio_file_path, output_file_path, model_size="large-v3", device="cuda", compute_type="float16", beam_size=5):
    """
    Transcribes audio to text and saves the output to a text file.

    Parameters:
    - audio_file_path (str): The path to the input audio file.
    - output_file_path (str): The path to the output text file.
    - model_size (str): The size of the Whisper model to use (default is "large-v3").
    - device (str): The device to use for computation ("cuda" or "cpu").
    - compute_type (str): The computation type ("float16", "int8_float16", etc.).
    - beam_size (int): The beam size for decoding (default is 5).

    Returns:
    - None
    """
    # Initialize the Whisper model
    model = WhisperModel(model_size, device=device, compute_type=compute_type)

    # Transcribe the audio
    segments, info = model.transcribe(audio_file_path, beam_size=beam_size)

    # Write the transcription to the output file
    with open(output_file_path, "w") as file:
        for segment in segments:
            file.write(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}\n")

    print(f"Transcription has been saved to '{output_file_path}'")
    
    # Example usage
    # transcribe_audio_to_txt("audio.mp3", "transcription_output.txt")

