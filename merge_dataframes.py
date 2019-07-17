'''
Testing the usage of passing unlimited parameters to a function.
Using concat() is like SQL Union All.
'''

import pandas as pd

def merge_dataframes(*args):
    df = pd.concat(args, sort = True)
    df = df.reset_index(drop = True)

    return df

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
            'age': [42, 52, 36, 24, 73],
            'preTestScore': [4, 24, 31, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70]
}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df2 = pd.DataFrame(raw_data)
df2.columns = ['last_name', 'first_name', 'age', 'preTestScore', 'postTestScore']


dff = merge_dataframes(df, df2, df)
print(dff)
