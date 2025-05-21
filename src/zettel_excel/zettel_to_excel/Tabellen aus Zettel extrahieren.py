def extrahiere_tabellen(block_content):
    table_list = []
    for element in block_content:
        if isinstance(element, list) and element[0] == 'TABLE':
            table_list.append(str(element))  # oder z.dumps(element)
    return table_list

# TESTDATEN
test_content = [
    ['PARA', ['TEXT', 'Im not a']],
    ['TABLE',
        [['CELL', ['TEXT', 'name']], ['CELL', ['TEXT', 'age']]],
        [['CELL', ['TEXT', 'luca']], ['CELL', ['TEXT', '27']]]
    ],
    ['PARA', ['TEXT', 'Table']]
]

# ERWARTETE AUSGABE
expected = [
    "['TABLE', [['CELL', ['TEXT', 'name']], ['CELL', ['TEXT', 'age']]], [['CELL', ['TEXT', 'luca']], ['CELL', ['TEXT', '27']]]]"
]

# TEST
assert extrahiere_tabellen(test_content) == expected
print("Test bestanden ")

tables = extrahiere_tabellen(test_content)
print(tables)

