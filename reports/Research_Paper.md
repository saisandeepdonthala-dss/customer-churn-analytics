
# Customer Segmentation & Churn Pattern Analytics in European Banking

## 1. Introduction

Customer churn is one of the common problems faced by banks. It happens when customers stop using the bank's services or close their accounts.

Keeping existing customers is important for banks because losing customers can affect their business and revenue. By studying customer data, banks can understand why some customers leave and which groups are more likely to leave.

In this project, I have analysed customer data from a European bank. I used Python, Pandas, NumPy, Matplotlib and Seaborn to study customer details and identify patterns related to churn.

The main aim of this project is to understand customer behaviour and find the groups where churn is higher.

## 2. Objectives of the Project

The main objectives of this project are:

- To calculate the overall customer churn percentage.
- To identify which age groups have more customers leaving.
- To compare customer churn across different countries.
- To understand the relationship between account activity and churn.
- To study churn based on credit score, balance, salary and tenure.
- To identify customers with higher account balances who have left the bank.
- To provide useful findings that may help banks improve customer retention.

## 3. Dataset Description

For this project, I used the European Bank customer dataset provided for the internship.

The dataset contains 10,000 customer records and 14 columns.

It includes customer information such as:

- Customer ID
- Credit Score
- Geography
- Gender
- Age
- Tenure
- Account Balance
- Number of Products
- Credit Card Details
- Account Activity
- Estimated Salary
- Customer Exit Status

The `Exited` column is used to identify whether a customer has left the bank.

- 0 means the customer stayed.
- 1 means the customer left.

The dataset was used for analysis and visualization.


## 4. Data Cleaning and Preparation

Before starting the analysis, I checked the dataset to understand its structure and identify the columns.

I performed the following steps:

- Loaded the dataset using Pandas.
- Checked the number of rows and columns.
- Checked for missing values and duplicate records.
- Removed the Surname column because it was not needed for this analysis.
- Created a new column called `ChurnStatus` using the `Exited` column.
- Divided customers into different age groups.
- Grouped customers based on their credit scores.
- Divided customers into new, mid-term and long-term groups based on tenure.
- Grouped customers based on their account balance.
- Divided customers into low, medium and high salary groups.

These steps helped me prepare the data for further analysis.

## 5. Tools and Technologies Used

I used the following tools and libraries for this project:

- **Python:** Used to write the code and perform the analysis.
- **Pandas:** Used to load, clean and analyse customer data.
- **NumPy:** Used for numerical operations.
- **Matplotlib:** Used to create charts and graphs.
- **Seaborn:** Used to create visualizations and understand relationships between columns.
- **Streamlit:** Used to create an interactive dashboard.

## 6. Exploratory Data Analysis

After preparing the dataset, I started exploring the customer data to understand churn patterns.

I compared customers who left the bank with customers who continued using its services. I also studied different customer groups to find where churn was higher.

The analysis covered age, gender, geography, account activity, credit score, tenure, balance, salary, number of products and credit card ownership.


### 6.1 Overall Customer Churn

The dataset contains 10,000 customers. Out of these, 2,037 customers have left the bank, while 7,963 customers are still with the bank.

The overall churn percentage is 20.37%, and the retention percentage is 79.63%.

This means that around 20 out of every 100 customers have left the bank. It shows that customer churn is an important area that needs attention.

**Results:**

- Total customers: 10,000
- Customers who left: 2,037
- Customers who stayed: 7,963
- Churn percentage: 20.37%
- Retention percentage: 79.63%

### 6.2 Churn Based on Age

I analysed customer churn across different age groups.

From the analysis, age is one of the important factors related to customer churn. Older customer groups showed higher churn compared with younger customers.

This suggests that banks should understand the needs of different age groups and provide services that match their expectations.

### 6.3 Churn Based on Gender

I also compared churn between male and female customers.

The analysis showed that female customers had a higher churn percentage than male customers in this dataset.

Banks can study customer feedback and service preferences to understand the reasons behind this difference.

### 6.4 Churn Across Different Countries

I compared customer churn in France, Spain and Germany.

The results showed:

- France: 16.15%
- Spain: 16.67%
- Germany: Highest churn among the three countries.

Germany had the highest customer churn, while France and Spain had comparatively lower churn percentages.

This shows that customer retention may need different approaches depending on the country.


### 6.5 Churn Based on Account Activity

I compared customers who actively use their accounts with those who are less active.

The results showed:

- Active customers: 14.27% churn
- Inactive customers: 26.85% churn

Inactive customers had a much higher churn percentage than active customers.

This suggests that regular customer engagement may help banks retain their customers.

