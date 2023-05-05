# This file is a script on how to load CSV data into the database using psycopg2
import psycopg2

# Link the database called demo_database1
conn = psycopg2.connect("host=localhost dbname=CAB_database user=postgres")
cur = conn.cursor()

# This command can only be executed once after the table has been created, comment out
cur.execute("""
    CREATE TABLE vmt_data_table(
        mun_name varchar(50),
        county varchar(50),
        mpo varchar(5),
        mpo_year integer,
        combo_long_haul bigint,
        combo_short_haul bigint,
        intercity_bus bigint,
        light_com_truck bigint,
        motor_home bigint,
        motor_cycles bigint,
        passenger_cars bigint,
        passenger_trucks bigint,
        refuse_truck bigint,
        school_bus bigint,
        single_long_haul bigint,
        single_short_haul bigint,
        transit_bus bigint,
        vmt_total bigint
    )
""")

with open('/home/lion/github-classroom/TCNJ-degoodj/cab-project-6/data_files/adjusted_vmt_data.csv', 'r') as f:
    
    next(f)
    cur.copy_from(f, 'vmt_data_table', sep=',')

conn.commit()

cur.execute('SELECT * FROM vmt_data_table')

all = cur.fetchall()