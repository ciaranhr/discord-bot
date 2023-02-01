import mysql.connector
import config

gamedb = mysql.connector.connect(
    host = config.credentials.get_hostname(),
    user = config.credentials.get_username(),
    password = config.credentials.get_password()
)