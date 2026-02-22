CSV Analyzer – Student Performance Dataset

A Python mini project that analyzes a public student performance dataset and generates summary statistics for selected numeric columns.

📌 Project Overview

This project reads a real-world CSV dataset, cleans missing values, processes numeric columns, and computes basic statistical measures such as count, mean, minimum, and maximum.
The final output is exported as a CSV report.

The goal of this project is to demonstrate:

CSV file handling in Python

Data cleaning and preprocessing

Basic statistical analysis

Proper project structure and environment management

📂 Dataset

Source: UCI Machine Learning Repository

Dataset: Student Performance Dataset

File used: student-mat.csv (Math subject students)

The dataset contains student-related attributes such as age, absences, and grades (G1, G2, G3).
The file uses a semicolon (;) as the delimiter.

⚙️ Features

Reads semicolon-delimited CSV files

Treats empty values and "NA" as missing data

Converts selected columns to numeric values

Ignores non-numeric columns during analysis

Computes:

Count

Mean

Minimum

Maximum

Exports results to a CSV report

🗂️ Project Structure
csv_analyzer/
├── data/
│   └── student.csv
├── output/
│   └── report.csv
├── analyzer.py
├── .gitignore
├── requirements.txt
└── venv/

data/ → input dataset

output/ → generated analysis report

analyzer.py → main Python script

venv/ → virtual environment (ignored in Git)

▶️ How to Run
1. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate
2. Place dataset

Copy student-mat.csv into the data folder and rename it to:

student.csv
3. Run the analyzer
python analyzer.py
4. View output

The generated report will be available at:

output/report.csv
📊 Sample Output (Report)
column,count,mean,min,max
age,395,16.69,15,22
absences,395,5.70,0,75
G1,395,10.90,3,19
G2,395,10.71,0,19
G3,395,10.41,0,20
🧪 Dependencies

This project uses only Python standard library modules.
Therefore, requirements.txt is intentionally empty.

📎 Notes

The virtual environment (venv/) and output files are excluded from version control using .gitignore.

The project is intended for academic and learning purposes.