from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item")
def read_item():
    return {"Household":"99 rs","clothes":"199 rs","Electronics":"5000rs" }
