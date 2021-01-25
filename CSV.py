import csv
import pandas as pd
import numpy as np

with open("D:\\EAI\\Parent Child\\feed file.csv","r") as access_csv:
    #reader = csv.DictReader(access_csv)
    reader = csv.reader(access_csv)
    dict_list = []
    ids=[]
    pids=[]
    for line in reader:
        dict_list.append(line)
        ids.append(line[0])
        pids.append(line[1])

# print(ids)
# print(pids)

# for i in range(0,len(ids)):
#     print("Child id: "+ ids[i] + " Parent id: "+ pids[i])

df= pd.DataFrame({'id':pd.Series(ids),'parent_id': pd.Series(pids)})

#print(df)

