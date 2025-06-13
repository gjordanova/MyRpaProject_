import pandas as pd

def validate_data(df, **kwargs):

    df = pd.DataFrame(df)
    assert (df["price"] > 0).all(), "Some of the prices are unknown !"
    return df.to_dict(orient="records")
