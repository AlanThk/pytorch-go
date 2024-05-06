import os
import re

import numpy as np
from PIL import Image

import os
import numpy as np
from PIL import Image, ImageChops
from pathlib import Path

# image0 = Image.open('/home/siok002/CODE/vispectdl-development/dataset/512/img/6872.png')
# image1 = Image.open('/home/siok002/CODE/vispectdl-development/dataset/predicted-output/res/6872.png')
# image0 = np.array(image0, dtype = np.float32)
# image1 = np.array(image1, dtype = np.float32)
# mse = np.mean((image0 - image1) ** 2)
# diff_max = np.max(image0 - image1)
# print('6872.png mse: ', mse)
# print('6872.png rms: ', np.sqrt(mse))
# print('6872.png diff_max: ', diff_max)

opt_folder_path = Path(r"/home/siok002/res/defect/256_defect_optical")
ras_folder_path = Path(r"/home/siok002/res/defect/256_defect_raster")
res_folder_path = Path(r"/home/siok002/res/defect/res")
out_folder_path = Path(r"/home/siok002/res/defect/output")

opt_png_files = [f for f in os.listdir(opt_folder_path) if f.endswith('.png')]
opt_png_files = sorted(opt_png_files, key=lambda x: int(re.search(r'\d+', x).group()))
opt_png_files = sorted(opt_png_files)
opt_image_arrays = []
for filename in opt_png_files:
    in_img_path = os.path.join(opt_folder_path, filename)
    with Image.open(in_img_path) as img:
        opt_image_arrays.append(np.array(img,dtype=np.float32))

ras_png_files = [f for f in os.listdir(ras_folder_path) if f.endswith('.png')]
ras_png_files = sorted(ras_png_files, key=lambda x: int(re.search(r'\d+', x).group()))
ras_png_files = sorted(ras_png_files)
ras_image_arrays = []
for filename in ras_png_files:
    in_img_path = os.path.join(ras_folder_path, filename)
    with Image.open(in_img_path) as img:
        ras_image_arrays.append(np.array(img,dtype=np.float32))

res_png_files = [f for f in os.listdir(res_folder_path) if f.endswith('.png')]
res_png_files = sorted(res_png_files, key=lambda x: int(re.search(r'\d+', x).group()))
res_png_files = sorted(res_png_files)
res_image_arrays = []
for filename in res_png_files:
    in_img_path = os.path.join(res_folder_path, filename)
    with Image.open(in_img_path) as img:
        res_image_arrays.append(np.array(img,dtype=np.float32))

print('len in_image_arrays.len: ', len(opt_image_arrays))
print('len out_image_arrays.len: ', len(res_image_arrays))
print('len in_image_arrays.shape: ', res_image_arrays[0].shape[0])
print('len in_image_arrays.size: ', res_image_arrays[0].size)

pred_width = res_image_arrays[0].shape[0]
for i in range(len(opt_image_arrays)):
    val_img = np.zeros([pred_width, pred_width * 4], dtype=np.float32)
    val_img[:, :pred_width] = opt_image_arrays[i]
    val_img[:, pred_width:2 * pred_width] = ras_image_arrays[i]
    val_img[:, 2 * pred_width:3 * pred_width] = res_image_arrays[i]
    val_img[:, -pred_width:] = opt_image_arrays[i] - res_image_arrays[i]
    np_temp = np.uint8(np.abs(val_img))
    im = Image.fromarray(np.uint8(np.abs(val_img)))
    im.save(out_folder_path.joinpath("test_{}.png".format(i)))

