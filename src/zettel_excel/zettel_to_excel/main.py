import logging

from src.zettel_excel.zettel_to_excel.extract_tables import extract_tables
from src.zettel_excel.zettel_to_excel.get_zettel import get_zettel
from src.zettel_excel.zettel_to_excel.parse_tables import parse_tables
from src.zettel_excel.zettel_to_excel.write_tables_into_excel import write_tables_into_excel

from src.zettel_excel.shared.validate_zettel_id import validate_zettel_id


def zettel_to_excel(zettel_id: str) -> dict:
    try:
        validate_zettel_id(zettel_id)
        zettel_content = get_zettel(zettel_id)
        encoded_tables = extract_tables(zettel_content)
        tables = parse_tables(encoded_tables)
        message = write_tables_into_excel(zettel_id, tables)
        return { "value": message, "error": None }
    except ValueError as err:
        return { "value": None, "error": err }
    except Exception as e:
        logging.error(f"Unerwarteter Fehler: {e}", exc_info=True)
        return { "value": None, "error": "Unerwarteter Programmfehler. Bitte "
                                         "kontaktieren Sie den Support." }
