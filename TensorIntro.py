import torch

tensor2D = torch.tensor([[1,2,3], [4, 5, 6]])
print(tensor2D)

print(tensor2D.shape)

print(tensor2D.reshape(3,2))

print(tensor2D.view(3,2))

print(tensor2D.T)

print(tensor2D @ tensor2D.T)
