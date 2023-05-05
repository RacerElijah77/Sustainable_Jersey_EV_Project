CREATE VIEW ZIP_CODE AS
SELECT zip, city, county_name
FROM zip_code_table;

CREATE VIEW ghg_vmt_merged AS
SELECT vmt_data_table.mun_name, vmt_data_table.county, vmt_data_table.vmt_total, ghg_data_table.ghg_total
FROM ghg_data_table INNER JOIN vmt_data_table ON vmt_data_table.mun_name = ghg_data_table.mun_name AND vmt_data_table.county = ghg_data_table.county;

CREATE VIEW zip_code_merged AS
SELECT ghg_vmt_merged.*, zip_code_table.zip
FROM ghg_vmt_merged INNER JOIN zip_code_table ON
UPPER(ghg_vmt_merged.county) = zip_code_table.county_name AND UPPER(ghg_vmt_merged.mun_name) = zip_code_table.city;

CREATE TABLE mun2_temp AS
SELECT zip_code_merged.mun_name, zip_code_merged.zip, zip_code_merged.county
FROM zip_code_merged;

ALTER TABLE mun2_temp ADD COLUMN mun2_id SERIAL PRIMARY KEY;

DELETE FROM
mun2_temp a
USING mun2_temp b
WHERE a.mun2_id > b.mun2_id
AND a.mun_name = b.mun_name AND a.county = b.county;

CREATE TABLE ghg_table_temp AS
SELECT zip_code_merged.mun_name, zip_code_merged.zip, zip_code_merged.ghg_total
FROM zip_code_merged;

ALTER TABLE ghg_table_temp ADD COLUMN ghg_id SERIAL PRIMARY KEY;

DELETE FROM
ghg_table_temp a
USING ghg_table_temp b
WHERE a.ghg_id > b.ghg_id
AND a.mun_name = b.mun_name AND a.ghg_total = b.ghg_total;

CREATE TABLE vmt_table_temp AS
SELECT zip_code_merged.mun_name, zip_code_merged.zip, zip_code_merged.vmt_total
FROM ZIP_CODE_merged;

ALTER TABLE vmt_table_temp ADD COLUMN vmt_id SERIAL PRIMARY KEY;

DELETE FROM
vmt_table_temp a
USING vmt_table_temp b
WHERE a.vmt_id > b.vmt_id
AND a.mun_name = b.mun_name AND a.vmt_total = b.vmt_total;






