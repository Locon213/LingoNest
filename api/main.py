from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to LingoNest API!"}

# Endpoint для перевода текста, который мы будем реализовывать позже
@app.post("/translate")
async def translate(text: str, target_lang: str):
    # Здесь будет логика для отправки текста на перевод
    return {"translated_text": "Пример перевода"}
