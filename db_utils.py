import psycopg2

def connect_to_database(config):
    """Establece una conexión a la base de datos PostgreSQL."""
    return psycopg2.connect(**config)


def fetch_tables_and_columns(cursor):
    """Obtiene todas las tablas y columnas del esquema público."""
    cursor.execute("""
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
    """)
    return cursor.fetchall()


def fetch_column_data(cursor, table, column):
    """Obtiene todos los datos de una columna específica."""
    query = f"SELECT {column} FROM {table} WHERE {column} IS NOT NULL"
    cursor.execute(query)
    return cursor.fetchall()