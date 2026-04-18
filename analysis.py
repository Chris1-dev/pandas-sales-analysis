import pandas as pd
import matplotlib.pyplot as plt

# ======================
# Load Data
# ======================
df = pd.read_csv("sales.csv")

# ======================
# Data Processing
# ======================
df["total"] = df["price"] * df["quantity"]

# ======================
# Analysis
# ======================
total_sales = df["total"].sum()
average_price = df["price"].mean()
best_selling = df.loc[df["quantity"].idxmax()]
sales_by_category = df.groupby("category")["total"].sum()

# ======================
# Print Results
# ======================
print("Total Sales:", total_sales)
print("Average Price:", average_price)

print("\nBest Selling Product:")
print(best_selling)

print("\nSales by Category:")
print(sales_by_category)

# ======================
# Visualization
# ======================
sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()