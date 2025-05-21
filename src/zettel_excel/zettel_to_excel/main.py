from src.zettel_excel.zettel_to_excel.extract_table import extract_tables
from src.zettel_excel.zettel_to_excel.get_zettel import get_zettel
from src.zettel_excel.zettel_to_excel.zettel_guard import validate_zettelnummer


def zettel_to_excel(zettel_id: str):
    valid_id = validate_zettelnummer(zettel_id)
    body = get_zettel(valid_id)
    tables = extract_tables(body)
    return tables
