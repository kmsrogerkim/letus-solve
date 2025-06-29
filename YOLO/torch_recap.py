import torch

x = torch.randn(2, 2)

print(x.shape)

y = torch.unsqueeze(x, dim = 0)
z = torch.unsqueeze(x, dim = 1)

print(y.shape)
print(z.shape)