import pandas as pd
import os

def write_tables_into_excel(zettel_id: str, tables: list[list[list[str]]]) -> str:
    """
    :param zettel_id: id of the zettel
    :param tables: list of matrices containing the content of the table
    :return: None
    """
    output_dir = "./excel"
    output_path = os.path.join(output_dir, f"{zettel_id}.xlsx")

    os.makedirs(output_dir, exist_ok=True)

    dfs = []
    for table in tables:
        if table:
            dfs.append(pd.DataFrame(table))

    if not dfs:
        raise ValueError("No tables to write to Excel.")

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        for i, df in enumerate(dfs):
            df.to_excel(writer, sheet_name=f"Table {i+1}", index=False)

    return f"Successfully created {zettel_id}.xlsx"


