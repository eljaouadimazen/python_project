from fastapi import FastAPI
app = FastAPI()



@app.get("/posts")
def get():
    return {"message": "Hello "}
