from datetime import datetime

def embed_table_in_zettel(sz_table_str: str, zettel_id="zettel001"):
    now = datetime.utcnow().isoformat() + "Z"
    return f'''(zettel
  (id "{zettel_id}")
  (title "Titel")
  (created "{now}")
  (modified "{now}")
  (content {sz_table_str})
)'''
