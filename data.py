import csv
import os
import psycopg2
from db import get_one, get_all

<<<<<<< Updated upstream

def varda_diena(vards):
    sql = "SELECT * FROM vardadienas WHERE vards=%s ORDER BY vards"
    t = (vards,)
    atbilde = get_one(sql, t)
    return atbilde

def varda_dala(teksts):
    sql = "SELECT * FROM vardadienas WHERE vards LIKE '%%s%' ORDER BY vards"
    t = (vards,)
    atbilde = get_all(sql, t)
    return atbilde

def menesa_vardi(menesis):
    sql = "SELECT * FROM vardadienas WHERE menesis=%s ORDER BY diena"
    m = (menesis,)
    atbilde = get_all(sql, m)
    return atbilde


def diena(menesis, diena):
    sql = "SELECT * FROM vardadienas WHERE menesis=%s AND diena=%s"
    atbilde = get_all(sql, (menesis, diena))
    return atbilde


def statistika(menesis='visi'):
    if menesis == 'visi':
        c.execute('''SELECT menesis, diena, count(vards) from vardadienas GROUP BY menesis, diena ORDER BY menesis ASC, diena ASC''')
    else:
        c.execute('SELECT menesis, diena, count(vards) from vardadienas WHERE menesis=? GROUP BY menesis, diena ORDER BY menesis ASC, diena ASC', (menesis,))
    return c.fetchall()
=======
# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
# Vienkāršam testam var nomainīt šīs vērtības pret konkrētiem lielumiem

ELEPHANT_HOST = "balarama.db.elephantsql.com"
ELEPHANT_NAME = "kfdthoqa"
ELEPHANT_PASSWORD = "l8NuOnY1jLFNtI-gHoYmw4-ytDiPPHob"


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
>>>>>>> Stashed changes
