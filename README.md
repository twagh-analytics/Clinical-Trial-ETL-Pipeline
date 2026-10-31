Hospital Lab Results: SQL ETL & Analysis

This portfolio project demonstrates a healthcare data analytics workflow using Python, SQLite, and Power BI. The objective of this project was to ingest raw hospital lab records, join them with patient demographics using a relational database engine, filter for abnormal health results, and visualize the findings to answer specific business questions.

Tech Stack

Python (Pandas & SQLite3): Data extraction, database connection, and pipeline automation.

SQL: Relational data merging (INNER JOIN) and data filtering (WHERE).

Power BI: Business intelligence visualization.

Project Workflow

1. Data Ingestion (Extract & Load)
I started with two raw flat files: patients_data.csv (containing patient IDs, names, ages, and genders) and lab_tests.csv (containing test types, results, and status flags). Using Pandas, I extracted these files and loaded them directly into a new SQLite database (hospital_labs.db) as two separate, independent tables.

2. Relational Querying (Transform)
Instead of merging the data in Python, I utilized the SQLite engine to process the data. I wrote a multi-line SQL query to:

Execute an INNER JOIN on the PatientID primary key to connect the patient demographics with their respective lab results.

Apply a WHERE clause (Status != 'Normal') to strictly filter the dataset, isolating only the patients who registered 'High' or 'Low' critical test results.

3. Export & Visualization
The results of the SQL query were read back into Python and exported as a clean abnormal_results.csv file. I then imported this dataset into Power BI to build a dashboard answering three core business questions:

Which lab test produces the highest average result value?
(Visualized using a Bar Chart: X-Axis = TestType, Y-Axis = Average of ResultValue)

Which gender experiences a higher volume of abnormal test results?
(Visualized using a Column Chart: X-Axis = Gender, Y-Axis = Count of PatientID)

Is there a correlation between patient age and test result values?
(Visualized using a Scatter Plot: X-Axis = Age, Y-Axis = ResultValue)
