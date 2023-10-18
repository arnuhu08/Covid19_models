import pandas as pd
import matplotlib.pyplot as plt
import numpy as numpy
data = pd.read_csv("Covid Data.csv")
df = data.drop(['INTUBED','ICU'], axis=1)
print(df.head(10))
# print(sum(df["PREGNANT"]==97))