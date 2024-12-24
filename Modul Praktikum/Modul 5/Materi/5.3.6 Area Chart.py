import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/data.csv")
medali = pd.read_csv("D:/medali.csv")
animal = pd.read_csv("D:/animal.csv")



# Pertumbuhan populasi lumba -lumba (Dolphins) dari tahun ke tahun
# dalam area chart
animal.plot(kind="area",x="Year", y="Dolphins")

# Pertumbuhan populasi lumba -lumba (Dolphins), ikan paus (Whales), dan beruang(Bears),
# dari tahun ke tahun dalam stacked area chart
animal.plot(kind="area",x="Year", y=["Dolphins","Whales","Bears"])