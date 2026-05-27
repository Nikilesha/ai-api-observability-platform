from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
