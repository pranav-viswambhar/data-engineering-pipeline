import pandas as pd
import os

# Define raw data path
RAW_DATA_PATH = "../data/raw/"

def extract_data():
    print("Starting data extraction...")

    customers_file = os.path.join(RAW_DATA_PATH, "customers.csv")
    products_file = os.path.join(RAW_DATA_PATH, "products.csv")
    orders_file = os.path.join(RAW_DATA_PATH, "orders.csv")

    # Read CSV files
    customers_df = pd.read_csv(customers_file)
    products_df = pd.read_csv(products_file)
    orders_df = pd.read_csv(orders_file)

    print("Customers data loaded:", customers_df.shape)
    print("Products data loaded:", products_df.shape)
    print("Orders data loaded:", orders_df.shape)

    return customers_df, products_df, orders_df


if __name__ == "__main__":
    extract_data()
