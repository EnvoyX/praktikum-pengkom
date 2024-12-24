import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("D:/data.csv")
medali = pd.read_csv("D:/medali.csv")
animal = pd.read_csv("D:/animal.csv")


# Banyaknya data per jenis kelamin (gender) per negara bagian (state)
data.groupby(["gender","state"])["name"].size().unstack().plot(kind="bar",
stacked=True)


# Banyaknya anak (num_children) dan banyaknya piaraan (num_pets)
# dalam 1 grafik stacked bar chart
data.plot(kind="bar", x="name", y=["num_children","num_pets"], stacked=True)


