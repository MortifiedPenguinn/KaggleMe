import pandas as pd
from pandasql import sqldf

# Define a function to perform SQL queries on the DataFrame
def query_dataframe(sql_query, dataframe):
    return sqldf(sql_query, locals())

# Define a function to perform column renaming
def rename_columns(dataframe):
    dataframe.rename(columns={'Quantity Ordered':'Quantity'}, inplace=True)
    dataframe.rename(columns={'Purchase Address':'FullAddress'}, inplace=True)
    dataframe.rename(columns={'Price Each':'PriceEach'}, inplace=True)
    dataframe.rename(columns={'Cost price':'CostPrce'}, inplace=True)
    dataframe.rename(columns={'Order Year':'OrderYear'}, inplace=True)
    dataframe.rename(columns={'Order Month':'OrderMonth'}, inplace=True)
    dataframe.rename(columns={'Purchase City':'PurchaseCity'}, inplace=True)

# Define a function to calculate and return total quantity of each product sold
def calculate_total_quantity_sold(dataframe):
    q1 = """
    SELECT Product, SUM(Quantity) AS total_sold
    FROM df
    GROUP BY Product
    ORDER BY total_sold DESC
    """
    result = query_dataframe(q1, dataframe)
    return result

# Define a function to calculate and return total revenue
def calculate_total_revenue(dataframe):
    q2 = """
    SELECT SUM(Quantity * PriceEach) AS total_revenue
    FROM df
    """
    result = query_dataframe(q2, dataframe)
    return result

# Define a function to calculate and return total profit
def calculate_total_profit(dataframe):
    q3 = """
    SELECT SUM(Quantity * (PriceEach - CostPrce)) AS total_profit
    FROM df
    """
    result = query_dataframe(q3, dataframe)
    return result

# Define a function to save the result to a CSV file
def save_to_csv(result, filename):
    result.to_csv(filename, index=False)

# Example usage:
if __name__ == "__main__":
    df = pd.read_csv("your_dataframe.csv")
    rename_columns(df)
    
    total_quantity_sold = calculate_total_quantity_sold(df)
    save_to_csv(total_quantity_sold, "total_quantity_of_product_sold.csv")
    
    total_revenue = calculate_total_revenue(df)
    print(total_revenue)
    
    total_profit = calculate_total_profit(df)
    print(total_profit)
