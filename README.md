# CSV Analyzer – Student Performance Dataset

A Python mini project that analyzes a real-world student performance dataset and generates summary statistics for selected numeric columns.

---

## 📌 Project Overview

This project reads a public CSV dataset, cleans missing values, processes numeric data, and computes basic statistical measures such as **count, mean, minimum, and maximum**.

The final output is exported as a CSV report.

This project demonstrates:
- CSV file handling in Python
- Data cleaning and preprocessing
- Basic statistical analysis
- Proper project structure and virtual environment usage

---

## 📂 Dataset

- **Source:** UCI Machine Learning Repository  
- **Dataset Name:** Student Performance Dataset  
- **File Used:** `student-mat.csv` (Math subject students)

The dataset contains student attributes such as age, absences, and grades (`G1`, `G2`, `G3`).  
The file uses a **semicolon (`;`)** as the delimiter.

---

## ⚙️ Features

- Reads semicolon-delimited CSV files
- Treats empty values and `"NA"` as missing data
- Converts selected columns to numeric values
- Ignores non-numeric columns during analysis
- Computes the following statistics:
  - Count
  - Mean
  - Minimum
  - Maximum
- Exports results to a CSV report

---

## 🗂️ Project Structure
csv_analyzer/
├── data/
│ └── student.csv
├── output/
│ └── report.csv
├── analyzer.py
├── .gitignore
├── requirements.txt
└── venv/


- `data/` → Input dataset  
- `output/` → Generated analysis report  
- `analyzer.py` → Main Python script  
- `venv/` → Virtual environment (ignored in Git)

---

## ▶️ How to Run

### 1. Create and activate virtual environment
```
python -m venv venv
.\venv\Scripts\activate
```
2. Add dataset
Place student-mat.csv inside the data folder and rename it to:
student.csv

3. Run the analyzer
python analyzer.py

4. View output
The generated report will be available at:
output/report.csv

📊 Sample Output
column,count,mean,min,max
age,395,16.69,15,22
absences,395,5.70,0,75
G1,395,10.90,3,19
G2,395,10.71,0,19
G3,395,10.41,0,20


🧪 Dependencies

This project uses only Python standard library modules.
Therefore, requirements.txt is intentionally empty.




