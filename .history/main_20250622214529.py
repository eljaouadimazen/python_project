from fastapi import FastAPI
from fastapi import Body

app = FastAPI()



@app.get("/posts")
def get_posts():
    return {"data": "this is your post "}
@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "created successfuly"}