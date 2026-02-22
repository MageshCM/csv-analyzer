import csv
INPUT_PATH = "data/student.csv"
OUTPUT_PATH = "output/report.csv"

NUMERIC_FIELDS = {"age", "absences", "G1", "G2", "G3"}
MISSING_VALUES = {"", "NA"}

def load_csv(path):
    with open(path,"r",newline="",encoding="utf-8") as file:
        reader=csv.DictReader(file, delimiter=";")
        return list(reader)
def clean_row(row):
    cleaned = {}
    for key, val in row.items():
        if val in MISSING_VALUES:
            cleaned[key] = None
        elif key in NUMERIC_FIELDS:
            try:
                cleaned[key] = int(val)
            except:
                cleaned[key] = None
        else:
            cleaned[key] = val
    return cleaned
def clean_data(data):
    return [clean_row(row) for row in data]

def collect_numeric_columns(data):
    columns = {field: [] for field in NUMERIC_FIELDS}
    for row in data:
        for field in NUMERIC_FIELDS:
            value = row.get(field)
            if value is not None:
                columns[field].append(value)
    return columns

def summarize(values):
    return {
        "count": len(values),
        "mean": sum(values) / len(values) if values else None,
        "min": min(values) if values else None,
        "max": max(values) if values else None
    }

def generate_report(numeric_data):
    report = {}
    for field, values in numeric_data.items():
        report[field] = summarize(values)
    return report

def export_report(report, path):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["column", "count", "mean", "min", "max"])
        for column, stats in report.items():
            writer.writerow([
                column,
                stats["count"],
                stats["mean"],
                stats["min"],
                stats["max"]
            ])

def main():
    raw_data = load_csv(INPUT_PATH)
    cleaned_data = clean_data(raw_data)
    numeric_data = collect_numeric_columns(cleaned_data)
    report = generate_report(numeric_data)
    export_report(report, OUTPUT_PATH)

if __name__ == "__main__":
    main()