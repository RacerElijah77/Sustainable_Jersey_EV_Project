CREATE TABLE contains_2_temp AS
SELECT mun2_temp.mun_name, mun2_temp.zip, ev_ownership_table.number_of_EVs, ev_ownership_table.total_personal_vehicles
FROM mun2_temp INNER JOIN ev_ownership_table ON
UPPER(mun2_temp.mun_name) = UPPER(ev_ownership_table.municipality)
ORDER BY mun_name;

CREATE TABLE contains_2_main AS
SELECT mun_name, zip,SUM(CAST (number_of_EVs AS integer)) num_evs, SUM(total_personal_vehicles) AS total_personal
FROM contains_2_temp
GROUP BY (mun_name, zip);

ALTER TABLE contains_2_main ADD COLUMN vehicle_id SERIAL PRIMARY KEY;

CREATE TABLE EV_RATIO AS
SELECT zip, total_personal, num_evs, CAST(num_evs AS decimal)/CAST(total_personal AS decimal) * 100 as percentage
FROM contains_2_main
ORDER BY total_personal;
