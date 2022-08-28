from pytube import YouTube
import os
import ffmpeg

AUDIO_EXTENSION, AUDIO_FORMAT = ".mp3", "mp3"
VIDEO_EXTENSION, VIDEO_FORMAT = ".mp4", "mp4"
MAX_RES = ["1080p", "1440p", "2160p"]
BORDER = "*****************************************************************************"

def download_stream(stream, extension, destination):
    out_file = stream.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + extension
    os.rename(out_file, new_file)
    return new_file

def get_destination():
    print(BORDER)
    print("Enter the destination as an absolute path")
    destination = str(input(">> "))
    return destination

def join_streams(audio, video, destination):
    input_video = ffmpeg.input(video)
    input_audio = ffmpeg.input(audio)
    new_file = title + "  " + VIDEO_EXTENSION
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(destination + "\\" + new_file).run()
    path = os.path.join(destination, audio)
    os.remove(path)
    path = os.path.join(destination, video)
    os.remove(path)
    return new_file

link = input("Enter the video's URL: ")
try:
    yt = YouTube(link)
    title = yt.title

    while True:
        print(BORDER)
        form = input("MP4 or MP3? ")
        if form.lower() == AUDIO_FORMAT:
            destination = get_destination()
            stream = yt.streams.filter(only_audio=True).first()
            extension = AUDIO_EXTENSION
            new_file = download_stream(stream, extension, destination)
            print(BORDER)
            print("Your download is complete!!!")
            break
        elif form.lower() == VIDEO_FORMAT:
            destination = get_destination()
            while True :
                available_resolutions = [i for i in (list(dict.fromkeys([i.resolution for i in yt.streams if i.resolution])))]
                available_resolutions.sort()
                print(BORDER)
                for item in available_resolutions:
                    print(item)
                resolution = input("These are the available resolutions for this video. Which resolution would you prefer? ")
                if resolution not in available_resolutions:
                    print("No such resolution.Please enter one of the given resolution options.")
                else:
                    break
            stream1 = yt.streams.filter(progressive=False, type="audio").first()
            stream2 = yt.streams.filter(progressive=False, type="video", res=resolution).first()
            audio_file = download_stream(stream1, AUDIO_EXTENSION, destination)
            video_file = download_stream(stream2, VIDEO_EXTENSION, destination)
            new_file = join_streams(audio_file, video_file, destination)
            print(BORDER)
            print("Your download is complete!!!")
            break
        else:
            print("Wrong Form.")
except:
    print(BORDER)
    print("Connection Error")