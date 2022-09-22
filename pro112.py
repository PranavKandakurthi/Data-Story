import pandas as pd
import statistics as st
import plotly.express as px
import csv

df= pd.read_csv("savings_data_final.csv")
fig=px.scatter(df,y=df["quant_saved"],color=df["rem_any"])
fig.show()

data=df["quant_saved"].tolist()
mean_population = st.mean(data)
median_population = st.median(data)
mode_population = st.mode(data)
stdev_population = st.stdev(data)
print("Mean of savings -",mean_population)
print("Mode of savings -",mode_population)
print("Median of savings -",median_population)
print("Stdev of savings -",stdev_population)

reminded_savings=[]
non_reminded_savings=[]
for data in savings_data:
  if int(data[3])==1:
    reminded_savings.append(float(data[0]))
  else:
    non_reminded_savings.append(float(data[0]))

mean_reminded= st.mean(reminded_savings)
median_reminded= st.median(reminded_savings)
mode_reminded= st.mode(reminded_savings)
stdev_reminded= st.stdev(reminded_savings)

mean_non_reminded= st.mean(non_reminded_savings)
median_non_reminded= st.median(non_reminded_savings)
mode_non_reminded= st.mode(non_reminded_savings)
stdev_non_reminded= st.stdev(non_reminded_savings)

print("Mean of reminded savings -",mean_reminded)
print("Mode of reminded savings -",mode_reminded)
print("Median of reminded savings -",median_reminded)
print("Stdev of reminded savings -",stdev_reminded)
print(" ")
print("Mean of non reminded savings -",mean_non_reminded)
print("Mode of non reminded savings -",mode_non_reminded)
print("Median of non reminded savings -",median_non_reminded)
print("Stdev of non reminded savings -",stdev_non_reminded)

import numpy as np

age=[]
savings=[]

for data in savings_data:
  if float(data[5])!=0:
    age.append(float(data[5]))
    savings.append(float(data[0]))

correlation= np.corrcoef(age,savings)
print(f"correlation between the age and savings {correlation[0,1]}")