import os
import time

def format_timestamp(path):
    # 获取文件创建时间
    timestamp = os.path.getctime(path)
    # 将时间戳转换为格式化的日期字符串
    date_str = time.strftime('%Y-%m-%d', time.localtime(timestamp))
    return date_str
def add_header_to_md(file_path, title):
    # 读取原始文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 构建新内容
    header = f"+++\ntitle = \"{title}\"\n+++\n"
    new_content = header + content

    # 重写文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def rename_md_files_in_subfolders(root_path):
    # 首先收集所有文件夹的路径
    folders = []
    for root, dirs, files in os.walk(root_path, topdown=False):
        for name in dirs:
            folders.append(os.path.join(root, name))

    # 重命名文件夹
    for folder in folders:
        folder_path, folder_name = os.path.split(folder)
        new_folder_name = folder_name.split(' ')[0]
        new_folder_path = os.path.join(folder_path, new_folder_name)
        if new_folder_path != folder:
            os.rename(folder, new_folder_path)
            print(f"Renamed folder '{folder}' to '{new_folder_path}'")

    #rename md
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                date_str = format_timestamp(file_path)
                name, ext = os.path.splitext(filename)
                new_name = f"{date_str}-{name.split(' ')[0]}{ext}"
                new_file = os.path.join(root, new_name)
                if new_file != file_path:
                    os.rename(file_path, new_file)
                    print(f"Renamed file '{file_path}' to '{new_file}'")
                    add_header_to_md(new_file, name.split(' ')[0])

# 替换为您的文件夹路径
folder_path = 'C:/Users/89206/Downloads/notion'
rename_md_files_in_subfolders(folder_path)
