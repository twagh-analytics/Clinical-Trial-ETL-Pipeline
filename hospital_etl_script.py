import pandas as pd
import sqlite3
df_patients = pd.read_csv("patients_data.csv")
df_labs = pd.read_csv("lab_tests.csv")

conn = sqlite3.connect("hospital_labs.db")

df_patients.to_sql("patients", conn, index=False, if_exists="replace")
df_labs.to_sql("labs", conn, index=False, if_exists="replace")

sql_query = """
 SELECT
 patients.PatientID,
 patients.Name,
 patients.Age,
 patients.Gender,
 labs.TestType,
 labs.ResultValue,
 labs.Status
 FROM patients
 INNER JOIN labs
  ON patients.PatientID = labs.PatientID
WHERE labs.status != 'Normal';
 """
df_abnormal_results = pd.read_sql(sql_query, conn)
df_abnormal_results.to_csv("abnormal_results.csv", index=False)

print(" 'abnormal_results.csv' generated successfully.")









