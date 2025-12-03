CREATE DATABASE inmobiliario;
USE inmobiliario;

show tables;
select * from comuna;

CREATE TABLE comuna (
    id_comuna INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(5) UNIQUE,
    nombre VARCHAR(150)
);

UPDATE comuna SET nombre = 'Quinta Normal'             WHERE codigo = 'QUI';
UPDATE comuna SET nombre = 'Pedro Aguirre Cerda'       WHERE codigo = 'PED';
UPDATE comuna SET nombre = 'Estación Central'          WHERE codigo = 'EST';
UPDATE comuna SET nombre = 'Colina'                    WHERE codigo = 'COL';
UPDATE comuna SET nombre = 'La Florida'                WHERE codigo = 'LAF';
UPDATE comuna SET nombre = 'Maipú'                     WHERE codigo = 'MAI';
UPDATE comuna SET nombre = 'Santiago'                  WHERE codigo = 'SAN';
UPDATE comuna SET nombre = 'Puente Alto'               WHERE codigo = 'PUE';
UPDATE comuna SET nombre = 'Las Condes'                WHERE codigo = 'LAS';
UPDATE comuna SET nombre = 'Lampa'                     WHERE codigo = 'LAM';
UPDATE comuna SET nombre = 'La Pintana'                WHERE codigo = 'LAP';
UPDATE comuna SET nombre = 'Renca'                     WHERE codigo = 'REN';
UPDATE comuna SET nombre = 'Huechuraba'                WHERE codigo = 'HUE';
UPDATE comuna SET nombre = 'Ñuñoa'                     WHERE codigo = 'ÑUÑ';
UPDATE comuna SET nombre = 'La Granja'                 WHERE codigo = 'LAG';
UPDATE comuna SET nombre = 'Pudahuel'                  WHERE codigo = 'PUD';
UPDATE comuna SET nombre = 'Independencia'             WHERE codigo = 'IND';
UPDATE comuna SET nombre = 'Buín'                      WHERE codigo = 'BUI';
UPDATE comuna SET nombre = 'Peñalolén'                 WHERE codigo = 'PEÑ';
UPDATE comuna SET nombre = 'Talagante'                 WHERE codigo = 'TAL';
UPDATE comuna SET nombre = 'Padre Hurtado'             WHERE codigo = 'PAD';
UPDATE comuna SET nombre = 'Tiltil'                    WHERE codigo = 'TIL';
UPDATE comuna SET nombre = 'Lo Barnechea'              WHERE codigo = 'LOB';
UPDATE comuna SET nombre = 'Conchalí'                  WHERE codigo = 'CON';
UPDATE comuna SET nombre = 'Providencia'               WHERE codigo = 'PRO';
UPDATE comuna SET nombre = 'La Reina'                  WHERE codigo = 'LAR';
UPDATE comuna SET nombre = 'Recoleta'                  WHERE codigo = 'REC';
UPDATE comuna SET nombre = 'El Monte'                  WHERE codigo = 'ELM';
UPDATE comuna SET nombre = 'Macul'                     WHERE codigo = 'MAC';
UPDATE comuna SET nombre = 'Calera de Tango'           WHERE codigo = 'CAL';
UPDATE comuna SET nombre = 'Paine'                     WHERE codigo = 'PAI';
UPDATE comuna SET nombre = 'La Cisterna'               WHERE codigo = 'LAC';
UPDATE comuna SET nombre = 'Melipilla'                 WHERE codigo = 'MEL';
UPDATE comuna SET nombre = 'El Bosque'                 WHERE codigo = 'ELB';
UPDATE comuna SET nombre = 'Lo Prado'                  WHERE codigo = 'LOP';
UPDATE comuna SET nombre = 'Vitacura'                  WHERE codigo = 'VIT';
UPDATE comuna SET nombre = 'Lo Espejo'                 WHERE codigo = 'LOE';
UPDATE comuna SET nombre = 'Cerrillos'                 WHERE codigo = 'CER';
UPDATE comuna SET nombre = 'Curacaví'                  WHERE codigo = 'CUR';
UPDATE comuna SET nombre = 'Pirque'                    WHERE codigo = 'PIR';
UPDATE comuna SET nombre = 'Isla de Maipo'             WHERE codigo = 'ISL';
UPDATE comuna SET nombre = 'María Pinto'               WHERE codigo = 'MAR';

