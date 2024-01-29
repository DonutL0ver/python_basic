FROM python:3.9-buster


COPY mai.py /app/mai.py

RUN pip install fastapi uvicorn

WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "mai:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

#Команда для запуска Docker контейнера
#docker run -d -p 8000:8000 todo-app