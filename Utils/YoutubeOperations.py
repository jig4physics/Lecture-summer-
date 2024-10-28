import pytube as pt
import yt_dlp
import re

class YoutubeOperations:
    def __init__(self):
        pass
    
    def download(self,url):
        ydl_opts={}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict['title']
        video_name = re.sub('[\\\\/*?:"<>|]', '', video_title)
        name = video_name
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
                'noplaylist': True,
                'continue_dl': True,
                'outtmpl': f'./{name}',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
                'geobypass':True,
                'ffmpeg_location':'/usr/bin/ffmpeg'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url)
        return f"{name}.wav"

if __name__ == "__main__":
    yo= YoutubeOperations()
    yo.download(url="https://www.youtube.com/watch?v=-G9XCmD9zbk")