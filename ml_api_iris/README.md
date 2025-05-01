Простой пример REST API для предсказаний с помощью обученной ML-модели на FastAPI.

Быстрый старт
-------------

1. Клонируйте репозиторий:
   git clone https://github.com/yourusername/ml_api_project.git
   cd ml_api_project

2. Создайте и активируйте виртуальное окружение:
   python3 -m venv venv
   source venv/bin/activate

3. Установите зависимости:
   pip install -r requirements.txt

4. Обучите модель:
   python train_model.py

5. Запустите API сервер:
   uvicorn api:app --reload

6. Откройте документацию:
   http://127.0.0.1:8000/docs

7. Протестируйте endpoint /predict через Swagger UI или с помощью скрипта:
   python test_request.py

Пример запроса
--------------

POST /predict
{
  "data": [5.1, 3.5, 1.4, 0.2]
}

Пример ответа
-------------

{
  "prediction": 0
}

Структура проекта
-----------------

- train_model.py — обучение и сохранение модели
- api.py — FastAPI сервер
- test_request.py — пример клиента для тестирования
- model.pkl — сохранённая модель (генерируется после обучения)