import fastapi

app = fastapi.FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "service": "Foresight Engine"}
