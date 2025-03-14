from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1.2, 3.4], [4.4, 2.2], [3.7, 4.3], [5.8, 6.0]])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("Standartlaştırılmış veri: ")
print(scaled_data)
