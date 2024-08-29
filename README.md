# VidCaptionGen
Generate video caption in crt format.
## Requirements
- python of course
- faster-whisper
- ffmpeg-python


```mermaid
graph LR
A[video] -> B[audio]
B -> C[origin_txt]
C -> D[srt]
```