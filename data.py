import os
import psycopg2

# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
# Vienkāršam testam var nomainīt šīs vērtības pret konkrētiem lielumiem

ELEPHANT_HOST = "balarama.db.elephantsql.com" # os.getenv("ELEPHANT_HOST") # "balarama.db.elephantsql.com"
ELEPHANT_NAME = "kfdthoqa" # os.getenv("ELEPHANT_NAME") # "manadb"
ELEPHANT_PASSWORD = "l8NuOnY1jLFNtI-gHoYmw4-ytDiPPHob" # os.getenv("ELEPHANT_PASSWORD") # "managaraparole"


def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    cur.close()
    conn.close()
    return result