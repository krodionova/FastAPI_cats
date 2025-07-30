from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel


app = FastAPI()

cats = [
    {
        'id': 1,
        'name': 'Kugel',
        'age': 5,
    },
    {
        'id': 2,
        'name': 'Merv',
        'age': 2
    },
]

@app.get(
'/cats',
tags=['Кошечки'],
summary = 'Получить всех кошечек')
def get_cats():
    return cats

@app.get('/cats/{id}', tags=['Кошечки'], summary='Получить конкретную кошечку')
def get_kitty(id: int):
    for kitty in cats:
        if kitty['id'] == id:
            return kitty
    raise HTTPException(status_code=404, detail='такой кисоньки нет :(')

class NewCat(BaseModel):
    name: str
    age: int

#постзапрос на добавление данных

@app.post('/cats', tags=['Кошечки'])
def create_cat(new_cat: NewCat):
    cats.append({
        'name': new_cat.name,
        'age': new_cat.age,
        'id': len(cats) + 1
    }) #здесь обычно pydantic
    return {'success': True, 'message': 'Добавлен новый котик :)'}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)