from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="Task Manager API")
tasks = {}


# TODO: Implement GET /health and return {"status": "ok"}.

# TODO: Define Pydantic models and implement the task collection routes.

# TODO: Implement routes to retrieve, update, and delete an individual task.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)