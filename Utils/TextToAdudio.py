from gtts import gTTS

class TextToAudio:
    def __init__(self, lang="en"):
        self.lang = lang

    def generateAudio(self, filename, content):
        tts = gTTS(text=content, lang=self.lang)
        tts.save(f"{filename}.mp3")
        print(f"Audio saved as {filename}.mp3")
