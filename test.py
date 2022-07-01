import pandas as pd
import numpy as np



LABEL = ["NAM", "EMEA", "LATAM", "APAC", "OTHER"]
CAN_LIST = ["ON", "QC", "NS", "NB", "MB", "BC", "PE", "SK", "AB", "NL"]


# Getting to know how this git thing works
def loc_label (location):

    split = location.split(',')
    if len(split) == 1:
        country = split[0]
    else:
        city = split[0]
        country = split[1]

    #Make it into country
    if len(country) < 3:
        if country == "UK":
            return LABEL[1]
        return LABEL[0]
        # check where it belongs
        
    #check in dictionary

    #return the label
    return country



data = pd.read_csv(r'C:\Users\gilberto.tovar\test\data.csv')
df = pd.DataFrame(data, columns= ['Location'])
print(df.loc[1])


