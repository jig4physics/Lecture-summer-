import whisper

class Transcription:
    def __init__(self, modelType="base"):
        # Load the Whisper model
        self.model = whisper.load_model(modelType)
        
    def transcript(self,waveform,sample_rate):
        # Convert to numpy array as Whisper requires numpy array input
        audio_numpy = waveform.squeeze().numpy()

        # Transcribe the audio using Whisper
        result = self.model.transcribe(audio_numpy)
        transcription = result['text']
        return transcription
    
    def transcriptFile(self, filename):
        result = self.model.transcribe(filename)
        transcription = result['text']
        return transcription