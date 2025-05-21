import re

def parse_sz(sz_table_list: list[str]) -> list[list]:
    """
    :param sz_table_list: list of sz encoded tables
    :return: list of elements in sz table
    """
    parsed_tables = []
    for sz_table in sz_table_list:
        column_length = sz_table.split('((CELL')[1].count('(CELL') + 1
        raw_cells = re.findall(r'\(CELL[^)]*?\)', sz_table)
        cells = parse_cells(raw_cells)
        table_rows = []
        for i in range(0, len(cells), column_length):
            row = cells[i:i + column_length]
            table_rows.append(row)

        parsed_tables.append(table_rows)
    return parsed_tables

def parse_cells(raw_cells: list[str]) -> list[list]:
    """
    :param raw_cells: list of raw cells in sz encoding
    :return: list of cell content
    """
    cells = []
    for raw_cell in raw_cells:
        cell = raw_cell.replace('(CELL', '')
        if cell == "":
            cells.append(cell)
        else:
            raw_contents = [match[1:-1].strip() for match in re.findall(r'\([^()]*\)', cell)]
            content = parse_content(raw_contents)
            cells.append(content)
    return cells

def parse_content(raw_contents: list[str]) -> str:
    """
    :param raw_contents: list of raw contents in cell in sz encoding
    :return: parsed content of cell
    """
    content = ""
    for raw_content in raw_contents:
        content_key, content_value = raw_content.split(" ", 1)
        match content_key:
            case "TEXT":
                content_value = content_value.replace('"', '')
                content += f"{content_value}"
            case _:
                pass
    return content
