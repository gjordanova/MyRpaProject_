import pandas as pd
from src.utils.helpers import get_output_paths

def process_data(df, **kwargs):

    df_raw = pd.DataFrame(df)
    df_raw["price"] = df_raw["price"].str.replace("£", "").astype(float)
    paths = get_output_paths()
    df_raw.to_csv(paths["processed"], index=False)
    return df_raw.to_dict(orient="records")
