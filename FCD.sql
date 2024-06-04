rutas
CREATE TABLE IF NOT EXISTS rutas (
	id  	INTEGER PRIMARY KEY,
	nombre  VARCHAR(40) UNIQUE,
	dificul VARCHAR(15),
	km      REAL,
	desnive VARCHAR(6)
);