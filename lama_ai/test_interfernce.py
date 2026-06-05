import os
from model_loader import load_model

MODEL_PATH = "weights/model.onnx"

if not os.path.exists(MODEL_PATH):
    print("Model file not found.")
else:
    session = load_model(MODEL_PATH)
    print("Inputs:", session.get_inputs())
    print("Outputs:", session.get_outputs())