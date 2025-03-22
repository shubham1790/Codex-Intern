import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Define the correct path for the dataset
csv_file_path = "house_prices.csv"

# Check if file exists, otherwise generate a sample dataset
if not os.path.exists(csv_file_path):
    print(f"Warning: The file '{csv_file_path}' was not found. Creating a sample dataset...")
    data = {
        "Size_sqft": np.random.randint(800, 4000, 100),
        "Bedrooms": np.random.randint(1, 6, 100),
        "Bathrooms": np.random.randint(1, 4, 100),
        "Location": np.random.choice(["Urban", "Suburban", "Rural"], 100),
        "Age": np.random.randint(0, 50, 100),
        "Price": np.random.randint(100000, 1000000, 100)
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)
else:
    df = pd.read_csv(csv_file_path)

# Preprocess categorical variables
encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded_locations = encoder.fit_transform(df[['Location']])
encoded_df = pd.DataFrame(encoded_locations, columns=encoder.get_feature_names_out(['Location']))
df = pd.concat([df.drop(columns=['Location']), encoded_df], axis=1)

# Split features and target variable
X = df.drop(columns=['Price'])
y = df['Price']

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Visualization: Actual vs. Predicted Prices
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, color='blue')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs. Predicted House Prices")
plt.show()
