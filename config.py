# Configuración de la base de datos PostgreSQL
DB_CONFIG = {
    "host": "localhost",  # Cambiar a la dirección de tu servidor PostgreSQL
    "database": "tu_base_de_datos",  # Cambiar al nombre de tu base de datos
    "user": "tu_usuario",  # Cambiar al usuario de la base de datos
    "password": "tu_contraseña"  # Cambiar a la contraseña de tu base de datos
}

# Archivo de salida para los resultados
OUTPUT_FILE = "credit_card_search_results.csv"

# Expresión regular para números de tarjetas de crédito (13-19 dígitos)
CREDIT_CARD_PATTERN = r'\b(?:\d[ -]*?){13,19}\b'