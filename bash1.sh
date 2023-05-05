#! /bin/bash

dropdb CAB_database
createdb CAB_database

python python_scripts/create_ev_ownership_data.py
python python_scripts/create_ghg_data.py
python python_scripts/create_vmt_data.py
python python_scripts/create_zipcode_data.py

psql -U lion -d CAB_database -c "\i sql_files/mun_DDL_script.sql"
psql -U lion -d CAB_database -c "\i sql_files/contains_DDL_script.sql"
psql -U lion -d CAB_database -c "\i sql_files/vehicle_DDL_script.sql"
psql -U lion -d CAB_database -c "\i sql_files/example_DML_script.sql" << EOF
       <q>
EOF

export FLASK_APP=app.py
xdg-open http://127.0.0.1:5000
flask run
