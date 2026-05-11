import pandas as pd
import matplotlib.pyplot as plt
file=pd.read_csv("online_retail.csv")
df=file
print(df)

#Cleaning the data
print(df.info())
print(df.describe())
print(df.isnull().sum())
#df=df.dropna()#it drops the null values

#filling the null values with value 0
df["Description"]=df["Description"].fillna(0)
df["CustomerID"]=df["CustomerID"].fillna(0)

#checking the Null values
print(df.isnull().sum())

#save the file after cleaning the data as a csv file
df.to_csv("cleaned_data.csv",index=False)
print("data cleaned successfully")

# Analyze the data:

file=pd.read_csv("cleaned_data.csv")
df=file

# Convert date column
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Extract month
df["Month"] = df["InvoiceDate"].dt.to_period("M")

# Group by month
monthly_revenue = df.groupby("Month")["Revenue"].sum()

# Print results
print(monthly_revenue)

# Plot graph
monthly_revenue.plot()

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Revenue Trend")

plt.show()

#Top-selling products:
# Group by product and calculate total quantity sold
top_products = df.groupby("Description")["Quantity"].sum()

# Sort
top_products = top_products.sort_values(ascending=False)
top_10_products = top_products.head(10)
print(top_10_products)

# Create bar plot
top_10_products.plot(kind="bar", figsize=(10,5))

plt.xlabel("Products")
plt.ylabel("Quantity Sold")
plt.title("Top 10 Selling Products")
plt.show()

# Highest Revenue Months
# Top 10 highest revenue months
top_revenue_months = monthly_revenue.sort_values(ascending=False).head(10)

print(top_revenue_months)

# Bar chart
top_revenue_months.plot(kind="bar", figsize=(10,5))

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Top 10 Highest Revenue Months")

plt.xticks(rotation=45)

plt.show()