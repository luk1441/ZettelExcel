def validate_zettel_id(zettel_id: str) -> None:
    if not zettel_id.isdigit() or len(zettel_id) != 14:
        raise ValueError(f"Invalide Zettelnummer '{zettel_id}'. Die "
                         f"Zettelnummer muss aus genau 14 Ziffern (0–9) "
                         f"bestehen.")
