from fastapi.testclient import TestClient
from ..backend import app

client = TestClient(app)

def test_root():
  response = client.get('/')
  assert response.status_code == 200
  assert response.json() == {"message": "Welcome to the API Page for Ops Random Forest Breast Cancer Classifier!"}