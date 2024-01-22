import pandas as pd
import os
dataframes = {}
directory = '/home/Web-Scraper/CSV Files'
for filename in os.listdir(directory):
    # if 'PC' in filename:
    f = os.path.join(directory,filename)
    df = pd.read_csv(f)
    df = df.drop_duplicates()
    df = df.fillna('N/A')
    dataframes[filename] = df



