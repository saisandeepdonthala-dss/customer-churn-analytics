import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/European_Bank.csv")
print(df.head())

# Create a copy of the original dataset

df_clean = df.copy()

# Remove surname column

df_clean.drop(columns=["Surname"], inplace=True)

# Create churn status

df_clean["ChurnStatus"] = df_clean["Exited"].map({
    0: "Retained",
    1: "Churned"
})

print(df_clean.head())

# Age segmentation

df_clean["AgeGroup"] = pd.cut(
    df_clean["Age"],
    bins=[0, 29, 45, 60, float("inf")],
    labels=["<30", "30-45", "46-60", "60+"]
)

# Credit score segmentation

df_clean["CreditScoreBand"] = pd.cut(
    df_clean["CreditScore"],
    bins=[0, 579, 669, float("inf")],
    labels=["Low", "Medium", "High"]
)

# Tenure segmentation

df_clean["TenureGroup"] = pd.cut(
    df_clean["Tenure"],
    bins=[-1, 3, 7, float("inf")],
    labels=["New", "Mid-term", "Long-term"]
)

# Balance segmentation

positive_balance_median = df_clean.loc[
    df_clean["Balance"] > 0, "Balance"
].median()

def balance_segment(balance):
    if balance == 0:
        return "Zero-balance"
    elif balance <= positive_balance_median:
        return "Low-balance"
    else:
        return "High-balance"

df_clean["BalanceSegment"] = df_clean["Balance"].apply(balance_segment)

print(df_clean.shape)

churn_counts = df_clean["ChurnStatus"].value_counts()

print(churn_counts)

# Calculate churn percentage

total_customers = len(df_clean)

churned_customers = (df_clean["ChurnStatus"] == "Churned").sum()

retained_customers = (df_clean["ChurnStatus"] == "Retained").sum()

churn_percentage = (churned_customers / total_customers) * 100

retention_percentage = (retained_customers / total_customers) * 100

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)

print("Churn Percentage:", round(churn_percentage, 2), "%")
print("Retention Percentage:", round(retention_percentage, 2), "%") 

# Churn Distribution Visualization
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    data=df_clean,
    x="ChurnStatus",
    hue="ChurnStatus",
    palette={
        "Retained": "seagreen",
        "Churned": "tomato"
    },
    legend=False
)

plt.title("Customer Churn Distribution")
plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.savefig("reports/graphs/churn_distribution.png",
            dpi=300, bbox_inches="tight")
plt.show()


# Age-wise Customer Churn Analysis

age_churn = df_clean.groupby(
    "AgeGroup", observed=False
)["Exited"].mean() * 100

age_churn = age_churn.reset_index(name="ChurnPercentage")

print("\nAge-wise Churn Percentage:")
print(age_churn)

# Visualization

plt.figure(figsize=(9, 5))

ax = sns.barplot(
    data=age_churn,
    x="AgeGroup",
    y="ChurnPercentage",
    color="coral"
)

plt.title("Customer Churn Percentage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig(
    "reports/graphs/age_group_churn.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# Gender-wise Customer Churn Analysis

gender_churn = df_clean.groupby("Gender")["Exited"].mean() * 100

gender_churn = gender_churn.reset_index(name="ChurnPercentage")

print("\nGender-wise Churn Percentage:")
print(gender_churn)

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=gender_churn,
    x="Gender",
    y="ChurnPercentage",
    hue="Gender",
    palette="Set2",
    legend=False
)

plt.title("Customer Churn Percentage by Gender")
plt.xlabel("Gender")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/gender_churn.png", dpi=300, bbox_inches="tight")
plt.show()


# Geography-wise Customer Churn Analysis

geo_churn = df_clean.groupby("Geography")["Exited"].mean() * 100

geo_churn = geo_churn.reset_index(name="ChurnPercentage")

print("\nGeography-wise Churn Percentage:")
print(geo_churn)

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=geo_churn,
    x="Geography",
    y="ChurnPercentage",
    hue="Geography",
    palette="Set2",
    legend=False
)

plt.title("Customer Churn Percentage by Geography")
plt.xlabel("Country")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/geography_churn.png", dpi=300, bbox_inches="tight")
plt.show()



# Customer Activity-wise Churn Analysis

activity_churn = df_clean.groupby(
    "IsActiveMember"
)["Exited"].mean() * 100

activity_churn = activity_churn.reset_index(
    name="ChurnPercentage"
)

activity_churn["CustomerType"] = activity_churn[
    "IsActiveMember"
].map({
    1: "Active",
    0: "Inactive"
})

print("\nActivity-wise Churn Percentage:")
print(activity_churn[["CustomerType", "ChurnPercentage"]])

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=activity_churn,
    x="CustomerType",
    y="ChurnPercentage",
    hue="CustomerType",
    palette="Set2",
    legend=False
)

plt.title("Customer Churn by Activity Status")
plt.xlabel("Customer Activity")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/activity_churn.png", dpi=300, bbox_inches="tight")
plt.show()


# Credit Score-wise Customer Churn Analysis

credit_churn = df_clean.groupby(
    "CreditScoreBand",
    observed=False
)["Exited"].mean() * 100

credit_churn = credit_churn.reset_index(
    name="ChurnPercentage"
)

print("\nCredit Score-wise Churn Percentage:")
print(credit_churn)

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=credit_churn,
    x="CreditScoreBand",
    y="ChurnPercentage",
    hue="CreditScoreBand",
    palette="viridis",
    legend=False
)

