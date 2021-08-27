from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


# run cmd:  uvicorn main:app --reload      chose port: uvicorn main:app --port 8001 --reload
# docs: http://127.0.0.1:8000/docs  http://127.0.0.1:8000/redo
app = FastAPI()


@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get('/user/{user_id}')
def get_user(user_id: int):
    user_data = "the data of user :{}".format(user_id)
    return {user_data}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_name": item.name, "item_id": item_id}


# 查询参数
# 声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数
fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get('/items/')
def read_item(skip: int = 0, limit: int = 10):  # 这两个是默认值
    return fake_items_db[skip: skip + limit]


@app.get('/items/{item_id}')
def read_item_optional(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items_bool/{item_id}")
def read_item_bool(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({
            "description": "This is a amazing item that has a long description"
        })
    return item
