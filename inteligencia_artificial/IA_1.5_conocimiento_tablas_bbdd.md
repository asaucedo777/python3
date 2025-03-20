# REPRESENTACIÓN DEL CONOCIMIENTO

5. TABLAS Y BASES DE DATOS
- Datos tabulados
- Tipos de bases de datos


## 5. TABLAS Y BASES DE DATOS
Las bases de datos son herramientas que permiten organizar, almacenar y gestionar la información de manera eficiente desde el punto de vista de los recursos utiizados y la disponibilidad de la informacion para su tratamiento.

### Tipos de bases de datos
Se clasifican en función de la forma en la que están organizados los datos en la base de datos:
- SQL o bases de datos relacionales: los datos están organizados en tablas. Estas tablas están relacionadas de forma lógica y también pueden estarlo en forma de claves primarias y foráneas.
- NoSQL: los datos están organizados en formatos más flexibles (documentos, grafos o pares clave-valor)

### Estructura física de una base de datos
Existen unos principios generales de almacenamiento de los datos en una base de datos, entre los que destacan los siguientes:
- Archivos de datos: los archivos de datos, son archivos binarios en disco en los que cada archivo contiene "páginas" o "bloques", que son la unidad mínima de almacenamiento.
- Páginas: Cada página contiene registros de una tabla, metadatos y punteros
- Extent: Son conjuntos de páginas contiguas
- Segmentos: Son colecciones de extents que pertenece a una tabla

### Caso concreto postgresql
Cada base de datos, tabla, índice u objeto tiene un archivo de datos en PGDATA.
Los archivos de datos se almacen con el nombre del OID del objeto y éstos se dividen en archivos de un máximo de 1GB.
Cada archivo contiene páginas de 8KB por defecto, que incluyen: encabezado, datos y espacio libre.
