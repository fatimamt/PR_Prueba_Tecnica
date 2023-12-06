LOAD DATA LOCAL INFILE '{{ params.filepath }}'

{ % if 'MATRIZ' in params.check_name %}
INTO TABLE MATRIZ_RELACIONES
{ % else %}
INTO TABLE LISTA_ACTORES
{% endif %}

FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;