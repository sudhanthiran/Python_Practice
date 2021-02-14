import pandas as pd

dframe = pd.DataFrame({'col1':['A']*3+['B']*4+['C','B','A'],'col2':[2,3,4,2,4,2,1,3,4,4]})

print(dframe.drop_duplicates(subset='col1',keep='first'))

print(dframe)