from PIL import Image
import os

def convert_png_to_bmp(png_file_path, bmp_file_path):
    """
    将PNG图像转换为BMP图像。

    :param png_file_path: PNG图像的文件路径。
    :param bmp_file_path: 转换后BMP图像的保存路径。
    """
    with Image.open(png_file_path) as img:
        img.save(bmp_file_path, format='BMP')

# 示例用法
png_folder_path = '/home/siok002/CODE/Blind2Unblind-main/res/out_Blind2Unblind'  # PNG文件的路径
bmp_folder_path = '/home/siok002/CODE/Blind2Unblind-main/res/out_Blind2Unblind_bmp'  # 转换后BMP文件的保存路径
input_image_files = [f for f in os.listdir(png_folder_path) if f.endswith('.png')]
for filename in input_image_files:
    in_img_path = os.path.join(png_folder_path, filename)
    out_img_path = os.path.join(bmp_folder_path, filename.replace(".png",".bmp"))
    with Image.open(in_img_path) as img:
        convert_png_to_bmp(in_img_path, out_img_path)


