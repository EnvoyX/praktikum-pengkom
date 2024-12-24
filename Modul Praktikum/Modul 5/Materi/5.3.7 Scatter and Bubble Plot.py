import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/data.csv")
medali = pd.read_csv("D:/medali.csv")
animal = pd.read_csv("D:/animal.csv")





# Relationship antara variable gold dan total dalam grafik scatter plot
# dan tunjukkan adanya korelasi positif
medali.plot(kind="scatter", x="gold", y="total")



# Banyaknya total medali dikaitkan dengan perolehan nilai medali emas (gold)
# pada sumbu x dan perolehan medali perak (silver) pada sumbu y
# dalam grafik bubble plot
medali.plot(kind="scatter",x="gold", y="silver",sizes=medali["total"], color="orange")