import pandas as pd

def generate_report(input_path: str, report_dir: str):
    df = pd.read_csv(input_path)
    summary = df.groupby('category')['price'].mean()
    report_file = os.path.join(report_dir, 'report.txt')
    with open(report_file, 'w') as f:
        f.write(summary.to_string())
