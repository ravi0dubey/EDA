import pandas as pd
import numpy as np
import seaborn as sns
import os
import pandas_profiling
import pandas.plotting._matplotlib as plt


df1 =pd.read_csv('D:\\Study\\Data Science\\Python\\ineuron\\Data_Set\\fitbit.csv')
df1.head(5)

profile = df1.profile_report(title="fitbit_EDA")
profile.to_file(output_file="fitbit_EDA.html")