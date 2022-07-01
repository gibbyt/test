from cProfile import label
import pandas as pd
import numpy as np
import openpyxl


def loc_label(location):
    dict = pd.read_excel(r"Countries and Regions.xlsx")

    split = location.split(',')
    if len(split) == 1:
        country = split[0]
    else:
        city = split[0]
        country = split[1]
    
    #Inferecnce that all acronyms are either the UK or in NA
    if len(country) < 4:
        if "UK" in country:
            return "EMEA"
        return "NA"

    #check in dictionary
    for i in range(len(dict)):
        if dict.loc[i, "Country"] in country:
            return dict.loc[i, "Region"]
    #return the label
    return country


df = pd.read_csv(r'data copy.csv')

list = []
for i in range(len(df)):
    label = loc_label(df.loc[i, "Location"])
    list.append(label)
df["Region"] = list







