import psycopg2

con = cur = None


def connect():
    global con, cur

    try:
        con = psycopg2.connect(
            host='rajje.db.elephantsql.com',
            database='dmuhvnag',
            user='dmuhvnag',
            password='Pibk3nJehuU-kusJpY0PoC0Ad96Sgjqb'
        )
        cur = con.cursor()
    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
        print(e)


def getDB():
    if not (con and cur):
        connect()
    return con, cur


def closeDB():
    if cur and con is not None:
        cur.close()
        con.close()
        print('closing cur and con...')