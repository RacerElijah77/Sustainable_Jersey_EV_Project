CREATE VIEW get_vehicle_type AS
SELECT mun_name, county, unnest(array['combo_long_haul', 'combo_short_haul', 'intercity_bus', 'light_com_truck', 'passenger_cars', 'passenger_trucks', 'refuse_truck', 'school_bus', 'single_long_haul', 'single_short_haul', 'transit_bus']) AS vehicle_type, unnest(array[combo_long_haul, combo_short_haul, intercity_bus, light_com_truck, passenger_cars, passenger_trucks, refuse_truck, school_bus, single_long_haul, single_short_haul, transit_bus]) AS quantity FROM vmt_data_table;

CREATE VIEW get_zip AS
SELECT get_vehicle_type.mun_name, zip_code_table.zip, get_vehicle_type.vehicle_type
FROM get_vehicle_type INNER JOIN zip_code_table ON UPPER(get_vehicle_type.mun_name) = zip_code_table.city AND UPPER(get_vehicle_type.county) = zip_code_table.county_name;

CREATE TABLE VEHICLE AS SELECT * FROM get_zip;

ALTER TABLE VEHICLE ADD COLUMN vehicle_id SERIAL PRIMARY KEY;
