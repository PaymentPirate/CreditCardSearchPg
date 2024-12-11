import logging
from config import DB_CONFIG, OUTPUT_FILE, CREDIT_CARD_PATTERN
from db_utils import connect_to_database, fetch_tables_and_columns, fetch_column_data
from file_utils import initialize_csv, append_to_csv_with_card_type, search_pattern_in_data

# Configurar el logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("scanner.log"),
        logging.StreamHandler()
    ]
)

def main():
    """Función principal que ejecuta el script."""
    try:
        # Intentar conectar a la base de datos
        logging.info("Conectando a la base de datos...")
        conn = connect_to_database(DB_CONFIG)
        cur = conn.cursor()
        logging.info("Conexión a la base de datos establecida.")

        # Inicializar el archivo CSV
        logging.info(f"Inicializando el archivo CSV: {OUTPUT_FILE}")
        initialize_csv(OUTPUT_FILE)

        # Obtener las tablas y columnas
        logging.info("Obteniendo tablas y columnas del esquema público...")
        tables_columns = fetch_tables_and_columns(cur)
        logging.info(f"Tablas y columnas obtenidas: {len(tables_columns)} columnas encontradas.")

        # Procesar cada tabla y columna
        for table, column, data_type in tables_columns:
            logging.debug(f"Procesando {table}.{column} (tipo {data_type})...")
            if data_type in ['text', 'varchar', 'char', 'integer', 'bigint', 'numeric']:
                rows = fetch_column_data(cur, table, column)
                logging.debug(f"{len(rows)} filas obtenidas de {table}.{column}.")
                matches = search_pattern_in_data(rows, CREDIT_CARD_PATTERN)
                if matches:
                    logging.info(f"Se encontraron coincidencias en {table}.{column}: {matches}")
                    append_to_csv_with_card_type(OUTPUT_FILE, conn.info.dbname, table, column, matches)
                else:
                    logging.debug(f"No se encontraron coincidencias en {table}.{column}.")

        # Cerrar conexión
        cur.close()
        conn.close()
        logging.info("Conexión cerrada y proceso completado.")
    except Exception as e:
        logging.error(f"Error en la ejecución: {e}", exc_info=True)


if __name__ == "__main__":
    main()
