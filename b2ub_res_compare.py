import os
import numpy as np
from PIL import Image, ImageChops

input_folder_path = "/home/siok002/CODE/Blind2Unblind-main/res/input"
n2v_folder_path = "/home/siok002/CODE/Blind2Unblind-main/res/out_N2V"
b2nb_folder_path = "/home/siok002/CODE/Blind2Unblind-main/res/out_Blind2Unblind_bmp"

input_image_files = [f for f in os.listdir(input_folder_path) if f.endswith('.bmp')]
in_image_arrays = []
for filename in input_image_files:
    in_img_path = os.path.join(input_folder_path, filename)
    with Image.open(in_img_path) as img:
        in_image_arrays.append(np.array(img))

n2v_image_files = [f for f in os.listdir(n2v_folder_path) if f.endswith('.bmp')]
n2v_image_arrays = []
for filename in n2v_image_files:
    n2v_img_path = os.path.join(n2v_folder_path, filename)
    with Image.open(n2v_img_path) as img:
        n2v_image_arrays.append(np.array(img))

b2nb_image_files = [f for f in os.listdir(b2nb_folder_path) if f.endswith('.bmp')]
b2nb_image_arrays = []
for filename in b2nb_image_files:
    b2nb_img_path = os.path.join(b2nb_folder_path, filename)
    with Image.open(b2nb_img_path) as img:
        b2nb_image_arrays.append(np.array(img)[:,:,0])
        # b2nb_image_arrays.append(np.array(img))

print(f'len in_image_arrays: {len(in_image_arrays)}. shape in_image_arrays[0]: {in_image_arrays[0].shape}')
print(f'len n2v_image_arrays: {len(n2v_image_arrays)}. shape n2v_image_arrays[0]: {n2v_image_arrays[0].shape}')
print(f'len b2nb_image_arrays: {len(b2nb_image_arrays)}. shape b2nb_image_arrays[0]: {b2nb_image_arrays[0].shape}')

# mse_arrays = []
# rms_arrays = []
rms = 0
rms_all_n2v = []
rms_all_b2nb = []
delta_max_min = 0
delta_max_min_all_n2v = []
delta_max_min_all_b2nb = []
delta_std_dev = 0
delta_std_dev_all_n2v = []
delta_std_dev_all_b2nb = []


if len(in_image_arrays) == len(n2v_image_arrays):
    for i in range(len(n2v_image_arrays)):
        rms = np.sqrt(np.mean((in_image_arrays[i] - n2v_image_arrays[i]) ** 2))
        rms_all_n2v.append(rms)
        max1 = np.max(in_image_arrays[i])
        max2 = np.max(n2v_image_arrays[i])
        min1 = np.min(n2v_image_arrays[i])
        min2 = np.min(in_image_arrays[i])
        diff_max = max1 - max2 if max1 > max2  else max2 - max1
        diff_min = min1 - min2 if min1 > min2  else min2 - min1
        delta_max_min = diff_max + diff_min
        delta_max_min_all_n2v.append(delta_max_min)
        # delta_std_dev = abs(np.std(in_image_arrays[i]) - np.std(n2v_image_arrays[i]))
        delta_std_dev = np.std(n2v_image_arrays[i])
        delta_std_dev_all_n2v.append(delta_std_dev)



# print('rms_all: ', rms_all/len(in_image_arrays))
# print('delta_max_min_all: ', delta_max_min_all/len(in_image_arrays))
# print('delta_std_dev_all: ', delta_std_dev_all/len(in_image_arrays))

if len(in_image_arrays) == len(b2nb_image_arrays):
    for i in range(len(b2nb_image_arrays)):
        rms = np.sqrt(np.mean((in_image_arrays[i] - b2nb_image_arrays[i]) ** 2))
        rms_all_b2nb.append(rms)
        # max = abs(np.max(in_image_arrays[i]) - np.max(b2nb_image_arrays[i]))
        # min = abs(np.min(b2nb_image_arrays[i]) - np.min(in_image_arrays[i]))
        # delta_max_min = max + min
        max1 = np.max(in_image_arrays[i])
        max2 = np.max(b2nb_image_arrays[i])
        min1 = np.min(b2nb_image_arrays[i])
        min2 = np.min(in_image_arrays[i])
        diff_max = max1 - max2 if max1 > max2 else max2 - max1
        diff_min = min1 - min2 if min1 > min2 else min2 - min1
        delta_max_min = diff_max + diff_min
        delta_max_min_all_b2nb.append(delta_max_min)
        # delta_std_dev = abs(np.std(in_image_arrays[i]) - np.std(b2nb_image_arrays[i]))
        delta_std_dev = np.std(b2nb_image_arrays[i])
        delta_std_dev_all_b2nb.append(delta_std_dev)

# print('\nrms_all_n2v: ')
# for i in range(len(in_image_arrays)):
#     print(rms_all_n2v[i], end=" ")
# print('\nrms_all_b2nb: ')
# for i in range(len(in_image_arrays)):
#     print(rms_all_b2nb[i], end=" ")
# print('\ndelta_max_min_all_n2v: ')
# for i in range(len(in_image_arrays)):
#     print(delta_max_min_all_n2v[i], end=" ")
# print('\ndelta_max_min_all_b2nb: ')
# for i in range(len(in_image_arrays)):
#     print(delta_max_min_all_b2nb[i], end=" ")
# print('\ndelta_std_dev_all_n2v: ')
# for i in range(len(in_image_arrays)):
#     print(delta_std_dev_all_n2v[i], end=" ")
# print('\ndelta_std_dev_all_b2nb: ')
# for i in range(len(in_image_arrays)):
#     print(delta_std_dev_all_b2nb[i], end=" ")

rms_all = 0
delta_max_min_all = 0
delta_std_dev_all = 0
for i in range(len(rms_all_n2v)):
    rms_all += rms_all_n2v[i]
    delta_max_min_all += delta_max_min_all_n2v[i]
    delta_std_dev_all += delta_std_dev_all_n2v[i]
print('n2v: ')
print('rms_all: ', rms_all / len(in_image_arrays))
print('delta_max_min_all: ', delta_max_min_all / len(in_image_arrays))
print('delta_std_dev_all: ', delta_std_dev_all / len(in_image_arrays))

rms_all = 0
delta_max_min_all = 0
delta_std_dev_all = 0
for i in range(len(rms_all_b2nb)):
    rms_all += rms_all_b2nb[i]
    delta_max_min_all += delta_max_min_all_b2nb[i]
    delta_std_dev_all += delta_std_dev_all_b2nb[i]
print('b2nb: ')
print('rms_all: ', rms_all / len(in_image_arrays))
print('delta_max_min_all: ', delta_max_min_all / len(in_image_arrays))
print('delta_std_dev_all: ', delta_std_dev_all / len(in_image_arrays))

#ssim