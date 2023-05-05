# This file is a script on how to load CSV data into the database using psycopg2
import psycopg2

# Link the database called demo_database1
conn = psycopg2.connect("host=localhost dbname=CAB_database user=postgres")
cur = conn.cursor()

# This command can only be executed once after the table has been created, comment out
cur.execute("""
    CREATE TABLE zip_code_table(
        zip integer PRIMARY KEY,
        city varchar(50),
        state char(2),
        county_name varchar(50) 
    )
""")

with open('/home/lion/github-classroom/TCNJ-degoodj/cab-project-6/data_files/zip_codes.csv', 'r') as f:
    
    next(f)
    cur.copy_from(f, 'zip_code_table', sep=',')

conn.commit()

cur.execute('SELECT * FROM zip_code_table')

all = cur.fetchall()