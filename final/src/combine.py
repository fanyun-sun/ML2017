import os
import pandas as pd
import numpy as np
import sys

output_file = sys.argv[1]

res = pd.Series(np.arange(7662))
lst = [2, 234, 34, 3451, 4]
for seed in lst:
    filename = '{}'.format(seed)
    df = pd.read_csv(os.path.join('CSVs',filename))
    res += df['price_doc']/len(lst)

    if seed == lst[-1]:
        df['price_doc']= res
        #df.to_csv(output_file, index=False)


df_lst = []
sz = int(df.shape[0]/3)
print(sz)
res = [-0.00726728669792, -0.0326138809059, np.log(0.99)/2 , 0.0236381324083]
print(res)

df['price_doc'] = np.log1p(df['price_doc'])

for i in range(4):

    if i == 0:
        tmp = df.iloc[:1000]
    elif i == 1:
        tmp = df.iloc[1000:sz]
    elif i == 2:
        tmp = df.iloc[sz:2*sz]
    elif i == 3:
        tmp = df.iloc[2*sz:3*sz]

    tmp['price_doc'] += res[i]
    df_lst.append( tmp )

#df = pd.concat(df_lst)
df['price_doc'] = np.exp(df['price_doc'])-1
df.to_csv(output_file, index=False)
