import os
from tqdm import tqdm

from faster_whisper_model import transcribe_audio_to_txt
from txt2srt import rename_txt2srt, format2srt, test_translate
from vid2mp3 import extract_mp3

# 文件夹路径
mp4_folder = 'mp4_files'
mp3_folder = 'mp3_files'
txt_folder = 'txt_files'
srt_folder = 'srt_files'

# 创建文件夹（如果不存在）
folders = [mp4_folder, mp3_folder, txt_folder, srt_folder]
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 模式选择
mode_num = int(input("Choose mode (txt to srt:1, mp4 to txt:2): "))
if mode_num == 1:
    case_ = 1
elif mode_num == 2:
    case_ = 2
else:
    raise ValueError("Invalid mode.")

mode_num = int(input("Choose translate (Chinese:1, English:2, Bilingual:3): "))

if mode_num == 1:
    mode = 'chinese'
elif mode_num == 2:
    mode = 'english'
elif mode_num == 3:
    mode = 'bilingual'
else:
    raise ValueError("Invalid mode.")

# mp4 to mp3
if case_ == 2:
    print("Converting MP4 files to MP3...")
    for filename in tqdm(os.listdir(mp4_folder), desc="MP4 to MP3"):
        if filename.endswith('.mp4'):
            print(f"Converting {filename}...")
            mp4_path = os.path.join(mp4_folder, filename)
            mp3_filename = filename.replace('.mp4', '.mp3')
            mp3_path = os.path.join(mp3_folder, mp3_filename)
            # 转mp3
            extract_mp3(mp4_path, mp3_path)
    print("Done.")

    # mp3 to txt
    print("Transcribing MP3 files to TXT...")
    for filename in tqdm(os.listdir(mp3_folder), desc="MP3 to TXT"):
        if filename.endswith('.mp3'):
            print(f"Converting {filename}...")
            mp3_path = os.path.join(mp3_folder, filename)
            txt_filename = filename.replace('.mp3', '.txt')
            txt_path = os.path.join(txt_folder, txt_filename)
            # 调用whisper
            transcribe_audio_to_txt(mp3_path, txt_path)

# txt to srt(translated)
if case_ == 1:
    print("Converting TXT files to SRT...")
    for filename in tqdm(os.listdir(txt_folder), desc="TXT to SRT"):
        if filename.endswith('.txt'):
            print(f"Converting {filename}...")
            txt_path = os.path.join(txt_folder, filename)
            srt_path = os.path.join(srt_folder, filename)
            format2srt(txt_path, srt_path, test_translate, mode)

    # 重命名SRT文件
    rename_txt2srt(srt_folder)

print("Process completed successfully.")
