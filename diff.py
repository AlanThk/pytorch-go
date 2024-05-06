#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:17:49 2024

@author: siok003
"""

import os  
import numpy as np
from PIL import Image, ImageChops  
import matplotlib.pyplot as plt  
import cv2
  

def get_images_from_dir(directory):  

    """从指定目录获取图片，返回文件名和文件路径的字典"""  

    supported_formats = ['jpg', 'jpeg', 'png', 'gif', 'bmp']  

    images = {}  

    for root, dirs, files in os.walk(directory):  

        for file in files:  

            if file.split('.')[-1].lower() in supported_formats:  

                filename_without_ext = os.path.splitext(file)[0]  

                images[filename_without_ext] = os.path.join(root, file)  

    return images  

  

def draw_difference(image_path0, image_path1, image_path2, output_path):  

    """绘制两个图片的差分图并保存"""  
    image0 = Image.open(image_path0)
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

      

    # 确保两个图像大小相同，如果不同则调整第一张图片的大小  

    if image1.size != image2.size:  

        image1 = image1.resize(image2.size)  

      

    # 使用ImageChops计算差分图  
    image1 = np.array(image1, dtype = np.float32)  
    image2 = np.array(image2, dtype = np.float32) 

    diff = abs(image1 - image2)

    # 创建一个一行三列的子图布局  
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(16, 4))  
      
    # 在第一个子图中显示第一个灰度图像  
    axs[0].imshow(image0, cmap='gray')  
    axs[0].set_title('gerber')  
    axs[0].axis('off')  # 关闭坐标轴  
      
    # 在第二个子图中显示第二个灰度图像  
    axs[1].imshow(image1, cmap='gray')  
    axs[1].set_title('img')  
    axs[1].axis('off')  # 关闭坐标轴  

    # 在第二个子图中显示第二个灰度图像  
    axs[2].imshow(image2, cmap='gray')  
    axs[2].set_title('predicted')  
    axs[2].axis('off')  # 关闭坐标轴  
      
    # 使用imshow函数绘制彩色图像  
    # 可以通过cmap参数指定颜色映射，例如 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'rainbow', 等。  
    cax = axs[3].imshow(diff, cmap='jet', vmin=np.min(diff), vmax=np.max(diff))  
      
    # 添加颜色条  
    # 使用fig.colorbar()函数添加颜色条，可以通过cax参数指定与哪个图像相关联  
    # fig.colorbar(cax)  
      
    # 设置标题和坐标轴标签（可选）  
    axs[3].set_title('Max Diff Value Is : ' + str(np.max(diff)))  
    # axs[2].set_xlabel('X-axis Label')  
    # axs[2].set_ylabel('Y-axis Label')  
      
    # 显示图像（如果在Jupyter Notebook等交互式环境中）  
    # plt.show()  
      
    # 调整子图之间的距离  

    # plt.tight_layout() 

    # 保存图像到文件，可以设置文件格式和DPI  
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

  

def main(dir0, dir1, dir2, output_dir):  

    images0 = get_images_from_dir(dir0)  

    images1 = get_images_from_dir(dir1)  

    images2 = get_images_from_dir(dir2)  

      

    # 获取两个目录中相同的文件名（不包括后缀）  

    common_filenames = set(images0.keys()) & set(images1.keys()) & set(images2.keys())

    # 对于每个相同的文件名，找到对应的完整路径并绘制差分图  

    for filename in common_filenames:  

        path0 = images0[filename]  

        path1 = images1[filename]  

        path2 = images2[filename]  

        output_path = os.path.join(output_dir, f"diff_{filename}.png")  # 使用.png作为输出格式 
        draw_difference(path0, path1, path2, output_path)  
        print(f"Saved difference image for {filename} to {output_path}")  
  

if __name__ == "__main__":  

    # draw_difference("/home/siok003/AI/vispectdl-development/pcb_output/img_ok/2.jpg", "/home/siok003/AI/vispectdl-development/pcb_output/output/2.png" , "/home/siok003/AI/vispectdl-development/pcb_output/diff" )
    DIRECTORY0 = "/home/siok002/CODE/vispectdl-development/dataset/128/img_gerber"  # 替换为你的第一个目录路径
    DIRECTORY1 = "/home/siok002/CODE/vispectdl-development/dataset/128/img"  # 替换为你的第一个目录路径
    DIRECTORY2 = "/home/siok002/CODE/vispectdl-development/dataset/predicted-output/res"  # 替换为你的第二个目录路径

    OUTPUT_DIRECTORY = "/home/siok002/diff_out"  # 替换为你的输出目录路径
    main(DIRECTORY0, DIRECTORY1, DIRECTORY2, OUTPUT_DIRECTORY)
