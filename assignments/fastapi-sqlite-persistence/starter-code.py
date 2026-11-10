from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="Task Manager API")
tasks = {}
next_task_id = 1


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""


class TaskUpdate(TaskCreate):
    completed: bool = False


class Task(TaskUpdate):
    id: int


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    global next_task_id

    task = {
        "id": next_task_id,
        "title": task_data.title,
        "description": task_data.description,
        "completed": False,
    }
    tasks[next_task_id] = task
    next_task_id += 1
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return tasks[task_id]


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    task = {"id": task_id, **task_data.dict()}
    tasks[task_id] = task
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    del tasks[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# TODO: Replace the in-memory dictionary with SQLite persistence.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)