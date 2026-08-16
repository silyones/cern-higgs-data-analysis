import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/higgs_4lepton.csv")
'''
#print(df)
print("first few rows of dataset:")
print(df.head())

print("\nshape of dataset:")
print(df.shape)

print("\ncolumns in dataset")
print(df.columns.tolist())
'''

#to print charge of the 4 leptons 
print("\ncharge of the 4 leptons:")
print(df[["Event","Q1","Q2","Q3","Q4"]])