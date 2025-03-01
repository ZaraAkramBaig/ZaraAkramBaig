from fastapi import FastAPI

app = FastAPI()  # Creating a FastAPI instance

@app.get("/")  # Defining a route (endpoint)
def read_root():
    return {"message": "Hello! My Name is Zara Akram. <3 \nWelcome to FastAPI!"}

@app.get("/items/{item_id}")  # Path parameter
def read_item(item_id: int):
    return {"item_id": item_id}
