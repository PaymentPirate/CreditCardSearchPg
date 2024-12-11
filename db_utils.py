import logging
import psycopg2

def connect_to_database(config):
    """Establece una conexión a la base de datos PostgreSQL."""
    try:
        conn = psycopg2.connect(**config)
        logging.debug("Conexión a la base de datos PostgreSQL exitosa.")
        return conn
    except Exception as e:
        logging.error("Error al conectar a la base de datos.", exc_info=True)
        raise

def fetch_tables_and_columns(cursor):
    """Obtiene todas las tablas y columnas del esquema público."""
    try:
        query = """
            SELECT table_name, column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
        """
        cursor.execute(query)
        tables_columns = cursor.fetchall()
        logging.debug(f"Tablas y columnas obtenidas: {len(tables_columns)} columnas encontradas.")
        return tables_columns
    except Exception as e:
        logging.error("Error al obtener las tablas y columnas.", exc_info=True)
        raise

def fetch_column_data(cursor, table, column):
    """Obtiene todos los datos de una columna específica."""
    try:
        # Usar LOWER para manejar datos en minúsculas
        query = f"SELECT LOWER({column}) FROM {table} WHERE {column} IS NOT NULL"
        cursor.execute(query)
        rows = cursor.fetchall()
        logging.debug(f"{len(rows)} filas obtenidas de {table}.{column}.")
        return rows
    except Exception as e:
        logging.error(f"Error al obtener datos de {table}.{column}.", exc_info=True)
        raise
