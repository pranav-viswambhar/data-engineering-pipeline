import sqlite3
import pandas as pd
import os

# Go to project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

CLEAN_PATH = os.path.join(BASE_DIR, "data", "clean")
DB_PATH = os.path.join(BASE_DIR, "warehouse.db")

conn = sqlite3.connect(DB_PATH)

pd.read_csv(os.path.join(CLEAN_PATH, "customers_clean.csv")) \
    .to_sql("customers", conn, if_exists="append", index=False)

pd.read_csv(os.path.join(CLEAN_PATH, "products_clean.csv")) \
    .to_sql("products", conn, if_exists="append", index=False)

pd.read_csv(os.path.join(CLEAN_PATH, "orders_clean.csv")) \
    .to_sql("orders", conn, if_exists="append", index=False)

conn.close()

print("✅ Data loaded into SQLite successfully")
