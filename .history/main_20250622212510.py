from fastapi import FastAPI
app = FastAPI()



@app.get("/post")
def root():
    return {"message": "Hello "}
