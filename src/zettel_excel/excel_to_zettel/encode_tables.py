import pandas as pd


def encode_tables(tables: list[pd.DataFrame]) -> str:
    encoded_tables = []
    for table in tables:
        encoded_tables.append(encode_rows(table))
    return "\n---\n".join(encoded_tables)

def encode_rows(table: pd.DataFrame) -> str:
    encoded_rows = []
    for _, row in table.iterrows():
        encoded_rows.append(encode_cells(row))
    return "\n".join(encoded_rows)

def encode_cells(row: pd.Series) -> str:
    encoded_cells = []
    for cell in row:
        if pd.isna(cell):
            encoded_cells.append("")
        else:
            encoded_cells.append(f"{cell}")
    return "|" + "|".join(encoded_cells) + "|"
