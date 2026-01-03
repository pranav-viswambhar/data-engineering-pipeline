# 🚀 End-to-End Data Engineering Pipeline

## 📌 Overview
This project demonstrates a **complete end-to-end data engineering pipeline** that ingests raw data, performs cleaning and transformation, loads it into a relational data warehouse (SQLite), and runs analytical SQL queries to generate business insights.

The project follows **industry-style data engineering practices**, including clear folder structure, modular scripts, and separation of ingestion, transformation, storage, and analytics layers.

---

## 🏗️ Architecture

Raw Data  
⬇  
**Ingestion (Python)**  
⬇  
**Transformation (Pandas)**  
⬇  
**Data Warehouse (SQLite)**  
⬇  
**Analytics (SQL Queries)**

---

## 📂 Project Structure

data-engineering-pipeline/
│
├── data/
│ ├── raw/ # Raw CSV data
│ └── clean/ # Cleaned CSV data after transformation
│
├── ingestion/
│ └── extract.py # Reads raw data
│
├── transformation/
│ └── transform.py # Cleans and prepares data
│
├── sql/
│ ├── schema.sql # Database schema (tables)
│ ├── load.sql # SQL-based data loading (optional)
│ ├── analytics.sql # Business analytics queries
│ └── warehouse/
│ └── load_to_sqlite.py # Python-based data loading into SQLite
│
├── warehouse.db # SQLite data warehouse
├── README.md # Project documentation
└── .gitignore

yaml
Copy code

---

## 🧰 Tech Stack

- **Python** – Data ingestion & transformation
- **Pandas** – Data cleaning and processing
- **SQLite** – Lightweight data warehouse
- **SQL** – Analytics and reporting
- **VS Code + SQLite Extension** – Development & query execution
- **Git & GitHub** – Version control

---

## 🔄 Data Pipeline Workflow

### 1️⃣ Data Ingestion
- Raw CSV files are read from the `data/raw/` directory.
- Implemented using Python scripts.

### 2️⃣ Data Transformation
- Cleaning steps include:
  - Handling missing values
  - Standardizing column names
  - Ensuring correct data types
- Cleaned data is saved to `data/clean/`.

### 3️⃣ Data Loading
- Cleaned CSV files are loaded into **SQLite** tables:
  - `customers`
  - `products`
  - `orders`
- Implemented using **Pandas + SQLite (`to_sql`)**.

### 4️⃣ Data Analytics
- SQL queries are executed to generate insights such as:
  - Total revenue by product
  - Top customers by number of orders

---

## 📊 Sample Analytics Queries

### 🔹 Total Revenue by Product
```sql
SELECT
    p.product_name,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;
🔹 Top Customers by Number of Orders
sql
Copy code
SELECT
    c.email AS customer,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.email
ORDER BY total_orders DESC;
▶️ How to Run the Project
Step 1: Run Transformation
bash
Copy code
python transformation/transform.py
Step 2: Load Data into SQLite
bash
Copy code
python sql/warehouse/load_to_sqlite.py
Step 3: Run Analytics
Open analytics.sql

Right-click → Run Query

View results in SQLite Explorer

🎯 Key Learnings
Building modular data pipelines

Handling real-world CSV data

Loading data into relational databases

Writing analytical SQL queries

Organizing projects like a data engineer

📌 Use Case
This project simulates a mini data warehouse for an e-commerce system and is suitable for:

Data Engineer portfolios

SQL & Python interview preparation

Demonstrating ETL/ELT concepts

👤 Author
Pranav Viswambhar
B.Tech – Computer Science Engineering
