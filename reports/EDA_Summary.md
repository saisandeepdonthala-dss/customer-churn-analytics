# Customer Segmentation & Churn Pattern Analytics in European Banking

## 1. About the Project

In this project, I worked on a customer dataset from a European bank to understand customer behaviour and find out how many customers are leaving the bank.

I used Python to clean the data, divide customers into different groups and analyse their churn patterns. I also created graphs to make the results easier to understand.

## 2. Dataset Details

For this project, I used the `European_Bank.csv` dataset.

- Total customers: 10,000
- Total columns in the original dataset: 14
- Records used for analysis: 10,000

I removed the Surname column because it was not useful for my analysis. I also created a few new columns, such as Age Group, Credit Score Band, Tenure Group, Balance Segment and Churn Status, to make the analysis easier.

## 3. Overall Customer Churn

After checking the dataset, I found the following results:

- Total customers: 10,000
- Customers who left the bank: 2,037
- Customers who stayed with the bank: 7,963
- Churn percentage: 20.37%
- Retention percentage: 79.63%

From this analysis, I found that 2,037 customers had left the bank, which is 20.37% of the total customers. This gives us an idea of how customer churn is affecting the bank.

## 4. Customer Churn Analysis

I checked customer churn based on different factors to understand which groups were more likely to leave the bank.

### Age Group

Customers in the older age groups showed higher churn compared to younger customers. Age appears to be an important factor when looking at customer churn.

### Gender

I compared churn between male and female customers. The results showed that female customers had a higher churn percentage than male customers.

### Geography

I checked customer churn across France, Germany and Spain. Germany had the highest churn percentage, while France had the lowest at 16.15%.

### Customer Activity

Inactive customers had a higher churn percentage (26.85%) compared to active customers (14.27%). This suggests that regular customer activity may be related to better customer retention.

### Credit Score

Customers with low credit scores had a churn percentage of 22.02%, while medium and high credit score groups had 20.56% and 19.32%, respectively.

### Tenure

I compared customers based on how long they had been with the bank. New customers had a churn percentage of 21.14%, mid-term customers had 19.64%, and long-term customers had 20.45%.

### Account Balance

Customers with low and high balances had higher churn percentages (24.00% and 24.16%) compared to zero-balance customers (13.82%).

### Number of Products

Customers with one product had a churn percentage of 27.71%. Customers with two products had a much lower churn percentage of 7.58%.

For customers with three products, churn was 82.71%, and all 60 customers with four products had left the bank. However, the number of customers in these two groups was small, so these results should be considered carefully.

### Credit Card Ownership

The churn percentage was 20.18% for customers with a credit card and 20.81% for customers without one. The difference was very small.

### Estimated Salary

I divided customers into three salary groups. The churn percentages were 20.13% for low salary, 19.77% for medium salary and 21.21% for high salary. There was no major difference between the groups.

## 5. Correlation Analysis

I also checked the correlation between different customer details and churn.

The main findings were:

- Age had the strongest positive correlation with churn (0.285).
- IsActiveMember had a negative correlation with churn (-0.156).
- Balance showed a weak positive correlation (0.119).
- Estimated Salary had almost no correlation with churn (0.012).
- Credit Score, Tenure, Credit Card ownership and Number of Products also showed weak correlations.

From this analysis, age and customer activity showed relatively stronger relationships with churn compared to the other numerical factors. Correlation does not necessarily mean that one factor causes customers to leave.

## 6. Conclusion

After completing this analysis, I found that around 20.37% of the bank's customers had left.

Age, customer activity, geography and the number of products showed noticeable differences in churn across customer groups.

One thing I noticed was that inactive customers had a higher churn percentage than active customers. Customers with two products also had a much lower churn percentage than customers with one product.

This project helped me understand how to work with customer data, perform exploratory data analysis using Python and present findings through graphs.

## 7. Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code