import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



ad_data = pd.read_csv('advertising.csv')


from sklearn.model_selection import train_test_split

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']
11
X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

print(X.head())