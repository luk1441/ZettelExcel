import pandas as pd


def encode_tables(tables: list[pd.DataFrame]) -> list[str]:
    encoded_tables = []
    for table in tables:
        encoded_tables.append(f"(TABLE {encode_rows(table)})")
    return encoded_tables

def encode_rows(table: pd.DataFrame) -> str:
    encoded_rows = []
    for _, row in table.iterrows():
        encoded_rows.append(f"({encode_cells(row)})")
    return " ".join(encoded_rows)

def encode_cells(row: pd.Series) -> str:
    encoded_cells = []
    for cell in row:
        encoded_cells.append(f"(CELL (){f' (TEXT "{cell}")' if not pd.isna(cell) else ""})")
    return " ".join(encoded_cells)
