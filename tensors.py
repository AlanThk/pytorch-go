import torch
import numpy as np

data = [[[1, 2,3], [3, 4,5]]]
x_data = torch.tensor(data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# We move our tensor to the GPU if available
if torch.cuda.is_available():
  tensor = tensor.to('cuda')
  print(f"Device tensor is stored on: {tensor.device}")

tensor = torch.rand(2, 2,1)
print(tensor)
#
# t1 = torch.cat([tensor, tensor], dim=0)
# print(t1.shape)
#
# t1 = torch.cat([tensor, tensor], dim=1)
# print(t1.shape)
#
# t1 = torch.cat([tensor, tensor], dim=2)
# print(t1.shape)

tensor = torch.ones(4,4)
tensor[:,1] = 0
# This computes the element-wise product
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
# Alternative syntax:
print(f"tensor * tensor \n {tensor * tensor}")

print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
# Alternative syntax:
print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

print(tensor, "\n")
tensor.add_(5)
print(tensor)

n = np.ones(5)
t = torch.from_numpy(n)
print(f"n: {n}")
print(f"t: {t}")

np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")



data=[[2,.6,9],[54,23,6]]
t = torch.tensor(data)
print(t.shape)
n = np.array(data)
print(n.shape)

t2n = t.numpy()
print(t2n.shape)

n2t = torch.from_numpy(n)
print(n2t.shape)