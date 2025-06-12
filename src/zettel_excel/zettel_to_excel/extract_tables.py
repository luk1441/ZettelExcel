def extract_tables(zettel_content: str) -> list[str]:
    tables = []
    depth_count = 0
    start_index = -1

    for i, char in enumerate(zettel_content):
        if char == '(' and zettel_content[i:i + 7] == '(TABLE ':
            start_index = i
            depth_count += 1
        elif char == '(':
            if depth_count != 0:
                depth_count += 1
        elif char == ')':
            if depth_count != 0:
                depth_count -= 1
            if start_index != -1 and depth_count == 0:
                tables.append(zettel_content[start_index:i + 1])
                start_index = -1
    return tables
