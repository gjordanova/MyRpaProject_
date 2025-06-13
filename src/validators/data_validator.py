import pandas as pd

def validate_data(input_path: str):
    df = pd.read_csv(input_path)
    if df.empty:
        raise ValueError("No data found")
    if df['price'].isnull().any():
        raise ValueError("Null prices found")
