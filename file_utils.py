import csv
import re


def initialize_csv(file_path):
    """Inicializa el archivo CSV escribiendo la cabecera."""
    with open(file_path, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Database", "Table", "Column", "Data Found", "Card Type"])


def identify_card_type(card_number):
    """
    Identifica el tipo de tarjeta de crédito basado en el número.

    Args:
        card_number (str): Número de tarjeta de crédito.

    Returns:
        str: Tipo de tarjeta (Visa, MasterCard, AmEx, etc.).
    """
    if card_number.startswith(('4',)):
        return "Visa"
    elif card_number.startswith(('51', '52', '53', '54', '55')) or \
            card_number.startswith(tuple(str(i) for i in range(2221, 2721))):
        return "MasterCard"
    elif card_number.startswith(('34', '37')):
        return "American Express"
    elif card_number.startswith(('6',)):
        return "Discover"
    elif card_number.startswith(('35',)):
        return "JCB"
    elif card_number.startswith(('30', '36', '38', '39')):
        return "Diners Club"
    else:
        return "Unknown"


def append_to_csv_with_card_type(file_path, dbname, table, column, matches):
    """Escribe resultados en el archivo CSV incluyendo el tipo de tarjeta."""
    with open(file_path, mode="a", newline="") as file:
        csv_writer = csv.writer(file)
        for match in matches:
            card_type = identify_card_type(match.replace(" ", "").replace("-", ""))
            csv_writer.writerow([dbname, table, column, match, card_type])


def search_pattern_in_data(rows, pattern):
    """Busca coincidencias con un patrón en los datos."""
    matches = []
    compiled_pattern = re.compile(pattern)
    for row in rows:
        value = row[0]
        if value is not None:
            value_str = str(value)
            matches.extend(compiled_pattern.findall(value_str))
    return matches