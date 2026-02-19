import pandas as pd

def chk(df):
    dtype = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({'dtype': dtype, "Num_unique": n_unique}).T

def chk_nulls(df):
    null = df.isnull().sum()
    ratio = null / df.shape[0]
    return pd.DataFrame({'null': null, "ratio": ratio}).T