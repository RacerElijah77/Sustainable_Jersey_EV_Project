#! /usr/bin/python3
# <!-- Madison Bavosa, Emmanuel Pasteur, EJ Gasataya -->
# <!-- CSC 315 - Databases (UI For Group Project on Sustainable Jersey) -->
# <!-- Main Python file that will run the application via Flask communication -->

import psycopg2
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    rows = []
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows
 
# app.py (NEEDED TO CHANGE FOR CSS Linking)
app = Flask(__name__, template_folder='templates', static_folder = 'css')


# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

# Python route for handling GHG Query Range
@app.route('/ghg-handler', methods=['POST'])
def ghg_handler():
    rows = connect('SELECT ghg_table_temp.mun_name, ghg_table_temp.zip, ROUND(AVG(ghg_total), 2) ghg_total, contains_2_main.total_personal, contains_2_main.num_evs, ROUND(EV_ratio.percentage, 2) ' +
                   'FROM ghg_table_temp INNER JOIN contains_2_main ' +
                   'ON ghg_table_temp.zip = contains_2_main.zip AND ghg_table_temp.mun_name = contains_2_main.mun_name ' +
                   'INNER JOIN EV_ratio ON EV_ratio.zip = ghg_table_temp.zip ' +
                   'WHERE ghg_total > ' + request.form['ghg_min'] + ' AND ghg_total < ' + request.form['ghg_max'] + ' ' +
                   'GROUP BY (ghg_table_temp.mun_name, ghg_table_temp.zip, contains_2_main.total_personal, contains_2_main.num_evs, EV_ratio.percentage) ' +
                   'ORDER BY ghg_total DESC;')
    
    heads = ['Municipality', 'Zip Code', 'Total GHG Emissions', 'Number of Personal Vehicles', '# of EVs', 'Ratio of EVs %']
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/zip-handler', methods=['POST'])
def zip_handler():
    rows = connect('SELECT * FROM zip_code WHERE zip = ' + request.form['zip'] + ';')
    heads = ['Zip Code', 'City Name (Municipality)', 'County']
    return render_template('my-result.html', rows=rows, heads=heads)


# Python route for handling VMT Query Range
@app.route('/vmt_data_handler', methods=['POST'])
def vmt_data_handler():
    rows = connect(
        'SELECT vmt_table_temp.mun_name, vmt_table_temp.zip, CAST (AVG(CAST (vmt_total AS integer)) AS integer) vmt_total, contains_2_main.total_personal, contains_2_main.num_evs, ROUND(EV_ratio.percentage, 2) ' + 
        'FROM vmt_table_temp INNER JOIN contains_2_main ' + 
        'ON vmt_table_temp.zip = contains_2_main.zip AND vmt_table_temp.mun_name = contains_2_main.mun_name ' +
        'INNER JOIN EV_ratio ON EV_ratio.zip = vmt_table_temp.zip ' +
        'WHERE vmt_total > ' + request.form['min_vmt']  + ' AND vmt_total < ' + request.form['max_vmt'] + ' ' +
        'GROUP BY (vmt_table_temp.mun_name, vmt_table_temp.zip, contains_2_main.total_personal, contains_2_main.num_evs, EV_ratio.percentage) ' +
        'ORDER BY vmt_total DESC;')
    
    heads = ['Municipality', 'Zip Code', 'VMT-Total', 'Number of Personal Vehicles', '# OF EVs', 'Ratio of EVs %']
    return render_template('my-result.html', rows=rows, heads=heads)

# Python route for handling ev-ratio queries
# @app.route('/ev_ratio-handler', methods=['POST'])
# def ev_ratio_handler():
#     rows = connect('SELECT contains_2_main.mun_name, contains_2_main.zip, EV_ratio.num_evs, EV_ratio.percentage, contains_2_main.total_personal FROM contains_2_main INNER JOIN EV_ratio ON contains_2_main.zip = EV_ratio.zip WHERE contains_2_main.zip = ' + request.form['zip'] + ';')
#     heads = ['Municipality', 'Zip Code', '# Of EVs', 'Ratio of EVs %', 'Number of Personal Vehicles']
#     return render_template('my-result.html', rows=rows, heads=heads)

if __name__ == '__main__':
    app.run(debug = True)
