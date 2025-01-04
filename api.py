from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# Define request body schema
class PredictRequest(BaseModel):
    text: str

# POST endpoint
@app.post("/predict/")
async def predict(request: PredictRequest):
    text = request.text
    predicted_label = 1  # Example prediction
    return {"text": text, "predicted_label": predicted_label}
