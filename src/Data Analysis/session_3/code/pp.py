import pandas as pd

def chk(df):
    dtype = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({'dtype': dtype, "Num_unique": n_unique}).T



