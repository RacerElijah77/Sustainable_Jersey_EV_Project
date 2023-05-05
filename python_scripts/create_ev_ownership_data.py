# This file is a script on how to load CSV data into the database using psycopg2
import psycopg2

# Link the database called demo_database1
conn = psycopg2.connect("host=localhost dbname=CAB_database user=postgres")
cur = conn.cursor()

# This command can only be executed once after the table has been created, comment out
cur.execute("""
    CREATE TABLE ev_ownership_table(
        municipality varchar(50),
        county varchar(50),
        year integer,
        total_personal_vehicles integer,
        number_of_EVs varchar(10),
        percent_of_EVs varchar(10)
    )
""")

with open('/home/lion/github-classroom/TCNJ-degoodj/cab-project-6/data_files/adjusted_EV_data.csv', 'r') as f:
    
    next(f)
    cur.copy_from(f, 'ev_ownership_table', sep=',')

conn.commit()

cur.execute('SELECT * FROM ev_ownership_table')

all = cur.fetchall()