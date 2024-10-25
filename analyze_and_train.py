import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import os

df = pd.read_csv('CollegeDistance.csv')

print("Podgląd danych:")
print(df.head())

missing_values = df.isnull().sum()
print(f"Brakujące wartości: \n{missing_values}")

print("Opis statystyczny zmiennych:")
print(df.describe())

output_dir = './output'
os.makedirs(output_dir, exist_ok=True)

plt.figure(figsize=(10,6))
df.hist(bins=50, figsize=(20,15))
plt.savefig(f'{output_dir}/data_distribution.png')

X = df.drop('score', axis=1)
y = df['score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse}')
print(f'R²: {r2}')

with open(f'{output_dir}/model_performance.txt', 'w') as f:
    f.write(f'MSE: {mse}\n')
    f.write(f'R²: {r2}\n')
