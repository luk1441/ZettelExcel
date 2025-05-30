import re

import pandas as pd

def parse_tables(encoded_tables: list[str]) -> list[pd.DataFrame]:
    parsed_tables = []
    for encoded_table in encoded_tables:
        column_length = encoded_table.split('((CELL')[1].count('(CELL') + 1
        encoded_cells = re.findall(r'\(CELL[^)]*?\)', encoded_table)
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
        cell = encoded_cell.replace('(CELL', '')
        if cell == "":
            cells.append(cell)
        else:
            encoded_contents = [match[1:-1].strip() for match in re.findall(r'\([^()]*\)', cell)]
            content = parse_contents(encoded_contents)
            cells.append(content)
    return cells

def parse_contents(encoded_contents: list[str]) -> str:
    content = ""
    for encoded_content in encoded_contents:
        content_key, content_value = encoded_content.split(" ", 1)
        match content_key:
            case "TEXT":
                content_value = content_value.replace('"', '')
                content += f"{content_value}"
            case _:
                pass
    return content
