import torch

print(torch.cuda.is_available())
print(torch.__version__)
print(torch.cuda.device_count())