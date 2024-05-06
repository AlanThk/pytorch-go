import os
import sys

# src = "/home/siok002/CODE/vispectdl-development/dataset/256/img_gerber/0.png"
# dst = "/home/siok002/CODE/vispectdl-development/dataset/256/"
# os.system(f"mv {src} {dst}")
# os.system("mv /home/siok002/CODE/vispectdl-development/dataset/256/img_gerber/0.png /home/siok002/CODE/vispectdl-development/dataset/256/")

in_folder_path = "/home/siok002/CODE/vispectdl-development/dataset/256_test/img/"test7
src_folder_path = "/home/siok002/CODE/vispectdl-development/dataset/256/img_gerber/"
out_folder_path = "/home/siok002/CODE/vispectdl-development/dataset/256_test/img_gerber/"

in_png_files = [f for f in os.listdir(in_folder_path) if f.endswith('.png')]
in_image_arrays = []
for filename in in_png_files:
    src = os.path.join(src_folder_path, filename)
    # dst = os.path.join(out_folder_path, filename)
    os.system(f"mv {src} {out_folder_path}")