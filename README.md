
# Credit Card Scanner

Este proyecto es un script modularizado en Python diseñado para buscar números de tarjetas de crédito en todas las tablas y columnas de una base de datos PostgreSQL. Además, identifica el tipo de tarjeta (Visa, MasterCard, American Express, etc.) y genera un archivo CSV con los resultados.

## 🚀 Funcionalidades

- Escanea todas las tablas y columnas de una base de datos PostgreSQL.  
- Identifica patrones que coincidan con números de tarjetas de crédito (13-19 dígitos).  
- Clasifica el tipo de tarjeta:  
  - Visa  
  - MasterCard  
  - American Express  
  - Discover  
  - JCB  
  - Diners Club  
  - Otros  
- Genera un archivo CSV con los resultados, incluyendo:  
  - Base de datos  
  - Tabla  
  - Columna  
  - Número de tarjeta encontrado  
  - Tipo de tarjeta  
- Modularizado para facilitar la reutilización y mantenimiento.

## 📂 Estructura del Proyecto

```
credit_card_scanner/
├── config.py           # Archivo de configuración
├── db_utils.py         # Funciones relacionadas con la base de datos
├── file_utils.py       # Funciones relacionadas con la gestión de archivos y patrones
├── scanner.py          # Script principal
└── README.md           # Documentación del proyecto
```

## ⚙️ Configuración

1. **Clona el repositorio**:  
   ```bash
   git clone https://github.com/tu_usuario/credit_card_scanner.git
   cd credit_card_scanner
   ```

2. **Edita el archivo `config.py`**:  
   Configura tus credenciales y parámetros de conexión a PostgreSQL:  
   ```python
   DB_CONFIG = {
       "host": "localhost",
       "database": "tu_base_de_datos",
       "user": "tu_usuario",
       "password": "tu_contraseña"
   }

   OUTPUT_FILE = "credit_card_search_results_with_types.csv"
   CREDIT_CARD_PATTERN = r'\b(?:\d[ -]*?){13,19}\b'
   ```

3. **Instala las dependencias**:  
   Asegúrate de tener Python 3.7+ instalado y ejecuta:  
   ```bash
   pip install psycopg2
   ```

## 🏃‍♂️ Ejecución

1. **Ejecuta el script principal**:  
   ```bash
   python scanner.py
   ```

2. **Revisa los resultados**:  
   Los resultados se guardarán en el archivo `credit_card_search_results_with_types.csv`, con el siguiente formato:  

   | Database       | Table          | Column        | Data Found         | Card Type         |  
   |----------------|----------------|---------------|--------------------|-------------------|  
   | my_database    | clientes       | numero_tarjeta | 4111111111111111   | Visa              |  
   | my_database    | transacciones  | tarjeta       | 5500000000000004   | MasterCard        |  
   | my_database    | pagos          | card_number   | 378282246310005    | American Express  |  

## 🛠️ Tecnologías Usadas

- **Python 3.7+**  
- **PostgreSQL**  
- **psycopg2**: Librería para conectarse a PostgreSQL desde Python.  

## 📋 Notas

- **Seguridad**: Este script está diseñado para fines de auditoría y análisis. Asegúrate de cumplir con las leyes y normativas aplicables al trabajar con datos sensibles.  
- **PCI DSS**: Si estás buscando datos de tarjetas de crédito, asegúrate de manejar la información de acuerdo con los estándares PCI DSS.  

## 🖇️ Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el script o agregar funcionalidades, abre un [issue](https://github.com/tu_usuario/credit_card_scanner/issues) o envía un [pull request](https://github.com/tu_usuario/credit_card_scanner/pulls).  

## 🧑‍💻 Autor

**[Ignacio Cataldo]**  
- GitHub: [https://github.com/PaymentPirate/](https://github.com/PaymentPirate/)  

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
