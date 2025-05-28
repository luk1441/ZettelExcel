from src.zettel_excel.zettel_to_excel.extract_tables import extract_tables
from src.zettel_excel.zettel_to_excel.get_zettel import get_zettel
from src.zettel_excel.zettel_to_excel.zettel_guard import validate_zettelnummer
from src.zettel_excel.zettel_to_excel.parse_sz import parse_sz


def zettel_to_excel(zettel_id: str):
    valid_id = validate_zettelnummer(zettel_id)
    if valid_id == True:
        body = get_zettel(zettel_id)
        tables = extract_tables(body)
        parsed_table = parse_sz(tables)
    else:
        print("Error: Invalid Zettel ID")
    return parsed_table
