# lama_ai/check_model.py

from model_loader import load_model

session = load_model("weights/deepfillv2.onnx")

print("MODEL LOADED")
print("INPUTS:")
for inp in session.get_inputs():
    print(inp.name, inp.shape)

print("OUTPUTS:")
for out in session.get_outputs():
    print(out.name, out.shape)