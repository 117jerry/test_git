import psycopg2
from faker import Faker

faker = Faker()


def get_database_connection():
    try:
        con = psycopg2.connect(
            host="rajje.db.elephantsql.com",
            database='dmuhvnag',
            user='dmuhvnag',
            password='Pibk3nJehuU-kusJpY0PoC0Ad96Sgjqb'
        )
        return con
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        exit(1)


def select_all_from_table(table_name):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            curr.execute(f"SELECT * FROM {table_name}")
            return curr.fetchall()


def execute_query(query, parameters=None):
    with get_database_connection() as connection:
        with connection.cursor() as curr:
            # Use parameterized queryies to avoid sql injection
            curr.execute(query, parameters)
        connection.commit()


def add_user(first_name, last_name, address, phone, start_date, role):
    # Create dic of values
    values = dict(first_name=first_name, last_name=last_name, address=address, phone=phone, start_date=start_date,
                  role=role)
    # Build the query to be executed 
    query = """INSERT INTO users (first_name, last_name, address, phone, start_date, role)
                VALUES ( %(first_name)s, %(last_name)s, %(address)s, %(phone)s, %(start_date)s, %(role)s)"""
    
    execute_query(query, values)


def main():
    # Add 5 random users to the database
    for _ in range(5):
        # Generate random data 
        fn = faker.first_name()
        ln = faker.last_name()
        addr = faker.address()
        phone = faker.phone_number()
        start_date = faker.date_time_between(start_date='-5y', end_date='now')
        role = faker.random_int(0, 5)
        # Add the user to the db 
        add_user(fn, ln, addr,phone, start_date, role)
    
    # Display all users
    for row in select_all_from_table('users'):
        print(row)


main()
