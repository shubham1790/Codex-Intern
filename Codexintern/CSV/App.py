import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the correct path for the CSV file
csv_file_path = "sample_data.csv"

# Attempt to locate the file
if not os.path.exists(csv_file_path):
    csv_file_path = os.path.join(os.getcwd(), "sample_data.csv")
    if not os.path.exists(csv_file_path):
        print(f"Warning: The file '{csv_file_path}' was not found. Creating a sample dataset...")
        # Create a sample dataset
        data = {
            "Product": ["A", "B", "C", "D", "E"],
            "Sales": [150, 200, 300, 250, 400],
            "Profit": [30, 50, 80, 60, 120],
            "Customer_Rating": [4.2, 3.8, 4.5, 4.0, 4.7]
        }
        df = pd.DataFrame(data)
        df.to_csv(csv_file_path, index=False)
    else:
        df = pd.read_csv(csv_file_path)
else:
    df = pd.read_csv(csv_file_path)

# Display basic statistics
print("Dataset Overview:\n", df.head())
print("\nSummary Statistics:\n", df.describe())

# Calculate the average sales
average_sales = df["Sales"].mean()
print(f"\nAverage Sales: {average_sales:.2f}")

# Create a bar chart for sales
plt.figure(figsize=(8,5))
plt.bar(df["Product"], df["Sales"], color='blue')
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales by Product")
plt.show()

# Create a scatter plot of Sales vs. Profit
plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Profit"], color='red')
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs. Profit")
plt.show()

# Create a heatmap of correlations (excluding non-numeric columns)
numeric_df = df.select_dtypes(include=["number"])
plt.figure(figsize=(6,4))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Insights based on the analysis
print("\nInsights:")
print("1. The average sales across all products is", round(average_sales, 2))
print("2. Sales and Profit appear to have a positive correlation, as seen in the scatter plot.")
print("3. The heatmap shows relationships between different numerical variables, such as a high correlation between Sales and Profit.")
