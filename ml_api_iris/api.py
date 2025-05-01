from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Инициализация FastAPI приложения
app = FastAPI()

# Загрузка обученной модели
model = joblib.load("iris_model.pkl")

# Описание структуры входных данных


class Features(BaseModel):
    data: list

# Эндпоинт для предсказания


@app.post("/predict")
def predict(features: Features):
    X = np.array([features.data])
    prediction = model.predict(X)
    return {"prediction": int(prediction[0])}
