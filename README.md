# YouTube-Downloader-with-Python
Youtube Downloader console application with Python libraries Pytube and ffmpeg

Pytube is a library used to comunicate with Youtube via Youtube api

Link to pytube doc: https://pytube.io/en/latest/

Ffmpeg is a library used to edit audio and video files. It is used in this project to concatenate the seperate audio file to the video file. This is needed because we use the adaptive streams (streams that can only be audio or video that support higher quality). More about this in the Pytube documentation. 

Link to ffmpeg doc: https://kkroening.github.io/ffmpeg-python/
