import pandas as pd

def process_data(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    df['price'] = df['price'].str.replace('£','').astype(float)
    df.to_csv(output_path, index=False)
