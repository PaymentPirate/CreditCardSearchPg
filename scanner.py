from config import DB_CONFIG, OUTPUT_FILE, CREDIT_CARD_PATTERN
from db_utils import connect_to_database, fetch_tables_and_columns, fetch_column_data
from file_utils import initialize_csv, append_to_csv, search_pattern_in_data


def main():
    """Función principal que ejecuta el script."""
    # Conectar a la base de datos
    conn = connect_to_database(DB_CONFIG)
    cur = conn.cursor()

    # Inicializar el archivo CSV
    initialize_csv(OUTPUT_FILE)

    # Obtener las tablas y columnas
    tables_columns = fetch_tables_and_columns(cur)

    # Procesar cada tabla y columna
    for table, column, data_type in tables_columns:
        if data_type in ['text', 'varchar', 'char', 'integer', 'bigint', 'numeric']:
            print(f"Buscando en {table}.{column} (tipo {data_type})...")
            rows = fetch_column_data(cur, table, column)
            matches = search_pattern_in_data(rows, CREDIT_CARD_PATTERN)
            if matches:
                append_to_csv(OUTPUT_FILE, conn.info.dbname, table, column, matches)

    # Cerrar conexión
    cur.close()
    conn.close()

    print(f"Búsqueda completada. Los resultados están en el archivo {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()