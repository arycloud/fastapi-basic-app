from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Docker!"}

@app.get("/greeting")
def read_item():
    return {"Assalam-o-Alaikum"}


