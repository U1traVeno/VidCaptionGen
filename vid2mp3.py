import ffmpeg

def extract_mp3(input_mp4, output_mp3):
    """
    Extract audio from an mp4 file and save as an mp3 file.
    """
    try:
        # Run ffmpeg command to extract audio
        ffmpeg.input(input_mp4).output(output_mp3, format='mp3').run()
        print(f"Audio has been successfully extracted to '{output_mp3}'")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e}")

    # Example usage
    # extract_audio_from_video('video.mp4', 'audio.mp3')