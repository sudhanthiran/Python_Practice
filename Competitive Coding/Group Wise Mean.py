import numpy as np
import pandas as pd

d= {'key':['X','X','Y','Y','Z'],'X':np.arange(5),'Y':[3,4,5,6,7]}
data = pd.DataFrame(d,index=d['key'])
print(data.groupby(data.index).mean())

