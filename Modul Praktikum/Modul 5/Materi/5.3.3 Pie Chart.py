import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/data.csv")
medali = pd.read_csv("D:/medali.csv")
animal = pd.read_csv("D:/animal.csv")


# Komposisi banyaknya orang berdasarkan negara
data["state"].value_counts().plot(kind = "pie")