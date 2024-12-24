import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/data.csv")
medali = pd.read_csv("D:/medali.csv")
animal = pd.read_csv("D:/animal.csv")



# 5
# Vertical bar chart untuk menampilkan umur dari setiap orang
data.plot(kind="bar",x="name",y="age",title="Age of Person")

# Banyaknya anak (num_children) dan banyaknya piaraan (num_pets) dalam
# 1 grafik vertical bar chart
data.plot(kind="bar",x="name",y=["num_children","num_pets"])


data.plot(kind="bar",x="name",y=["num_children","num_pets"])
