from fastapi import FastAPI, HTTPException
from urllib.parse import urlparse, parse_qs
import uvicorn
from pydantic import BaseModel
import requests
from typing import Optional

from Utils.Transcription import Transcription
from Utils.YoutubeOperations import YoutubeOperations

app = FastAPI()

class URLRequest(BaseModel):
    url: str  # URL where q parameter should be fetched from

@app.get("/")
async def fetch_q(q: Optional[str] = None):
    try:
        t = Transcription()
        y = YoutubeOperations()

        print("Query", q)    
        # Download file from youtube
        filename = y.download(URL=q)
    
        
        # Transcribe
        data = t.transcriptFile(filename=filename)
        return {"data": data}
    except Exception as e:
        print("Error", e)

# Ensure that the app runs with `python index.py`
if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=9033, reload=True)
