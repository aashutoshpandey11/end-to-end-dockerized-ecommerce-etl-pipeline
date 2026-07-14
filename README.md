# 🚀 End-to-End Dockerized E-Commerce ETL Pipeline

An end-to-end **Data Engineering** project that automates the process of extracting, transforming, and loading (ETL) e-commerce product data into a PostgreSQL database using **Python, Docker, PostgreSQL, SQLAlchemy, Pandas, and Streamlit**.

The project demonstrates a real-world ETL workflow by collecting product data from a REST API, cleaning and validating the dataset, loading it into a PostgreSQL database, and visualizing business insights through an interactive Streamlit dashboard.

---

## 📌 Project Highlights

- ✅ Automated ETL Pipeline
- ✅ REST API Data Extraction
- ✅ Data Cleaning & Transformation
- ✅ Data Quality Validation
- ✅ PostgreSQL Database Integration
- ✅ SQLAlchemy Database Connectivity
- ✅ Docker & Docker Compose
- ✅ Interactive Streamlit Dashboard
- ✅ Plotly Visualizations
- ✅ Pipeline Logging
- ✅ SQL Analysis Queries

---

## 📖 Project Overview

This project simulates a real-world Data Engineering workflow.

The ETL pipeline performs the following tasks:

1. Extracts product data from the Fake Store API.
2. Cleans and transforms the raw dataset.
3. Performs data quality validation.
4. Loads the processed data into PostgreSQL.
5. Stores execution logs.
6. Visualizes the processed data using Streamlit.

---

## 🏗️ Architecture

```text
                  Fake Store API
                        │
                        ▼
           Extract (Python + Requests)
                        │
                        ▼
      Raw CSV (data/raw/products.csv)
                        │
                        ▼
     Transform & Validate (Pandas)
                        │
                        ▼
 Clean CSV (data/cleaned/cleaned_products.csv)
                        │
                        ▼
 PostgreSQL Database (Docker + SQLAlchemy)
                        │
                        ▼
        SQL Analysis & Streamlit Dashboard
```

---

## ⚙️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | ETL Development |
| Requests | API Data Extraction |
| Pandas | Data Cleaning & Transformation |
| PostgreSQL | Relational Database |
| SQLAlchemy | Database Connectivity |
| Docker | Containerization |
| Docker Compose | Multi-container Environment |
| Streamlit | Interactive Dashboard |
| Plotly | Interactive Charts |
| SQL | Data Analysis |
| Logging | Pipeline Monitoring |

---

## 📂 Project Structure

```text
end-to-end-dockerized-ecommerce-etl-pipeline/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── products.csv
│   └── cleaned/
│       └── cleaned_products.csv
│
├── logs/
│   └── pipeline.log
│
├── postgres/
│   └── init/
│       └── create_tables.sql
│
├── scripts/
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── utils/
│       └── logger.py
│
├── sql/
│   └── analysis_queries.sql
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🌐 Data Source

This project uses the **Fake Store API** as its data source.

API Endpoint:

https://fakestoreapi.com/products

The dataset contains:

- Product Title
- Description
- Price
- Category
- Product Image
- Rating
- Rating Count

---

## 🔄 ETL Workflow

### 1️⃣ Extract

- Connects to the Fake Store API
- Downloads product data
- Saves raw data as CSV

Output:

```text
data/raw/products.csv
```

---

### 2️⃣ Transform

The transformation stage performs:

- Remove duplicate records
- Handle missing values
- Standardize column names
- Convert data types
- Calculate discounted price
- Validate dataset quality

Output:

```text
data/cleaned/cleaned_products.csv
```

---

### 3️⃣ Load

Loads the cleaned dataset into PostgreSQL using SQLAlchemy.

Database Table:

```text
products
```

---

### 4️⃣ Logging

Every pipeline execution is automatically logged.

Example:

```text
Pipeline Started

Downloaded 20 Products

Transformation Completed

Loading 20 Records

Pipeline Completed Successfully

Execution Time: 1.52 Seconds
```

Logs are stored in:

```text
logs/pipeline.log
```

---

## 🗄️ Database

Database:

```text
PostgreSQL
```

Table:

```text
products
```

The database schema is automatically created when Docker starts.

SQL scripts are available in:

```text
postgres/init/
```

and

```text
sql/
```

---

## 📊 Streamlit Dashboard

The project includes an interactive analytics dashboard built using Streamlit.

### Dashboard Features

- 📈 KPI Cards
- 📦 Products by Category
- 💰 Average Price by Category
- 🥧 Category Distribution
- ⭐ Rating Distribution
- 📈 Price vs Rating Scatter Plot
- 🏆 Top 10 Most Expensive Products
- 📋 Category Summary Table
- 📊 Database Statistics
- 📑 Data Quality Report
- 🔍 Product Search
- 🎯 Category Filter
- 💵 Price Range Filter
- ⭐ Rating Filter
- 📥 Download Filtered Data as CSV

---

## 🐳 Docker

The project is fully containerized using Docker.

### Services

- PostgreSQL Database
- ETL Pipeline

### Start the Project

```bash
docker compose up --build
```

### Stop the Project

```bash
docker compose down
```

---

## ▶️ Running the Dashboard

Start Streamlit:

```bash
streamlit run dashboard/app.py
```

Open your browser:

```text
http://localhost:8501
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/<your-github-username>/end-to-end-dockerized-ecommerce-etl-pipeline.git
```

### Navigate into the Project

```bash
cd end-to-end-dockerized-ecommerce-etl-pipeline
```

### Build and Start Docker Containers

```bash
docker compose up --build
```

### Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📈 SQL Analysis

The project includes SQL queries for:

- Total Products
- Average Product Price
- Products by Category
- Highest Rated Products
- Most Expensive Products
- Category-wise Average Rating

SQL scripts are available in:

```text
sql/analysis_queries.sql
```

---

## 📸 Screenshots

### 📊 Streamlit Dashboard

> *(Add dashboard screenshot here)*

---

### 🐳 Docker Containers

> *(Add Docker Desktop screenshot here)*

---

### 🗄️ PostgreSQL Database

> *(Add pgAdmin screenshot here)*

---

### 📜 Pipeline Logs

> *(Add terminal output screenshot here)*

---

## 🎯 Skills Demonstrated

- ETL Pipeline Development
- Python Programming
- REST API Integration
- Data Cleaning & Transformation
- Data Quality Validation
- PostgreSQL
- SQL
- SQLAlchemy
- Docker
- Docker Compose
- Streamlit
- Plotly
- Logging
- Relational Database Design
- Data Visualization

---

## 🚀 Future Improvements

- Apache Airflow Workflow Orchestration
- Incremental Data Loading
- CI/CD using GitHub Actions
- Cloud Deployment (AWS, Azure, or GCP)
- Data Warehouse Integration
- Automated Scheduling
- Environment Variables (.env)
- Unit & Integration Testing

---

## 👨‍💻 Author

**Aashutosh Pandey**

Bachelor of Science (Hons) Computing

The British College (Leeds Beckett University)

---

## 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for more details.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!