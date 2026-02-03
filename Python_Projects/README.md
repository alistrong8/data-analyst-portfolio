# Python Basic EDA Project

This project demonstrates foundational skills in Python for Data Analysis using the `pandas` and `matplotlib` libraries.

## 📄 File: [sales_eda.py](sales_eda.py)

### 🎯 Goal
To load a raw CSV dataset, inspect its structure, and perform basic aggregation to understand sales distribution.

### 🛠 Libraries Used
- **Pandas**: For data manipulation (DataFrames, grouping, aggregation).
- **Matplotlib**: For basic plotting.

### 🔍 Code Walkthrough
1.  **Loading Data**: Uses `pd.read_csv()` to import the `ecommerce_sales.csv`.
2.  **Inspection**: Uses `.head()`, `.info()`, and `.describe()` to check for null values and understand data types.
3.  **Aggregation**: Groups data by `Category` to calculate `Total Revenue`.
4.  **Visualization**: Generates a simple bar chart to visualize the results.

### 📊 Sample Output
```text
--- Total Revenue by Category ---
Category
Clothing       45200.50
Electronics   125000.00
Home           68000.75
Name: TotalPrice, dtype: float64
```
