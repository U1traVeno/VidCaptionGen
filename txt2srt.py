import os
import re

import os

def rename_txt2srt(file_dir):
    """
    Change txt file to srt file in the given directory.
    """
    for filename in os.listdir(file_dir):
        if filename.endswith(".txt"):
            new_filename = filename[:-4] + ".srt"
            file_path = os.path.join(file_dir, filename)  # 修正这里，使用 file_dir
            new_file_path = os.path.join(file_dir, new_filename)  # 修正这里，使用 file_dir
            os.rename(file_path, new_file_path)  # 使用修正后的路径
        else:
            print(f"{filename} is not a txt file! Ignoring it.")


def format2srt(txt_path, srt_path, translate, mode):
    """
    Converts subtitle text with timestamps to SRT subtitle format.
    Origin timestamp example:
    [0.00s -> 3.12s]  Hello there!
    SRT timestamp example:

    1
    00:00:00,320 --> 00:00:01,920
    大家好，我的模组制作者和
    hello there my fellow modders and

    2
    00:00:01,920 --> 00:00:04,319
    手工艺者们，在这里度过了美好的时光，
    crafters good times with scar here

    Parameters:
    txt_path (str): The path to the input text file with timestamps.
    srt_path (str): The path to save the formatted SRT subtitle file.
    translate (func): Translate original string and return translated string.
    mode (str): Three modes: 'bilingual', 'chinese', 'english'

    Returns:
    None
    """
    # 从txt文件读取字幕内容
    with open(txt_path, "r") as file:
        ori_txt = file.read()

    # 分割字幕行并剔除调试行
    lines = ori_txt.strip().split("\n")
    filtered_lines = [line for line in lines if not line.startswith("DEBUG")]

    # 正则表达式匹配时间戳
    pattern = re.compile(r'\[(\d+\.\d+)s -> (\d+\.\d+)s\]\s+(.*)')

    srt_subtitles = []
    index = 1

    for line in filtered_lines:
        match = pattern.match(line)
        if match:
            start_time = float(match.group(1))
            end_time = float(match.group(2))
            text = match.group(3)

            # 转换时间格式到 00:00:00,000
            start_timestamp = "{:02}:{:02}:{:02},{:03}".format(
                int(start_time // 3600),
                int((start_time % 3600) // 60),
                int(start_time % 60),
                int((start_time * 1000) % 1000)
            )
            end_timestamp = "{:02}:{:02}:{:02},{:03}".format(
                int(end_time // 3600),
                int((end_time % 3600) // 60),
                int(end_time % 60),
                int((end_time * 1000) % 1000)
            )

            # 翻译
            if mode == 'english' or mode == 'bilingual':
                translated_text = translate(text) 
            else:
                translated_text = text

            if mode == 'chinese':
                subtitle_content = f"{index}\n{start_timestamp} --> {end_timestamp}\n{translated_text}\n"
            elif mode == 'english':
                subtitle_content = f"{index}\n{start_timestamp} --> {end_timestamp}\n{text}\n"
            elif mode == 'bilingual':
                subtitle_content = f"{index}\n{start_timestamp} --> {end_timestamp}\n{translated_text}\n{text}\n"
            else:
                raise ValueError("Invalid mode. Options are 'chinese', 'english', 'bilingual'.")
            
            # 转成srt
            srt_subtitles.append(subtitle_content)
            index += 1
        else:
            print(f"Skipping line: {line}")

    # Write to SRT file
    with open(srt_path, "w", encoding='utf-8') as file:
        file.write("\n".join(srt_subtitles))



def test_translate(text):
    return text + "的中文翻译"

