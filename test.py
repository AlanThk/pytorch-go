##torch.mean()
# import torch
# x = torch.tensor([1,2,3])
# y = torch.tensor([1.5,2,3.5])
# mse = torch.mean(torch.square(x-y))
# print(mse)
# # print(tensor.unsqueeze(-1).shape)
# # print(tensor.unsqueeze(0).shape)
# # print(tensor.unsqueeze(1).shape)
# # print(tensor.unsqueeze(2).shape)
# # print(tensor.unsqueeze(3).shape)

##MSELoss()
# import torch
# import torch.nn as nn
#
# # 假设有一组预测值和真实值
# y_pred = torch.tensor([2.0, 3.0, 4.0], requires_grad=True)
# y_true = torch.tensor([1.0, 3.0, 6.0])
#
# # 创建MSELoss实例
# loss_fn = nn.MSELoss()
#
# # 计算损失
# loss = loss_fn(y_pred, y_true)
#
# print(loss)  # 打印损失值

# #np.log2()
# import numpy as np
# #n_stages = 1 + int(np.round(np.log2(256)))
# n = np.log2(2)
# print(n)
# n = np.log2(1)
# print(n)
# n = int(np.round(np.log2(256)))
# print(n)

#cat unsqueeze split
import torch
t1 = torch.tensor([[[1],[2]],[[3],[1]],[[2],[3]]])
print(t1.shape,t1)
t2 = torch.tensor([[[1],[2]],[[3],[1]],[[2],[3]]])
#print(t2)
t = torch.cat([t1,t2],dim=0)
print(t.shape,t)
#t = t1.unsqueeze(dim=0)
# splitTensors = t1.split(1,dim=-1)
# for i in splitTensors:
#     print(i.shape,i)

# c, h, w = t1.size()
# print(c)
# print(h)
# print(w)