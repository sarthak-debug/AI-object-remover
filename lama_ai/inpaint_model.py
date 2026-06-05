import cv2
import numpy as np
from model_loader import load_model

MODEL_PATH = "lama_ai/weights/model.onnx"

session = None

def get_session():
    global session

    if session is None:
        session = load_model(MODEL_PATH)

    return session


def remove_object(image_path, mask_path):

    print("AI PROCESSING STARTED")

    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, 0)

    print("Image Shape:", image.shape)
    print("Mask Shape:", mask.shape)

    # ONNX inference will go here

    cv2.imwrite("static/result.png", image)

    return "static/result.png"