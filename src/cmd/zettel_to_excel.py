from src.zettel_excel.zettel_to_excel.main import zettel_to_excel
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Fehler: Keine Zettelnummer angegeben. "
              "Bitte geben Sie eine Zettelnummer an.")
        sys.exit(1)

    zettel_id = sys.argv[1].strip()

    result = zettel_to_excel(zettel_id)

    if result["error"]:
        print(f"Fehler: {result['error']}")
    else:
        print(result["value"])
