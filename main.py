from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.get("/character/{char_name}")
def get_character(char_name: str):
    with open(f"char/{char_name}.json") as f:
        character = json.load(f)
    try:
        return character
    except KeyError:
        raise HTTPException(status_code=404, detail="Character not found")