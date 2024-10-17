# data_analysis_package/cleaning.py
import pandas as pd

def handle_missing_data(data: pd.DataFrame, method: str = 'drop') -> pd.DataFrame:
    if method == 'drop':
        return data.dropna(how='all')
    elif method == 'fill':
        return data.fillna(0)
    else:
        raise ValueError("Method must be 'drop' or 'fill'.")


