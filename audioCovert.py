import os
from pytube import YouTube


def audio_convert(video_url: str) -> None:
    video_file = YouTube(video_url).streams.filter().get_audio_only()
    video_file.download()

    mp4_filename: str = video_file.default_filename
    mp3_filename: str = mp4_filename.replace('.mp4', '.mp3')

    os.rename(mp4_filename, mp3_filename)


if __name__ == '__main__':
    try:
        input_url: str = input('Enter the url: ')
        audio_convert(video_url=input_url)
        print('Download Done!')
    except Exception as e:
        print(f"Something went wrong. Error: {e}")
