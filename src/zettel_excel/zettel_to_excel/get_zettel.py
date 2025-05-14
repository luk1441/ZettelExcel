import requests  # 1. Importiere das Modul für HTTP-Anfragen


def get_zettel_content(zettel_id):
    """
    Ruft den Inhalt eines Zettels aus dem Zettelstore anhand seiner ID ab.
    Gibt den Markdown-Inhalt des Zettels zurück (bzw. auf der Konsole aus).
    """

    # 2. Basis-URL des lokal laufenden Zettelstores (Standard-Port: 23123)
    base_url = "http://localhost:23123/api/zettel/"

    # 3. Zusammensetzen der vollständigen URL mit der Zettel-ID
    url = f"{base_url}{zettel_id}"

    try:
        # 4. HTTP-GET-Anfrage an die API senden
        response = requests.get(url)

        # 5. Prüfen, ob die Anfrage erfolgreich war (Statuscode 200)
        if response.status_code == 200:
            print("✅ Zettel erfolgreich abgerufen:\n")
            print(response.text)  # 6. Den Zettelinhalt anzeigen
            return response.text

        # 7. Fehlerbehandlung: Zettel nicht gefunden
        elif response.status_code == 404:
            print("❌ Zettel mit dieser ID wurde nicht gefunden.")

        # 8. Andere Fehlercodes
        else:
            print(f"❌ Fehler beim Abrufen: Statuscode {response.status_code}")
            print(response.text)

    except requests.exceptions.ConnectionError:
        # 9. Fehlerbehandlung: Verbindung zum Server nicht möglich
        print("❌ Verbindung zum Zettelstore fehlgeschlagen. Läuft der Server?")


# 10. Test bzw. Einstiegspunkt für das Skript
if __name__ == "__main__":
    zettel_id = input("Bitte gib eine Zettel-ID ein: ")  # z. B. 0000100000000000
    get_zettel_content(zettel_id)

