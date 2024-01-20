import pandas as pd
import os

console_data = {}
names_list = []
directory = 'CSV Files'
for filename in os.listdir(directory):
    print(filename)
    # if 'PC' in filename:
    f = os.path.join(directory,filename)
    df = pd.read_csv(f)
    df = df.drop_duplicates(keep=False, subset = ['Game'])
    df = df.fillna('N/A')
    modified_name = filename.replace('List of best-selling ', '')
    console_name = modified_name.replace(' video games.csv', '')
    console_data[console_name] = df.to_dict('records')
    names_list = names_list + df['Game'].tolist()



