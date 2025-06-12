def encode_excel_tables(table_data: list[list[str]]) -> str:
    sz = "(TABLE\n"
    for row in table_data:
        sz += "  (ROW\n"
        for cell in row:
            sz += f'    (CELL (TEXT "{cell}"))\n'
        sz += "  )\n"
    sz += ")"
    return sz

example = [
    ["Name", "Beruf", "Alter"],
    ["Max", "Informatiker", "30"],
    ["Lisa", "Designer", "28"]
]

sz_result = to_sz_table(example)
print(sz_result)
