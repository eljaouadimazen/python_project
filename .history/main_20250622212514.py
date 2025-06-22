from fastapi import FastAPI
app = FastAPI()



@app.get("/posts")
def root():
    return {"message": "Hello "}
