"""
Einstiegspunkt der ZettelExcel-Anwendung.
"""

def add(a: int | float, b: int | float) -> int | float:
    """
    Addiert zwei Zahlen (entweder int oder float) und gibt das Ergebnis zurück.

    Parameter:
    a (int | float): Die erste Zahl.
    b (int | float): Die zweite Zahl.

    Rückgabewert:
    int | float: Die Summe der beiden Zahlen.
    """
    return a + b

if __name__ == '__main__':
    add(2, 2)
