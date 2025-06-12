import os
import pandas as pd
import requests

def write_tables_into_zettel_store(zettel_id: str, encoded_tables: str) -> str:
        print(zettel_id, encoded_tables)
        """
        # TODO
         # PUT-Request vorbereiten
        url = f"http://localhost:23123/store/{zettelnummer}"
        updated_zettel = {
            "title": title,
            "content": content
        }

        response = requests.put(url, json=updated_zettel)

        if response.status_code == 200:
            print(f"Zettel {zettelnummer} erfolgreich aktualisiert.")
        else:
            print(f"Fehler bei Zettel {zettelnummer}: {response.status_code}")
            print(response.text)
        """
        return f"Zettel {zettel_id} erfolgreich aktualisiert."
