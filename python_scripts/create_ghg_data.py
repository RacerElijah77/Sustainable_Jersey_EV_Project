# This file is a script on how to load CSV data into the database using psycopg2
import psycopg2

# Link the database called demo_database1
conn = psycopg2.connect("host=localhost dbname=CAB_database user=postgres")
cur = conn.cursor()

# This command can only be executed once after the table has been created, comment out
cur.execute("""
    CREATE TABLE ghg_data_table(
        mun_name varchar(50),
        county varchar(50),
        mpo varchar(5),
        mpo_year integer,
        combo_long_haul decimal,
        combo_short_haul decimal,
        intercity_bus decimal,
        light_com_truck decimal,
        motor_home decimal,
        motor_cycles decimal,
        passenger_cars decimal,
        passenger_trucks decimal,
        refuse_truck decimal,
        school_bus decimal,
        single_long_haul decimal,
        single_short_haul decimal,
        transit_bus decimal,
        ghg_total decimal
    )
""")

with open('/home/lion/github-classroom/TCNJ-degoodj/cab-project-6/data_files/adjusted_ghg_data.csv', 'r') as f:
    
    next(f)
    cur.copy_from(f, 'ghg_data_table', sep=',')

conn.commit()

cur.execute('SELECT * FROM ghg_data_table')

all = cur.fetchall()