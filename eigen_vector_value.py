import numpy
import torch
import numpy as np

t1 = torch.tensor([[0,1],[1,1]])
t_res = torch.tensor([[0,1],[1,1]])
n = int(input("input an number:\n"))
for i in range(n):
    t_res = torch.mm(t1, t_res)
n1 = numpy.array([[0,1],[1,1]])
n_res = np.square(n1)
print(t_res)

# mat = np.array([[-1, 1, 0],
#                 [-4, 3, 0],
#                 [1, 0, 2]])

mat = np.array([[0,1],[1,1]])

eigenvalue, featurevector = np.linalg.eig(mat)

print("特征值：", eigenvalue)
print("特征向量：", featurevector)
