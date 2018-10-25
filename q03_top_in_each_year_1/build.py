# %load q03_top_in_each_year_1/build.py

import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q03_top_in_each_year_1(data):
    names_dict = {'Name':data['Name'],
                 'Count':data['Count'],
                 'Year':data['Year']}
    return names_dict
    


