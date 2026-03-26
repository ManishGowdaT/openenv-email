from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv
from tasks import TASKS

app = FastAPI()

env = EmailEnv()
class ActionRequest(BaseModel):
    action: str


@app.get("/")
def home():
    return {"message": "Email AI Environment is running"}


@app.get("/reset")
def reset():
    state = env.reset()
    return {"state": state}


@app.get("/state")
def state():
    return {"state": env._get_state()}

@app.post("/step")
def step(req: ActionRequest):
    state, reward, done = env.step(req.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
@app.get("/tasks")
def get_tasks():
    return {"tasks": TASKS}
@app.get("/grader")
def grader():
    # simple grading example
    # in real eval, they’ll call this after running steps
    return {
        "score_range": "0.0 - 1.0",
        "note": "Reward returned from step() is the score"
    }