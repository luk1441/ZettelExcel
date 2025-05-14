from src.zettel_excel.zettel_to_excel.main import zettel_to_excel
import sys

if __name__ == '__main__':
    zettel_id_input = sys.argv[1]
    result = zettel_to_excel(zettel_id_input)
    print(result)
