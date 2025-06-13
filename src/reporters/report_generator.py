import pandas as pd
from src.utils.helpers import get_output_paths

def generate_report(df, **kwargs):

    df = pd.DataFrame(df)
    avg_price = df["price"].mean()
    max_price = df["price"].max()
    min_price = df["price"].min()
    html = f"""
    <html>
      <head><title>Books Report</title></head>
      <body>
        <h1>Books Statistics</h1>
        <ul>
          <li>Average price: £{avg_price:.2f}</li>
          <li>Max price: £{max_price:.2f}</li>
          <li>Min price: £{min_price:.2f}</li>
        </ul>
      </body>
    </html>
    """
    path = get_output_paths()["report"]
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path
