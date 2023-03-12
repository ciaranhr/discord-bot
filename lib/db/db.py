import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import lib.bot.config as config
import mysql.connector
from mysql.connector import errorcode

host = config.credentials.get_hostname()
user = config.credentials.get_username()
password = config.credentials.get_password()
db = config.credentials.get_db()

try:
    cnx = mysql.connector.connect(user=user,
                                database=db)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
