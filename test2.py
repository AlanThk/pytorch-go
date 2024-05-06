import os
import numpy as np
from PIL import Image, ImageChops

# image0 = Image.open('/home/siok002/CODE/vispectdl-development/dataset/512/img/6872.png')
# image1 = Image.open('/home/siok002/CODE/vispectdl-development/dataset/predicted-output/res/6872.png')
# image0 = np.array(image0, dtype = np.float32)
# image1 = np.array(image1, dtype = np.float32)
# mse = np.mean((image0 - image1) ** 2)
# diff_max = np.max(image0 - image1)
# print('6872.png mse: ', mse)
# print('6872.png rms: ', np.sqrt(mse))
# print('6872.png diff_max: ', diff_max)

in_folder_path = "/home/siok002/CODE/vispectdl-development/dataset/256_test/img/"888
out_folder_path = "/home/siok002/CODE/vispectdl-development/dataset/predicted-output/res/"jzjzj

in_png_files = [f for f in os.listdir(in_folder_path) if f.endswith('.png')]
in_image_arrays = []dfgsdfhsdh
for filename in in_png_files:
    in_img_path = os.path.join(in_folder_path, filename)
    with Image.open(in_img_path) as img:
        in_image_arrays.append(np.array(img))

out_png_files = [f for f in os.listdir(out_folder_path) if f.endswith('.png')]
out_image_arrays = []
for filename in out_png_files:
    out_img_path = os.path.join(out_folder_path, filename)
    with Image.open(out_img_path) as img:
        out_image_arrays.append(np.array(img))

print('len in_image_arrays.shape: ', len(in_image_arrays))
print('len out_image_arrays.shape: ', len(out_image_arrays))

mse_arrays = []
rms_arrays = []
mse_sum = 0
rms_sum = 0
count_bad = 0
if len(in_image_arrays) == len(out_image_arrays):
    for i in range(len(out_image_arrays)):
        mse = np.mean((in_image_arrays[i] - out_image_arrays[i]) ** 2)
        rms = np.mean((in_image_arrays[i] - out_image_arrays[i]) ** 2)
        mse_arrays.append(mse)
        rms_arrays.append(np.sqrt(rms))
        if mse > 16:
            count_bad += 1
            print('png mse: ', i,mse,len(out_image_arrays))
# !diff_max = np.max(in_image_arrays - out_image_arrays)
for j in range(len(mse_arrays)):
    mse_sum += mse_arrays[j]
    rms_sum += rms_arrays[j]
mse_mse = mse_sum / len(mse_arrays)
rms_rms = rms_sum / len(rms_arrays)
print('all mse average: ', mse_mse)
print('all rms average: ', rms_rms)
print('count_bad: ', count_bad)
