from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def rutas():
    return {1:"Huasteca", 2:"Cordillera", 3:"Sierra", 4:"Selva"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}