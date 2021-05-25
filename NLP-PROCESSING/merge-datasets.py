import pandas as pd
import os


def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    file_list = []
    for file in files:
        path = os.path.join(root_dir, file)
        # print(prefix + path)
        file_list.append(prefix + path)
        if os.path.isdir(path):
            print_files_in_dir(path, prefix)
    return file_list


root_dir = "../DUCKDUCKGO-CRAWLER/datasets/"
final_file_list = print_files_in_dir(root_dir, "")

f = open('merged_text.txt', 'w', encoding='utf-8', newline='')
for single_file in final_file_list:
    df = pd.read_csv(single_file)
    for i in range(0, len(df)):
        print(df['text'][i])
        f.writelines(str(df['text'][i]))
f.close
