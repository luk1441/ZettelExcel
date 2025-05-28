from src.zettel_excel.excel_to_zettel."""??? Filename ändern. kein Punkt"""
from src.zettel_excel.excel_to_zettel.sz_to_zettel import embed_table_in_zettel
from src.zettel_excel.excel_to_zettel.convert_to_sz import to_sz_table

def excel_to_zettel():
    table = read_excel.file.py(zettel_id:str)
    sz_table = to_sz_table(table)
    zettel = embed_table_in_zettel(sz_table)
    return zettel
