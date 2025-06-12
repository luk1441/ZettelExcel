import pandas as pd
import os

def write_tables_into_excel(zettel_id: str, tables: list[pd.DataFrame]) -> str:
    output_dir = "./excel"
    output_path = os.path.join(output_dir, f"{zettel_id}.xlsx")

    os.makedirs(output_dir, exist_ok=True)

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f"Tabelle {i+1}", index=False,
                           header=False)

    return f"Datei '{zettel_id}.xlsx' wurde erfolgreich erstellt."


