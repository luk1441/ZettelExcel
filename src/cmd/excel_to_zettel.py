from src.zettel_excel.excel_to_zettel.main import excel_to_zettel
import sys

if __name__ == '__main__':
    zettel_id_input = sys.argv[1]
    result = excel_to_zettel(zettel_id_input)
    print(result)