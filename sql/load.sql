-- Load cleaned CSV files into tables

.mode csv
.headers on

.import '../data/clean/customers_clean.csv' customers
.import '../data/clean/products_clean.csv' products
.import '../data/clean/orders_clean.csv' orders
