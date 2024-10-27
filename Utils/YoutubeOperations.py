import pytube as pt

class YoutubeOperations:
    def __init__(self):
        pass
    
    def download(self,URL):
        # download mp3 from youtube video (Two Minute Papers)
        filename = "audio_english.mp3"
        yt = pt.YouTube(URL)
        stream = yt.streams.filter(only_audio=True)[0]
        stream.download(filename=filename)
        return filename