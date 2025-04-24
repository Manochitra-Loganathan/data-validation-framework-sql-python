# ✅ Data Validation Framework with SQL, Python, Splunk & Dynatrace

This project demonstrates a real-world **data validation and monitoring framework** across staging and reporting layers using **SQL Server**, **Python**, **Splunk**, and **Dynatrace**.

It includes:
- SQL & Python QA scripts
- Row count reconciliation logic
- Mock monitoring logs
- Threshold-based alert trigger configs

---

## 🛠️ Tech Stack

| Area           | Tools & Technologies                       |
|----------------|---------------------------------------------|
| Validation     | SQL Server, Python (pyodbc, pandas)        |
| Monitoring     | Splunk (mock ETL logs)                     |
| Alerting       | Dynatrace (JSON-based alert configs)       |
| Data Coverage  | Staging to Reporting QA                    |

---

## 📂 Folder Structure

```bash
data-validation-framework-sql-python/
│
├── tests/
│   ├── validation_checks.sql         # SQL null and row count validation
│   └── compare_row_counts.py         # Python reconciliation script
│
├── logs/
│   └── mock_splunk_etl_log.txt       # Sample log entries for Splunk monitoring
│
├── dynatrace/
│   └── row_count_alert.json          # Trigger rule based on row count delta
│
└── README.md
````
----
🔍 Use Case
This framework is designed to run QA checks post-ETL — ensuring data integrity between staging and reporting layers before dashboards or analytics consume the outputs.

Example Checks:
❓ Null validation on key fields (customer_id, product_id)

🔄 Row count reconciliation from staging to reporting

🔁 Realtime alerting when mismatch exceeds defined threshold

📜 Log tracking in Splunk (error, success, counts)

----
🧪 QA Logic Explained
🔸 SQL Validation Script
tests/validation_checks.sql:

Null check: Ensures no blanks in key dimensions

Row count reconciliation: UNION ALL from staging and reporting for direct comparison

----
🔸 Python Reconciliation Script
tests/compare_row_counts.py:

Connects to SQL Server using pyodbc

Compares row count between two layers

Prints match or mismatch with message

---
🔸 Splunk Monitoring Log
logs/mock_splunk_etl_log.txt:

Example entries to simulate:

ETL job execution

Validation step status

Failure messages with Job ID and details
---

🔸 Dynatrace Alert Trigger
dynatrace/row_count_alert.json:

JSON-configurable threshold

Triggers alert if row count deviation > 5

Mock fields: staging_count, reporting_count, status, trigger

---
📈 Benefits

Benefit	Description
🚦 Automated QA	SQL + Python script-based automation
🔁 Repeatable & Portable	Easy to plug into other pipelines
📉 Error Visibility	Alerts reduce the time to detect & respond
📊 Integrated Monitoring	Supports Splunk + Dynatrace-style tracking


---
📫 Let’s Connect
This project reflects my work in building reliable data delivery pipelines with automated QA, logging, and monitoring layers.

📍 Auckland, NZ — open to remote/hybrid roles in Data QA, Platform Engineering, or Analytics DevOps
🔗 Connect on LinkedIn
