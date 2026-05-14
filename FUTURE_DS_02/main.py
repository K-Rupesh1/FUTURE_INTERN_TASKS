import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

#Clean and organize customer Data:

#print(df)
#print(df.count())
print(df.head())
print(df.describe())
print(df.isnull().sum())
df=df.drop_duplicates()
#print(df.count())
df.to_csv("claned dataset.csv",index=False)

# Analyze Churn rates and retention trends:
df=df.sort_values("tenure")
print(df)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
churn_rate = df["Churn"].mean() * 100
print("Overall Churn Rate:", round(churn_rate, 2), "%")
contract_churn = df.groupby("Contract")["Churn"].mean() * 100
print(round(contract_churn),2)
contract_churn.plot(kind="bar")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.title("Churn Rate by Contract Type")

plt.show()


retention_rate = (1 - df["Churn"].mean()) * 100
print("Retention Rate:", round(retention_rate, 2), "%")
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=["0-1 Year", "1-2 Years", "2-4 Years", "4-6 Years"])
retention_by_tenure = df.groupby("TenureGroup")["Churn"].mean()
retention_by_tenure = (1 - retention_by_tenure) * 100
retention_by_tenure=round(retention_by_tenure,2)
print(retention_by_tenure)
retention_by_tenure.plot(kind="line", marker="o")
plt.xlabel("Tenure Group")
plt.ylabel("Retention Rate (%)")
plt.title("Retention Trend by Tenure")

plt.show()