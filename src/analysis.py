import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("data/raw/higgs_4lepton.csv")

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


#5. Calculate M invariant mass (M=√E² - px² - px² - pz²)
#first we need to calcualte total e,px,py,pz)
df["px"] = df[["px1","px2","px3","px4"]].sum(axis=1)
df["py"] = df[["py1","py2","py3","py4"]].sum(axis=1)
df["pz"] = df[["pz1","pz2","pz3","pz4"]].sum(axis=1)
df["E"] = df[["E1","E2","E3","E4"]].sum(axis=1)
df["cal_M"] = np.sqrt(df["E"]**2 - df["px"]**2 - df["py"]**2 - df["pz"]**2)

print("calculated M:")
print(df["cal_M"])


#6. visualizing invariant mass and event
#bar plot
df[["cal_M","M"]].plot(kind="bar")
plt.xticks(range(len(df)), df["Event"], rotation=90)
plt.xlabel("Collision event")
plt.ylabel("Invariant mass M(GeV)")
plt.title("Invariant mass M of Four Lepton")
plt.legend(["calculated M","real M"])
plt.tight_layout()
plt.savefig("results/figures/lepton_invariant_mass.png")
plt.show()
