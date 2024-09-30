from sqlite3 import connect

conn = connect("banco.sql")

conn.execute("""
    CREATE TABLE IF NOT EXISTS Usuario(
        id serial,
        name varchar(80),"
        constraint user_pk primary key(id)"
    )
    """)

conn.commit()
