
from pathlib import Path

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Getting the project folder and dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "European_Bank.csv"

st.set_page_config(
    page_title="Customer Churn Analysis",
    layout="wide"
)

st.title("Customer Churn Analysis Dashboard")

st.write(
    "This dashboard shows customer churn in a European bank. "
    "It helps us understand how many customers have left the bank "
    "and which groups have more customers leaving."
)

# Reading the dataset
@st.cache_data
def load_data():
    return pd.read_csv(file_path)


try:
    df = load_data()
except FileNotFoundError:
    st.error("Dataset not found. Please check the data folder.")
    st.stop()

# Adding customer status
df["ChurnStatus"] = df["Exited"].map({
    0: "Retained",
    1: "Churned"
})

# Dividing customers into age groups
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 29, 45, 60, float("inf")],
    labels=["Under 30", "30-45", "46-60", "60+"]
)

# Dividing customers based on their balance
positive_balance = df.loc[df["Balance"] > 0, "Balance"]

if len(positive_balance) > 0:
    balance_limit = positive_balance.median()
else:
    balance_limit = 0


def balance_group(balance):
    if balance == 0:
        return "Zero balance"
    elif balance <= balance_limit:
        return "Low balance"
    else:
        return "High balance"


df["BalanceGroup"] = df["Balance"].apply(balance_group)

# Filters
st.sidebar.header("Choose Filters")

countries = sorted(df["Geography"].dropna().unique())

selected_countries = st.sidebar.multiselect(
    "Select Country",
    countries,
    default=countries
)

ages = ["Under 30", "30-45", "46-60", "60+"]

selected_ages = st.sidebar.multiselect(
    "Select Age Group",
    ages,
    default=ages
)

genders = sorted(df["Gender"].dropna().unique())

selected_genders = st.sidebar.multiselect(
    "Select Gender",
    genders,
    default=genders
)

activity = st.sidebar.selectbox(
    "Account Activity",
    ["All", "Active", "Inactive"]
)

# Applying the selected filters
data = df[
    (df["Geography"].isin(selected_countries))
    & (df["AgeGroup"].astype(str).isin(selected_ages))
    & (df["Gender"].isin(selected_genders))
].copy()

if activity == "Active":
    data = data[data["IsActiveMember"] == 1]
elif activity == "Inactive":
    data = data[data["IsActiveMember"] == 0]

# Showing the main customer details
st.subheader("Customer Details")

total_customers = len(data)
churned = int((data["Exited"] == 1).sum())
retained = int((data["Exited"] == 0).sum())

if total_customers > 0:
    churn_percentage = (churned / total_customers) * 100
else:
    churn_percentage = 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Customers Who Left", f"{churned:,}")
col3.metric("Customers Staying", f"{retained:,}")
col4.metric("Churn Percentage", f"{churn_percentage:.2f}%")

if total_customers == 0:
    st.warning("No customers found for the selected filters.")
    st.stop()

# Churn in each country
st.subheader("Churn in Each Country")

country_data = (
    data.groupby("Geography")["Exited"]
    .mean()
    .mul(100)
)

fig, ax = plt.subplots()
country_data.plot(kind="bar", ax=ax)
ax.set_xlabel("Country")
ax.set_ylabel("Churn Percentage")
ax.set_title("Customer Churn by Country")
plt.xticks(rotation=0)
st.pyplot(fig)
plt.close(fig)

# Churn based on age
st.subheader("Churn Based on Age")

age_data = (
    data.groupby("AgeGroup", observed=False)["Exited"]
    .mean()
    .mul(100)
)

fig, ax = plt.subplots()
age_data.plot(kind="bar", ax=ax)
ax.set_xlabel("Age Group")
ax.set_ylabel("Churn Percentage")
ax.set_title("Customer Churn by Age Group")
plt.xticks(rotation=0)
st.pyplot(fig)
plt.close(fig)

# Churn based on years with the bank
st.subheader("Churn Based on Years with the Bank")

tenure_data = (
    data.groupby("Tenure")["Exited"]
    .mean()
    .mul(100)
)

fig, ax = plt.subplots()
tenure_data.plot(kind="line", marker="o", ax=ax)
ax.set_xlabel("Years with the Bank")
ax.set_ylabel("Churn Percentage")
ax.set_title("Customer Churn by Tenure")
st.pyplot(fig)
plt.close(fig)

# High-balance customer details
st.subheader("High-Balance Customers")

high_balance = data[data["BalanceGroup"] == "High balance"]

high_balance_total = len(high_balance)
high_balance_churned = int((high_balance["Exited"] == 1).sum())

if high_balance_total > 0:
    high_balance_percentage = (
        high_balance_churned / high_balance_total
    ) * 100
else:
    high_balance_percentage = 0

col1, col2, col3 = st.columns(3)

col1.metric("High-Balance Customers", f"{high_balance_total:,}")
col2.metric("High-Balance Customers Who Left", f"{high_balance_churned:,}")
col3.metric("Churn Percentage", f"{high_balance_percentage:.2f}%")

st.write(
    "Here, I have considered customers with a balance above the "
    "median positive balance as high-balance customers. This is "
    "only a simple way to identify customers with higher balances."
)

# Showing customer records
with st.expander("View Customer Records"):
    st.dataframe(data, use_container_width=True)

st.write("---")
st.write("Project completed as part of the Unified Mentor internship.")
