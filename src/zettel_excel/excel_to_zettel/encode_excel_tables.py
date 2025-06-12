def encode_excel_tables(table_data: list[list[str]]) -> str:
    sz = "(TABLE\n"
    for row in table_data:
        sz += "  (ROW\n"
        for cell in row:
            sz += f'    (CELL (TEXT "{cell}"))\n'
        sz += "  )\n"
    sz += ")"
    return sz
