from fastapi import FastAPI
from app.api import audio

app = FastAPI(title="DJ MoodMatcher API")

# Include the audio processing routes
# app.include_router(audio.router)

@app.get("/")
def root():
    return {"message": "DJ MoodMatcher API is running!"}