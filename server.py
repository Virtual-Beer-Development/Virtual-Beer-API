from fastapi import FastAPI
from src.drink_info import get_drink, get_drink_tags, get_instruction

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/get_drink/{drink}")
async def send_drink(drink):
    data = get_drink(drink)
    if data:
        return data
    if not data:
        return {"message": "Drink Not Found...", "sent":"OK"}

@app.get("/get_tags/{drink}")
async def get_drink_tag(drink):
    data = get_drink_tags(drink)
    if data:
        return {"tags":[data]}
    if not data:
        return {"message": "Drink Not Found...", "sent":"OK"}

@app.get("/get_instructions/{lang}/{drink}")
async def get_ins(lang, drink):
    data = get_instruction(lang, drink)
    if data:
        return {"instructions":data}
    if not data:
        return {"message":"Unsupported Language", "sent":"OK"}