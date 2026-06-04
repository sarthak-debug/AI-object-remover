import torch
import transformers

print("Torch:", torch.__version__)
print("Transformers:", transformers.__version__)
print("CUDA:", torch.cuda.is_available())

print("AI Environment Ready ")