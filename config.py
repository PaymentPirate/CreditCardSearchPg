# Configuración de la base de datos PostgreSQL
DB_CONFIG = {
    "host": "localhost",
    "database": "tu_base_de_datos",
    "user": "tu_usuario",
    "password": "tu_contraseña"
}

# Archivo de salida para los resultados
OUTPUT_FILE = "credit_card_search_results_with_types.csv"

# Expresión regular para números de tarjetas de crédito (13-19 dígitos)
CREDIT_CARD_PATTERN = r'\b(?:\d[ -]*?){13,19}\b'
