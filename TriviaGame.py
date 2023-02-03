import mysql.connector
import config


gamedb = mysql.connector.connect(
    host = config.credentials.get_hostname(),
    user = config.credentials.get_username(),
    password = config.credentials.get_password()
)

class Trivia():
    def __init__(self) -> None:
        pass

    def restart_trivia():
        pass