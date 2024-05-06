import torch
import numpy as np

empty_tensor = torch.zeros(3, 2, 1)
b = np.random.rand(2,3,5)
a  = torch.randn((2,3,5),dtype = torch.float32)
print(a)
print(a[0,2,4])
ai = a[0,2,4].item()
print(ai)##输出2*3*5=30，即array元素的个数
#print(b)##输出2*3*5=30，即array元素的个数
#print(empty_tensor)