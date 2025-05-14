import requests

def get_zettel_content(zettel_id):
    # Beispiel-URL: passe sie an den tatsächlichen Zettelstore an
    url = f"https://api.zettelstore.example.com/zettel/{zettel_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Fehler bei HTTP-Fehlercodes auslösen

        data = response.json()
        content = data.get('content')

        if content:
            print(f"Zettel-Inhalt (ID: {zettel_id}):\n{content}")
        else:
            print(f"Kein Inhalt für Zettel mit ID {zettel_id} gefunden.")

    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen des Zettels: {e}")

# Beispielaufruf
zettel_id = "abc123"
get_zettel_content(zettel_id)
