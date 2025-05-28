from src.zettel_excel.zettel_to_excel.main import zettel_to_excel
import sys
import re

def is_valid_zettelnummer(zettelnummer: str) -> bool:
# Entfernt alle nicht-numerischen Zeichen und prüft, ob genau 16 Ziffern übrig bleiben
    return bool(re.fullmatch(r"\d{16}", zettelnummer))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Fehler: Bitte geben eine Zettelnummer ein.")
        sys.exit(1)

zettel_id_input = sys.argv[1].strip()

# Zusätzliche Prüfung auf unerlaubte Zeichen
if re.search(r"[^\d]", zettel_id_input):
    print("Fehler: Die Zettelnummer darf nur Ziffern (0–9) enthalten, keine Buchstaben oder Sonderzeichen.")
    sys.exit(1)

if not is_valid_zettelnummer(zettel_id_input):
    print("Fehler: Ungültige Zettelnummer. Eine Zettelnummer muss genau 16 Ziffern enthalten.")
    sys.exit(1)

result = zettel_to_excel(zettel_id_input)
print(result)
