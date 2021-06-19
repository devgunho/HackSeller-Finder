# %%
import pandas as pd
import os

from pandas.core.frame import DataFrame
# %%


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


# %%
root_dir = "../DUCKDUCKGO-CRAWLER/datasets/"
final_file_list = print_files_in_dir(root_dir, "")
print("target list:", len(final_file_list), final_file_list)

# %%
result_df = DataFrame()

for single_file in final_file_list:
    df = pd.read_csv(single_file)
    category_str = single_file.split('/')[-1].split('.')[0]
    df.insert(0, 'category', category_str)
    # print(df)
    result_df = pd.concat([result_df, df])

result_df.to_csv('merged_text.csv', index=False)
