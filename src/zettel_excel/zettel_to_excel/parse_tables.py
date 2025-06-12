import re

import pandas as pd

def parse_tables(encoded_tables: list[str]) -> list[pd.DataFrame]:
    parsed_tables = []
    for encoded_table in encoded_tables:
        column_length = encoded_table.split('((CELL')[1].count('(CELL') + 1
        encoded_cells = encoded_table.split('(CELL (')[1:]
        cells = parse_cells(encoded_cells)
        table = []
        for i in range(0, len(cells), column_length):
            row = cells[i:i + column_length]
            table.append(row)
        parsed_tables.append(pd.DataFrame(table))
    return parsed_tables

def parse_cells(encoded_cells: list[str]) -> list[list]:
    cells = []
    for encoded_cell in encoded_cells:
        if '"' in encoded_cell:
            cells.append(re.search(r'"(.*?)"', encoded_cell).group(1))
        else:
            cells.append(None)
    return cells
