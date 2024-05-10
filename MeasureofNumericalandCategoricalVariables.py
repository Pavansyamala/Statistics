import pandas as pd
import numpy as np 

data = pd.read_csv('student-por.csv')

print(data.head())

print(data['sex'].count())
print(data['school'].count())
