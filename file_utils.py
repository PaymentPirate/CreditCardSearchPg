import csv
import re

def initialize_csv(file_path):
    """Inicializa el archivo CSV escribiendo la cabecera."""
    with open(file_path, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Database", "Table", "Column", "Data Found"])


def append_to_csv(file_path, dbname, table, column, matches):
    """Escribe resultados en el archivo CSV."""
    with open(file_path, mode="a", newline="") as file:
        csv_writer = csv.writer(file)
        for match in matches:
            csv_writer.writerow([dbname, table, column, match])


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