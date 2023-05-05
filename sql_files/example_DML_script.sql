SELECT *
FROM zip_code;

SELECT *
FROM mun2_temp;

SELECT *
FROM ghg_table_temp;

SELECT *
FROM vmt_table_temp;

SELECT *
FROM ev_ratio;

SELECT *
FROM contains_2_main;

SELECT ghg_table_temp.*, contains_2_main.total_personal, contains_2_main.num_evs
FROM ghg_table_temp INNER JOIN contains_2_main
ON ghg_table_temp.zip = contains_2_main.zip AND ghg_table_temp.mun_name = contains_2_main.mun_name
WHERE ghg_total > 40000 AND ghg_total < 70000 AND total_personal > 5000;

SELECT vmt_table_temp.mun_name, vmt_table_temp.zip, CAST (AVG(CAST (vmt_total AS integer)) AS integer) vmt_total, contains_2_main.total_personal, contains_2_main.num_evs
FROM vmt_table_temp INNER JOIN contains_2_main
ON vmt_table_temp.zip = contains_2_main.zip AND vmt_table_temp.mun_name = contains_2_main.mun_name
WHERE vmt_total > 300000000 AND vmt_total < 500000000 AND total_personal > 50000
GROUP BY (vmt_table_temp.mun_name, vmt_table_temp.zip, contains_2_main.total_personal, contains_2_main.num_evs);

SELECT mun_name, zip,SUM(CAST (number_of_EVs AS integer)) num_evs, SUM(total_personal_vehicles) AS total_personal
FROM contains_2_temp
GROUP BY (mun_name, zip);

SELECT contains_2_main.mun_name, contains_2_main.zip, EV_ratio.num_evs, EV_ratio.percentage
FROM contains_2_main INNER JOIN EV_ratio ON contains_2_main.zip = EV_ratio.zip
WHERE contains_2_main.zip = '7731';
