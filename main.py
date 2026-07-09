from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class Interaction(BaseModel):
    customer_name: str
    company: str
    interaction_type: str
    notes: str

@app.get("/")
def home():
    return {"message": "AI CRM Backend Running Successfully"}

@app.post("/save")
def save_interaction(data: Interaction):
    return {
        "status": "success",
        "data": data
    }