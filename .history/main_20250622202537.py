from fastapi import FastAPI
myapp = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}
