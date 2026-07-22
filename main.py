from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/character/{char_name}")
def get_character(char_name: str):
    with open(f"char/{char_name}.json") as f:
        character = json.load(f)
    try:
        return character
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Character not found")