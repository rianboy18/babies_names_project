# %load q01_create_dict/build.py
import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q01_create_dict(data):
    names_dict = {'Name':data['Name'],
                 'Count':data['Count']}
    return names_dict



c=q01_create_dict(data)
c


