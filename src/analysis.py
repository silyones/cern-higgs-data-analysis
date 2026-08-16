import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("data/raw/higgs_4lepton.csv")

print(df)

print("first few rows of dataset:")
print(df.head())

print("\nshape of dataset:")
print(df.shape)

print("\ncolumns in dataset")
print(df.columns.tolist())

#1. To calculate total charge (FYI — axis=1 means to calculate sum across row)

#to print charge of the 4 leptons 
print("\ncharge of the 4 leptons:")
print(df[["Event","Q1","Q2","Q3","Q4"]])


df["total_charge"] = df[["Q1","Q2","Q3","Q4"]].sum(axis=1)
print(df[["Event","Q1","Q2","Q3","Q4","total_charge"]])    

#2. To calculate energy

#print energy
print("\nEnergy in lepton:")
print(df[["Event","E1","E2","E3","E4"]])


#3. Visualize energy in leptons
#bar plot
energies = df[["E1", "E2", "E3", "E4"]]
energies.plot(kind="bar")
plt.xticks(range(len(df)), df["Event"], rotation=90)
plt.xlabel("Collision event")
plt.ylabel("Energy (GeV)")
plt.title("Energy of the Four Leptons")
plt.legend(["Lepton 1", "Lepton 2", "Lepton 3", "Lepton 4"])
plt.tight_layout()
plt.savefig("results/figures/lepton_energy.png")
plt.show()


#4. Calculate pt (pt = √px1² + py1²)
cal_pt1=np.sqrt((df["px1"]**2 + df["py1"]**2))
print("calculated pt value for lepton 1:")
print(cal_pt1)

