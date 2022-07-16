from fastapi import FastAPI 

app = FastAPI(title="MLOps Basic App")

@app.get("/")
async def home():
    return "<h2>This is sample NLP Project with MLOps</h2>"