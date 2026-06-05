import torch

print("Torch Version:", torch.__version__)
print("CPU Only:", not torch.cuda.is_available())