import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(BASE_DIR, "data", "raw")
CLEAN_PATH = os.path.join(BASE_DIR, "data", "clean")

os.makedirs(CLEAN_PATH, exist_ok=True)

def transform_data():
    print("Starting data transformation...")

    customers = pd.read_csv(os.path.join(RAW_PATH, "customers.csv"))
    orders = pd.read_csv(os.path.join(RAW_PATH, "orders.csv"))
    products = pd.read_csv(os.path.join(RAW_PATH, "products.csv"))

    # Basic transformations
    customers.drop_duplicates(inplace=True)
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    products["price"] = products["price"].astype(float)

    customers.to_csv(os.path.join(CLEAN_PATH, "customers_clean.csv"), index=False)
    orders.to_csv(os.path.join(CLEAN_PATH, "orders_clean.csv"), index=False)
    products.to_csv(os.path.join(CLEAN_PATH, "products_clean.csv"), index=False)

    print("Transformation completed successfully.")

if __name__ == "__main__":
    transform_data()
