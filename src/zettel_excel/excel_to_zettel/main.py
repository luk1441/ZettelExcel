import logging

from src.zettel_excel.excel_to_zettel.read_excel_file import read_excel_file

from src.zettel_excel.shared.validate_zettel_id import validate_zettel_id


def excel_to_zettel(zettel_id: str) -> dict:
    try:    
        validate_zettel_id(zettel_id)
        excel_tables = read_excel_file(zettel_id)
        encoded_tables = encode_excel_tables(excel_tables)
        message = write_tables_into_zettel_store(zettel_id, encoded_tables)
        return { "value": message, "error": None }
    except ValueError as err:
        return { "value": None, "error": err }
    except Exception as e:
        logging.error(f"Unerwarteter Fehler: {e}", exc_info=True)
        return { "value": None, "error": "Unerwarteter Programmfehler. Bitte "
                                         "kontaktieren Sie den Support." }
