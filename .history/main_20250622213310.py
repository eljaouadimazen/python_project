from fastapi import FastAPI
app = FastAPI()



@app.get("/posts")
def get_posts():
    return {"data": "this is your post "}
@app.post("/createpost")
def create_post(payload: dict = body())