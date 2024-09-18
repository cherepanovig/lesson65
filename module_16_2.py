# Домашнее задание по теме "Валидация данных".
# Цель: научится писать необходимую валидацию для вводимых данных при помощи классов Path и Annotated.

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main():
    return f'Главная страница'


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                  examples=["UrbanUser"])],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=[24])]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


@app.get("/user/admin")
async def admin():
    return f'Вы вошли как администратор'


@app.get("/user/{user_id}")
async def userid(user_id: int = Path(ge=1, le=100, description="Enter User ID", examples=[1])):
    return f'Вы вошли как пользователь № {user_id}'
