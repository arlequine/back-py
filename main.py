from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hola Arlequin"

@app.get("/url")
async def url():
    return {"url": "arlequindev.com"}