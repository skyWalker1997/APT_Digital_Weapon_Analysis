import os
import shutil

source_dir = '/Users/skywalker/Desktop/APT_Malware_Sandbox_Data_Analysis/APT_Digital_Weapon'
target_dir = '/Users/skywalker/Desktop/APT_Malware_Sandbox_Data_Analysis/APT'
dirs = os.listdir(source_dir)
APT_Name_List = []
APT_Malware_json = []
for dir in dirs:
    if dir.find('.') >= 0:
        continue
    else:
         APT_Name_List.append(dir)
         temp_dir = source_dir+'/'+dir+'/report'
         sub_dir = os.listdir(temp_dir)
         for json_file in sub_dir:
             temp_target_dir = target_dir+'/'+dir+'/'
             if not os.path.exists(temp_target_dir):
                os.makedirs(temp_target_dir)  # 创建路径
             shutil.move(temp_dir+'/'+json_file, temp_target_dir)