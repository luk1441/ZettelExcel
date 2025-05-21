def validate_zettelnummer(zettelnummer: str) -> bool:
    # Prüft, ob die Zettelnummer nur aus Ziffern besteht
    # und genau 16 Zeichen lang ist.
    # Gibt True zurück, wenn beide Bedingungen erfüllt sind,
    # sonst False mit entsprechender Fehlermeldung.
    if not zettelnummer.isdigit():
        print("Fehler: Die Zettelnummer darf nur Ziffern enthalten.")
        return False
    if len(zettelnummer) != 16:
        print("Fehler: Die Zettelnummer muss genau 16 Stellen lang sein.")
        return False
    return True
