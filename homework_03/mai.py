from fastapi import FastAPI
import asyncio

app = FastAPI()

todos = []

@app.get("/todos")
def get_todos():
    await asyncio.sleep(3)
    return todos

@app.post("/todos/{todo_item}")
def create_todo(todo_item: str):
    todos.append(todo_item)
    return {"message": "Задача добавлена"}

@app.delete("/todos/{index}")
def delete_todo(index: int):
    if index < len(todos):
        del todos[index]
        return {"message": "Задача удалена"}
    else:
        return {"message": "Неверный индекс"}