plt.title("Customer Churn by Credit Score")
plt.xlabel("Credit Score Band")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/credit_score_churn.png", dpi=300, bbox_inches="tight")
plt.show()


# Tenure-wise Customer Churn Analysis

tenure_churn = df_clean.groupby(
    "TenureGroup",
    observed=False
)["Exited"].mean() * 100

tenure_churn = tenure_churn.reset_index(
    name="ChurnPercentage"
)

print("\nTenure-wise Churn Percentage:")
print(tenure_churn)

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=tenure_churn,
    x="TenureGroup",
    y="ChurnPercentage",
    hue="TenureGroup",
    palette="viridis",
    legend=False
)

plt.title("Customer Churn by Tenure Group")
plt.xlabel("Customer Tenure")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/tenure_churn.png", dpi=300, bbox_inches="tight")
plt.show()


# Balance-wise Customer Churn Analysis

balance_churn = df_clean.groupby(
    "BalanceSegment"
)["Exited"].mean() * 100

balance_churn = balance_churn.reset_index(
    name="ChurnPercentage"
)

print("\nBalance-wise Churn Percentage:")
print(balance_churn)

# Visualization

plt.figure(figsize=(9, 5))

ax = sns.barplot(
    data=balance_churn,
    x="BalanceSegment",
    y="ChurnPercentage",
    hue="BalanceSegment",
    palette="viridis",
    legend=False
)

plt.title("Customer Churn by Account Balance")
plt.xlabel("Balance Segment")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/balance_churn.png", dpi=300, bbox_inches="tight")
plt.show()

# Number of Products-wise Customer Churn Analysis
product_churn = df_clean.groupby(
    "NumOfProducts"
)["Exited"].mean() * 100

product_churn = product_churn.reset_index(
    name="ChurnPercentage"
)

print("\nNumber of Products-wise Churn Percentage:")
print(product_churn)

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=product_churn,
    x="NumOfProducts",
    y="ChurnPercentage",
    hue="NumOfProducts",
    palette="viridis",
    legend=False
)

plt.title("Customer Churn by Number of Products")
plt.xlabel("Number of Bank Products")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/products_churn.png", dpi=300, bbox_inches="tight")
plt.show()

# Credit Card-wise Customer Churn Analysis
card_churn = df_clean.groupby(
    "HasCrCard"
)["Exited"].mean() * 100

card_churn = card_churn.reset_index(
    name="ChurnPercentage"
)

card_churn["CreditCardStatus"] = card_churn[
    "HasCrCard"
].map({
    1: "Has Credit Card",
    0: "No Credit Card"
})

print("\nCredit Card-wise Churn Percentage:")
print(card_churn[["CreditCardStatus", "ChurnPercentage"]])

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=card_churn,
    x="CreditCardStatus",
    y="ChurnPercentage",
    hue="CreditCardStatus",
    palette="Set2",
    legend=False
)

plt.title("Customer Churn by Credit Card Ownership")
plt.xlabel("Credit Card Status")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/credit_card_churn.png", dpi=300, bbox_inches="tight")
plt.show()


# Salary Segmentation
df_clean["SalaryGroup"] = pd.qcut(
    df_clean["EstimatedSalary"],
    q=3,
    labels=["Low Salary", "Medium Salary", "High Salary"]
)

# Salary-wise Churn Analysis
salary_churn = df_clean.groupby(
    "SalaryGroup",
    observed=False
)["Exited"].mean() * 100

salary_churn = salary_churn.reset_index(
    name="ChurnPercentage"
)

print("\nSalary-wise Churn Percentage:")
print(salary_churn)

# Visualization

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=salary_churn,
    x="SalaryGroup",
    y="ChurnPercentage",
    hue="SalaryGroup",
    palette="viridis",
    legend=False
)

plt.title("Customer Churn by Estimated Salary")
plt.xlabel("Salary Group")
plt.ylabel("Churn Percentage (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()
plt.savefig("reports/graphs/salary_churn.png", dpi=300, bbox_inches="tight")
plt.show()


# Customer Age vs Churn Analysis

age_analysis = df_clean.groupby("Age")["Exited"].mean() * 100

age_analysis = age_analysis.reset_index(
    name="ChurnPercentage"
)

print("\nAge-wise Detailed Churn Analysis:")
print(age_analysis.head(10))

# Visualization

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=age_analysis,
    x="Age",
    y="ChurnPercentage",
    marker="o"
)

plt.title("Customer Churn Percentage by Individual Age")
plt.xlabel("Customer Age")
plt.ylabel("Churn Percentage (%)")

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("reports/graphs/age_wise_churn.png", dpi=300, bbox_inches="tight")
plt.show()


# Correlation Analysis

numeric_columns = [
    "CreditScore",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "EstimatedSalary",
    "Exited"
]

correlation_matrix = df_clean[numeric_columns].corr()

print("\nCorrelation with Customer Churn:")
print(
    correlation_matrix["Exited"]
    .sort_values(ascending=False)
)

# Correlation Heatmap

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap - Customer Churn")

plt.tight_layout()
plt.savefig("reports/graphs/correlation_churn.png", dpi=300, bbox_inches="tight")
plt.show()

# Customer Count by Number of Products

product_summary = df_clean.groupby(
    "NumOfProducts"
).agg(
    TotalCustomers=("CustomerId", "count"),
    ChurnedCustomers=("Exited", "sum"),
    ChurnPercentage=("Exited", "mean")
)

product_summary["ChurnPercentage"] *= 100

print("\nCustomer Count by Number of Products:")
print(product_summary.round(2))