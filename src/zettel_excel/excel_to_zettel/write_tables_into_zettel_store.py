from os import write

import requests

def write_tables_into_zettel_store(zettel_id: str, encoded_tables: str) -> str:
        base_url = "http://localhost:23123/z/"
        url = base_url + zettel_id
        meta_data = requests.get(url + "?part=meta")
        title = zettel_id
        for i in meta_data.text.split("\n"):
                if i.startswith("title:"):
                        title = i.split(":")[1].strip()
                        break
        headers = { "Content-Type": "text/plain; charset=utf-8" }
        meta = f'title: {title}\nsyntax: zmk'
        content = encoded_tables
        data = meta + "\n\n" + content
        try:
                response = requests.put(url, data=data,
                                       headers=headers)
                if response.status_code == 204:
                        return f"Zettel {zettel_id} erfolgreich aktualisiert."
                else:
                        raise ValueError(response.status_code)
        except Exception as e:
                raise ValueError(f"Fehler beim Aktualisieren von Zettel {zettel_id}: {e}")

