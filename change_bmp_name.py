import os
import sys

# src = "/home/siok002/CODE/vispectdl-development/dataset/256/img_gerber/0.png"
# dst = "/home/siok002/CODE/vispectdl-development/dataset/256/"
# os.system(f"mv {src} {dst}")
# os.system("mv /home/siok002/CODE/vispectdl-development/dataset/256/img_gerber/0.png /home/siok002/CODE/vispectdl-development/dataset/256/")

in_folder_path = "/home/siok002/CODE/Blind2Unblind-main/res/input"
out_folder_path = "/home/siok002/CODE/Blind2Unblind-main/res/out_Blind2Unblind_bmp"

in_png_files = [f for f in os.listdir(in_folder_path)]
out_png_files = [f for f in os.listdir(out_folder_path)]
for i in range(len(in_png_files)):
    start = os.path.join(out_folder_path, out_png_files[i])
    end = os.path.join(out_folder_path, in_png_files[i])
    # dst = os.path.join(out_folder_path, filename)
    os.system(f"mv {start} {end}")