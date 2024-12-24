import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/data.csv")
medali = pd.read_csv("D:/medali.csv")
animal = pd.read_csv("D:/animal.csv")



# Pertumbuhan populasi beruang (Bears) dari tahun ke tahun dalam line chart
animal.plot(kind="line",x="Year",y="Bears")


# Pertumbuhan populasi beruang (Bears), lumba -lumba (Dolphins), dan ikan paus (Whales)

# dari tahun ke tahun dalam 1 line chart
animal.plot(kind="line",x="Year", y=["Bears","Dolphins","Whales"])