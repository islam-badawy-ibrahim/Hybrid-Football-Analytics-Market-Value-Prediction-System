import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

data_dict = {
    'Age': [19, 21, 25, 28, 32, 23, 20, 27, 24, 30, 18, 22, 26, 29, 31],
    'Overall': [70, 75, 85, 88, 90, 80, 72, 84, 78, 86, 65, 77, 83, 89, 91],
    'Potential': [85, 88, 87, 89, 90, 85, 86, 85, 84, 86, 82, 87, 86, 91, 92],
    'Value_Euro': [5000000, 15000000, 60000000, 80000000, 70000000, 30000000, 8000000, 45000000, 20000000, 55000000, 2000000, 18000000, 40000000, 95000000, 105000000]
}

df = pd.DataFrame(data_dict)

X = df[['Age', 'Overall', 'Potential']]
y = df['Value_Euro']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Model Training Complete.")
print(f"Accuracy (R^2 Score): {accuracy:.4f}")

def predict_new_player(age, overall, potential):
    new_data = np.array([[age, overall, potential]])
    new_data_scaled = scaler.transform(new_data)
    prediction = model.predict(new_data_scaled)
    return prediction[0]

sample_val = predict_new_player(22, 82, 90)
print(f"Predicted Value for Sample Player (22yrs, 82 Ov, 90 Pot): €{sample_val:,.2f}")

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.regplot(x='Overall', y='Value_Euro', data=df, color='teal', marker='o', scatter_kws={'s':100})
plt.title('Advanced Player Value Prediction Analysis', fontsize=15)
plt.xlabel('Overall Rating', fontsize=12)
plt.ylabel('Market Value (Euro)', fontsize=12)
plt.show()
