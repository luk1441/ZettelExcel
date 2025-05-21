def extrahiere_tabellen(block_content):
    """
    Diese Funktion extrahiert alle Tabellen aus dem gegebenen Blockinhalt,
    auch verschachtelte Tabellen werden erkannt.
    """
    tabellen_liste = []

    def suche_tabellen(inhalt):
        if isinstance(inhalt, list):
            if len(inhalt) > 0 and inhalt[0] == 'TABLE':
                tabellen_liste.append(inhalt)
            else:
                for element in inhalt:
                    suche_tabellen(element)

    suche_tabellen(block_content)
    return tabellen_liste


# Test 1 – einfache Tabelle
test_content = [
    ['PARA', ['TEXT', 'Beispiel']],
    ['TABLE',
        [['CELL', ['TEXT', 'Name']], ['CELL', ['TEXT', 'Alter']]],
        [['CELL', ['TEXT', 'Max']], ['CELL', ['TEXT', '25']]]
    ]
]

# Test 2 – verschachtelte Tabelle
test_content_nested = [
    ['TABLE',
        [['CELL', ['TEXT', 'Name']],
         ['CELL', ['TABLE',
             [['CELL', ['TEXT', 'Verschachtelt']], ['CELL', ['TEXT', 'Ja']]]
         ]]]
    ]
]

# Funktion aufrufen und Ergebnisse ausgeben
print("Einfache Tabelle:")
print(extrahiere_tabellen(test_content))

print("\nVerschachtelte Tabelle:")
print(extrahiere_tabellen(test_content_nested))
