from src.zettel_excel.zettel_to_excel.extract_tables import extract_tables
from src.zettel_excel.zettel_to_excel.get_zettel import get_zettel
from src.zettel_excel.zettel_to_excel.write_tables_into_excel import write_tables_into_excel
from src.zettel_excel.zettel_to_excel.zettel_guard import validate_zettelnummer
from src.zettel_excel.zettel_to_excel.parse_sz import parse_sz


def zettel_to_excel(zettel_id: str) -> str:
    valid_id = validate_zettelnummer(zettel_id)
    if valid_id:
        body = get_zettel(zettel_id)
        # tables = extract_tables(body)
        # TODO: if extract tables works again - uncomment it and delete tables variables defined below
        tables = [
            '(TABLE ((CELL (TEXT "name")) (CELL (TEXT "age")) (CELL (TEXT "tabelleintaelle"))) ((CELL (TEXT "name")) (CELL (TEXT "52")) (CELL)))',
            '(TABLE ((CELL (TEXT "name")) (CELL (TEXT "age"))) ((CELL (TEXT "bran")) (CELL (TEXT "33"))))'
        ]
        parsed_table = parse_sz(tables)
        return write_tables_into_excel(zettel_id, parsed_table)
    else:
        raise "Error: Invalid Zettel ID"
