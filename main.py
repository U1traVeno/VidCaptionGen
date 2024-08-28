from faster_whisper_model import transcribe_audio_to_txt
import txt2srt
import vid2mp3

mode_num = input(int("Choose mode(Chinese:1, English:2, Bilingual:3): "))
if mode_num == 1:
    mode = 'chinese'
elif mode_num == 2:
    mode = 'english'
elif mode_num == 3:
    mode = 'bilingual'
else:
    raise ValueError("Invalid mode.")

    


