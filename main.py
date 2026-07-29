from fastapi import FastAPI
from Backend.routes.predict import router as predict_router

app = FastAPI(
    title="Credit Default Prediction API",
    version="1.0.0"
)

app.include_router(predict_router)

@app.get("/")
def home():
    return {"Message": "The Credit Default Model API is Running Perfectly"}