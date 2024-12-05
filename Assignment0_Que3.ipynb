import pandas as pd
import numpy as np
df = pd.read_csv('IITK_Courses_Report.csv')
df.isnull()
non_numerical_columns= ['Student Name','Course']
df.dropna(subset = non_numerical_columns, inplace=True)
numerical_columns= ['Marks (%)','Attendance (%)']
for col in numerical_columns:
    for i in df[df[col].isnull()].index:
        above = df.loc[i - 1, col] 
        below = df.loc[i + 1, col] 
        df.loc[i, col] = np.sqrt(above * below)
df.to_csv('IITK_Courses_Report.csv')