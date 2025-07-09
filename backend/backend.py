# software engineers
import pandas as pd
import numpy as np
import joblib

from fastapi import FastAPI
from sklearn.preprocessing import LabelEncoder

# importing the dataset
data=pd.read_csv("../data-storage/breast_dataset.csv")

# preprocessing (adjusting) the data
label_class = LabelEncoder()
data["Class"] = label_class.fit_transform(data["Class"])

# app serve end point
app = FastAPI()

model = joblib.load("../model-storage/forest.joblib")

# create apis

@app.get("/")
async def root():
  return {"message": "Welcome to the API Page for Ops Random Forest Breast Cancer Classifier!"}

@app.post("/predict/")
async def predict_cancer(data: dict):
  features = np.array(data["features"]).reshape(1,-1)
  prediction = model.predict(features)
  class_name = label_class.inverse_transform(prediction)[0]
  return {"class": class_name}


# uvicorn backend:app --reload --host 172.30.112.1 --port 8000
# uvicorn backend:app --reload --host 0.0.0.0 --port 8000