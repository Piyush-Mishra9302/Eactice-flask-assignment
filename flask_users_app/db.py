
import mysql.connector
from mysql.connector import Error
from config import Config

def get_db_connection():
    """Create and return a new MySQL connection using values from Config."""
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DATABASE,
    )
