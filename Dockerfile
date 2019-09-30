# Какой образ взять за основу
FROM python:3.6
#Указание рабочей директории
WORKDIR /app
#Копирование содержимого папки в папку app
COPY . /app
#Установка нужных модулей в окружение
RUN pip install -r requirements.txt
#Точка входа в программу (нач команда)
ENTRYPOINT ["python", "app.py"]