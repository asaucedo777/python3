# REPRESENTACIÓN DEL CONOCIMIENTO

4. Gráficos
- Definiciones
- Tipos de gráficos

## 4.Gráficos
Un gráfico es un representación visual de un conjunto de datos numéricos. A diferencia de los diagramas, los gráficos requieren de una asignación numérica de los datos.

Los gráficos habitualmente representan la relación de 2 ó más magnitudes (ejs. Recuento de personas con la misma edad y edad, Cantidad de hombres por edade, Cantidad de mujeres por edad y edad)

A continuación y teniendo en cuenta los distintos tipos de gráficos que se pueden obtener con las librerías "seaborn" y "matplotlib" de python, se describen los siguientes tipos de gráficos:

### Datos individuales
- stairs(values): se representa el cada valor como un segmento horizontal de longitud fija a la altura que corresponda y se dibujan las líneas verticales de unión de cada segmento con el siguiente formando una "escalera" que representa la subida o bajada de valor de la variable

### Pairwise data (datos por parejas)
- plot(x, y): muestra los valores de la variable y a lo largo del eje x unidos linealmente
- scatter(x, y): similar al anterior, pero los valores de la variable son puntos, no líneas
- bar(x, height): el eje x se agrupa en intervalos de igual tamaño y se representa una barra vertical en cada intervalo de tamaño proporcional al recuento de valores de y en ese intervalo
- stem(x, height): similar a bar, pero en lugar de barras se utilizan líneas verticales
- fill_between(x, y1, y2): similar a plot, pero con 2 variables. Se destaca el area entre las 2 variables para comprobar su dispersión
- stackplot(x, y): similar a plot, pero la variable y se descompone en varios valores que se "apilan" para comprobar su dispersión

### Distribuciones estadísticas
- hist(x): agrupa los valores de la variable en intervalos y genera una barra de altura proporcional al recuento de valores en ese intervalo.
- boxplot(x): similar al hist pero lo que se representa es el menor valor dentro de ese intervalo, el mayor y un rectángulo con un area proporcional al recuento de valores dentro de ese intervalo.
- errorbar(x, y, yerr, xerr): similar al boxplot, pero lo que se representa en el error mínimo, error máximo y valor.
- violinplot(D): similar al boxplot pero el recuento de valores dentro de cada intervalo es un gráfico simétrico de la distribución de los valores dentro de ese intervalo.
- eventplot(D): similar al boxplot pero los recuentos dentro de cada intervalo se representan como segmentos horizontales.
- hist2d(x, y): permite analizar el grado de dependencia de 2 valores.
- hexbin(x, y, C): similar al anterior pero en lugar de puntos, se utilizan hexágonos con grados de tonalidad para representar la concentración de datos en dichos valores.
- ecdf(x): Muestra la distribución contínua de los valores de la distribución.
- pie(x): Hace un recuento de cada uno de los valores posibles de la variable y los representa como porciones de un círculo de tamaño proporcional al recuento de cada valor. Suele utilizarse con valores de variable NO numéricos.

### Representación matricial
Este tipo de diagramas se utilizan para visualizar variables matriciales
- imshow(Z):
- pcolormesh(X, Y, Z):
- contour(X, Y, Z):
- barbs(X,Y,U,V):
- quiver(X,Y,U,V):
- streamplot(X,Y,U,V):

### Datos en 3 dimensiones
En este tipo de gráficos se utiliza una vista isométria del gráfico para visualizar 3 variables:
- bar3d(x,y,z,dx,dy,dz):
...


