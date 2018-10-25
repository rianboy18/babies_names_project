# %load q02_top_names/build.py
import pandas as pd
from collections import Counter
from greyatomlib.babies_names_project.q01_create_dict.build import q01_create_dict


path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q02_top_names(path):
    df=Counter(data)
    mc = df.most_common(25)
    
    names_dict = (mc[0],mc[1])
                  
    return names_dict

c=q02_top_names(path)
c


