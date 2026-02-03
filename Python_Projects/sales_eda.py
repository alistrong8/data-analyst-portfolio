import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Dataset
# We are using the synthetic e-commerce data we generated
df = pd.read_csv('../Datasets/ecommerce_sales.csv')

# 2. Inspect the Data
print("--- First 5 Rows ---")
print(df.head())

print("\n--- Data Info (Types & Nulls) ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# 3. Basic Analysis
# Question: What is the total revenue per category?
category_revenue = df.groupby('Category')['TotalPrice'].sum()
print("\n--- Total Revenue by Category ---")
print(category_revenue)

# 4. Simple Visualization
# Plotting the category revenue
category_revenue.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue ($)')
plt.tight_layout()

# Save the plot
plt.savefig('category_revenue_plot.png')
print("\nPlot saved as 'category_revenue_plot.png'")
