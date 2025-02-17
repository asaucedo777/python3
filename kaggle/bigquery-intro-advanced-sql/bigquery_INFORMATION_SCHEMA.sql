/* Ver las tablas de un conjunto de datos:
 *  
 * DATASET: dialogflowasv:bigquery-public-data._conjunto_
 * 
 * _conjunto_ :
 * 		stackoverflow
 * 		baseball
 * 		... (más en https://console.cloud.google.com/marketplace/browse?filter=solution-type:dataset&project=dialogflowasv)
 * 
 * */

SELECT * FROM `bigquery-public-data.baseball.INFORMATION_SCHEMA.TABLES`;

/* Mostrar conjuntos de datos del proyecto dialogflowasv
 * */
SELECT * FROM `dialogflowasv.INFORMATION_SCHEMA.SCHEMATA`;

/*Ver columnas de una tabla de un dataset
 * */
SELECT * FROM `bigquery-public-data.baseball.INFORMATION_SCHEMA.COLUMNS` WHERE table_name = 'games_wide';


