import pandas as pd

df = pd.read_csv("salesdata.csv")

print("rows and columns in the dataset: ", df.shape)
print("the first ten rows are: ", df.head())
print("the last ten rows are:", df.tail())
print("the columns are: ", df.columns)
print("**************")
print("THE MISSING VALUES PER COLUMNS ARE: ")
print(df.isnull().sum())

total_sales = pd.to_numeric(df['sales'], errors='coerce').sum()
total_profit = df['profit'].sum()

print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total profit: ₹{total_profit}")
#converting the str type to numeric in sales 
df['sales'] = pd.to_numeric(df['sales'].replace('[\$,]', '', regex=True), errors='coerce')
#calcuating the sales by category
sales_by_category = df.groupby('category')['sales'].sum().round(2).sort_values(ascending=False)
print(sales_by_category)

df['order_date'] = pd.to_datetime(df['order_date'], errors= 'coerce')
df['year_month'] = df['order_date'].dt.to_period('M')
monthly_sales = df.groupby('year_month')['sales'].sum().round(2)
print(monthly_sales)
monthly_sales.to_csv("monthly_sales.csv")

sales_by_category.to_csv("sales_by_category.csv")

