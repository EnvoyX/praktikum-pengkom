import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/data.csv")
medali = pd.read_csv("D:/medali.csv")
animal = pd.read_csv("D:/animal.csv")



# Histogram orang berdasarkan kelompok umur: 0-20; 21-40; 41-60; 61-80; 81-100
data[["age"]].plot(kind="hist",bins=[0,20,40,60,80,100],rwidth=0.8)