### 6.6 Churn Based on Credit Score

I divided customers into three groups based on their credit scores.

The results were:

- Low credit score: 22.02%
- Medium credit score: 20.56%
- High credit score: 19.32%

Customers with lower credit scores had a slightly higher churn percentage than customers with higher credit scores.

### 6.7 Churn Based on Tenure

I studied how long customers had been associated with the bank.

The results were:

- New customers: 21.14%
- Mid-term customers: 19.64%
- Long-term customers: 20.45%

The churn percentages were fairly close across the three groups. New customers had the highest churn among them.

### 6.8 Churn Based on Account Balance

I divided customers into zero-balance, low-balance and high-balance groups.

The results were:

- Zero-balance customers: 13.82%
- Low-balance customers: 24.00%
- High-balance customers: 24.16%

Customers with low and high account balances had higher churn percentages than customers with zero balances.

### 6.9 Churn Based on Number of Products

I also checked whether the number of bank products used by customers had any relationship with churn.

The results were:

- 1 product: 27.71%
- 2 products: 7.58%
- 3 products: 82.71%
- 4 products: 100%

Customers using three or four products showed very high churn percentages. However, the number of customers in these groups was much smaller than in the one- and two-product groups. So, these results should be considered carefully.

### 6.10 Churn Based on Credit Card Ownership

I compared customers who had a credit card with customers who did not have one.

The results were:

- Customers with a credit card: 20.18%
- Customers without a credit card: 20.81%

The difference was very small. Credit card ownership did not show a major difference in churn in this analysis.

### 6.11 Churn Based on Estimated Salary

I divided customers into low, medium and high salary groups.

The results were:

- Low salary: 20.13%
- Medium salary: 19.77%
- High salary: 21.21%

The churn percentages were similar across all three groups. High-salary customers had a slightly higher churn percentage.

### 6.12 Correlation Analysis

I used a correlation heatmap to understand the relationship between different numerical columns and customer churn.

The analysis showed that:

- Age had a positive correlation of 0.285 with churn.
- Balance had a positive correlation of 0.119 with churn.
- Account activity had a negative correlation of -0.156 with churn.
- Estimated salary had a very small correlation of 0.012 with churn.

Age showed a stronger positive relationship with churn than the other numerical columns in this analysis.

Correlation shows how two variables are related. It does not prove that one variable causes the other.


## 7. High-Balance Customer Analysis

I wanted to understand whether customers with higher account balances were also leaving the bank.

For this analysis, I divided customers with a positive account balance into low-balance and high-balance groups using the median positive balance.

The results showed:

- Total high-balance customers: 3,191
- High-balance customers who left: 771
- High-balance customer churn percentage: 24.16%

The churn percentage among high-balance customers was higher than the overall churn percentage of 20.37%.

This is worth looking into because banks may want to pay more attention to customers who maintain higher account balances.

Here, I have used account balance as a simple way to identify high-balance customers. It does not represent their complete financial value to the bank.

## 8. Key Findings

After completing the analysis, I found the following points:

1. The overall customer churn percentage was 20.37%.
2. Germany had the highest churn percentage among the three countries.
3. Inactive customers had a higher churn percentage than active customers.
4. Older customers showed a stronger relationship with churn.
5. Customers with low and high balances had higher churn than zero-balance customers.
6. Customers with three and four products showed very high churn percentages, but these groups had fewer records.
7. High-balance customers had a churn percentage of 24.16%.
8. Estimated salary and credit card ownership showed only small differences in churn.

## 9. Suggestions to Improve Customer Retention

Based on the findings, I suggest the following steps that banks could consider:

- Contact inactive customers and understand why they are not using their accounts regularly.
- Pay more attention to customer groups with higher churn percentages.
- Study customer feedback in Germany to understand the reasons for higher churn.
- Provide better support and suitable banking services for older customers.
- Follow up with high-balance customers and understand their service requirements.
- Study customers who use three or four products separately because their churn percentages are high.
- Regularly monitor customer activity and churn patterns.

These are suggestions based on the analysis. Further customer feedback and research would be needed to understand the actual reasons why customers leave.

## 10. Conclusion

In this project, I analysed customer data from a European bank to understand customer churn patterns.

I used Python and its libraries to clean the data, divide customers into different groups, calculate churn percentages and create visualizations.

The analysis showed that account activity, age, geography and account balance were useful factors to study when looking at customer churn.

I also created a Streamlit dashboard where users can view customer details, select filters and compare churn across different groups.

This project helped me improve my skills in data cleaning, exploratory data analysis, data visualization and building a simple dashboard.

Overall, the project gave me practical experience in using data to understand a business problem.

