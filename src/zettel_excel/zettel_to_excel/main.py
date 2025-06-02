import logging

from src.zettel_excel.zettel_to_excel.extract_tables import extract_tables
from src.zettel_excel.zettel_to_excel.get_zettel import get_zettel
from src.zettel_excel.zettel_to_excel.validate_zettel_id import validate_zettel_id
from src.zettel_excel.zettel_to_excel.parse_tables import parse_tables
from src.zettel_excel.zettel_to_excel.write_tables_into_excel import write_tables_into_excel


def zettel_to_excel(zettel_id: str) -> dict:
    try:    
        validate_zettel_id(zettel_id)
        zettel = get_zettel(zettel_id)
        encoded_tables = extract_tables(zettel)
        tables = parse_tables(encoded_tables)
        message = write_tables_into_excel(zettel_id, tables) 
        return { "value": message, "error": None }
    except ValueError as err:
        return { "value": None, "error": err }
    except Exception as e:
        logging.error(f"Unerwarteter Fehler: {e}", exc_info=True)
        return { "value": None, "error": "Unerwarteter Programmfehler. Bitte "
                                         "kontaktieren Sie den Support." }
