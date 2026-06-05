import onnxruntime as ort

def load_model(model_path):

    session = ort.InferenceSession(
        model_path,
        providers=["CPUExecutionProvider"]
    )

    print("Model Loaded")

    return session