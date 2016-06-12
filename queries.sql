drop table communesCN_insee;
create table communesCN_insee AS 

select insee.id_code_commune as insee, com.communes, com.constats, com.dept from communesCN com
LEFT JOIN sir_insee_commune insee 
	ON (lower(com.communes) = lower(insee.nccenr) AND com.dept = insee.id_dep)
ORDER BY com.dept

SELECT count(insee) -20 as ctr from communesCN_insee

SELECT dept, count(insee) as ctr, sum(constats) as constats FROM communesCN_insee 
group by dept
Order by ctr DESC