import requests  # 1. Importiere das Modul für HTTP-Anfragen

def get_zettel(zettel_id):
    """
    Ruft den Inhalt eines Zettels aus dem Zettelstore anhand seiner ID ab.
    Gibt den Markdown-Inhalt des Zettels zurück (bzw. auf der Konsole aus).
    """

    # 2. Basis-URL des lokal laufenden Zettelstores (Standard-Port: 23123)
    base_url = "http://localhost:23123/z/"

    # 3. Zusammensetzen der vollständigen URL mit der Zettel-ID
    url = f"{base_url}{zettel_id}?enc=sz&parseonly"

    try:
        # 4. HTTP-GET-Anfrage an die API senden
        response = requests.get(url)
        zettel_content = response.text
        return zettel_content

    except requests.exceptions.ConnectionError:
        # 5. Fehlerbehandlung: Verbindung zum Server nicht möglich
        connection_error = "Verbindung zum Zettelstore fehlgeschlagen. Läuft der Server?"
        return connection_error
