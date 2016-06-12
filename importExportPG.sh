psql -c "CREATE TABLE "communesCN"( communes character varying(255),  constats integer,  dept character varying(3));"
psql -c "SET client_encoding TO 'UTF-8'; COPY communesCN FROM STDIN WITH CSV HEADER DELIMITER ','" <ComCN_exportPG.csv
psql -c "COPY (select * from communescn_insee) TO STDOUT DELIMITER ',' CSV HEADER;" > communescn_insee.csv



