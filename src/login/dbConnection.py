import psycopg2

con = cur = None


def connect():
    global con, cur

    try:
        con = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='parking'
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