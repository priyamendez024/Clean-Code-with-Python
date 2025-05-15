# Chapter 19: Data Processing Pipelines

import pandas as pd

def clean_data(df):
    df = df.dropna()
    df['amount'] = df['amount'].astype(float)
    return df

chunks = pd.read_csv('data.csv', chunksize=1000)
for chunk in chunks:
    clean_chunk = clean_data(chunk)
    # process or save clean_chunk