def validate_zettelnummer(zettelnummer: str) -> bool:
    # Prüft, ob die Zettelnummer nur aus Ziffern besteht
    # und genau 16 Zeichen lang ist.
    # Gibt True zurück, wenn beide Bedingungen erfüllt sind,
    # sonst False mit entsprechender Fehlermeldung.
    if not zettelnummer.isdigit():
        print("Fehler: Die Zettelnummer darf nur Ziffern enthalten.")
        return False
    if len(zettelnummer) != 14:
        print("Fehler: Die Zettelnummer muss genau 16 Stellen lang sein.")
        return False
    return True

def run_zettelnummer_check():
    # Fragt den Nutzer nach einer Zettelnummer über die Eingabeaufforderung
    # Validiert die Eingabe mit validate_zettelnummer().
    # Gibt eine Erfolgsmeldung aus, wenn die Eingabe gültig ist,
    # ansonsten eine Fehlermeldung und bricht den Vorgang ab.
    user_input = input("Bitte gib die Zettelnummer ein: ")
    if validate_zettelnummer(user_input):
        print(" Zettelnummer ist korrekt ,der Vorgang kann fortgesetzt werden.")
    else:
        print(" Vorgang abgebrochen ,eine ungültige Zettelnummer.")

if __name__ == "_main_":
    # Führt die Funktion run_zettelnummer_check aus,
    # wenn das Skript direkt gestartet wird.
    run_zettelnummer_check()



