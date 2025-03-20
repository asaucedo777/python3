# REPRESENTACIÓN DEL CONOCIMIENTO

6. Imágenes, vídeos y audios
- Imágenes
- Vídeos
- Audios

## 6. Imágenes, vídeos y audios

### Imágenes
Las imágenes se guardan digitalmente en archivos con un formato binario (no legible directamente) y organizados con un formato específico con características ideales en función de su uso.

#### Formatos de imagen
Los formatos de imagen se suelen clasificar en formatos rasterizados (mapas de bits) y formatos vectoriales (basados en ecuaciones trigonométricas).

Formatos de mapa de bits:
- JPEG (Join Fotographic Expert Group): Es un formato que permite la compresión de las imágenes (con pérdida de calidad). Es el formato más extendido por su versatilidad y compatibilidad con la mayor parte de dispositivos.
- PNG (Portable Network Graphics): Es un formato comprimido sin pérdida, se almacena toda la información de la imagen original. Además soporta transparencia, ideal para iconos y uso web.
- GIF (Graphic Interchange Format): Permite el almacenamiento en un único archivo de una secuencia de imágenes para su uso como una animación. Utiliza un algoritmo de compresión LZW sin pérdida con una gama limitada de colores (256 colores)
- BMP (Bit Map): Almacena la imagen como un mapa de píxeles donde cada píxel representa un color. Es un archivo con alta compatibilidad y máxima calidad aunque el tamaño de los archivos en muy grande por la falta de compresión.
- TIFF (Tagged Image File Format): Utilizado en fotografía profesional y diseño gráfico, soporta alta calidad y compresión sin pérdida.
- RAW: Formato crudo utilizado en fotografía profesional, que contiene todos los datos capturados por el sensor de la cámara.

Formatos vectoriales:
- SVG (Scalable Vector Graphics): Formato basado en XML para representar imágenes bidimensionales. El archivo contiene la definición matemética de cada una de las formas geométricas que conforman la imagen.
- EPS (Encapsulated PostScript): El archivo puede contener tanto formas geométricas que conforman la imagen como conjuntos de píxeles. Se base en el lenguaje PostScritp que es un lenguage que define la apariencia de documentos impresos.

#### Formatos de video
Los formatos de video más utilizados son:
- MP4 (mpeg-4 parte 14): Es el formato más utilizado por su versatilidad y compatibilidad. Puede contener video, audio, subtítulos e imágenes.
- MOV (formato QuickTime Movie):
- AVI (Audio Video Interleave):
- MKV (Matroska):
- WebM

#### Formatos de audio
El audio se digitaliza a través de un dispositivo que captura las ondas de presión en el aire a señales eléctricas analógicas.
Las fases de digitalizacion del sonido son las siguientes:
- Captura del sonido -> señales eléctricas analógicas
- Muestreo -> se capturan valores a intervalos tiempo regulares (ej. CD de audio captura 44100 muetras por segundo 44,1 kHz)
- Cuantización -> a cada muestra se le asigna un valor numérico con una determinada precisión (ej. CD de audio con resolución de 16 bits permite asignar un valor entre 0 y 2^16 (65536))
- Codificación -> los datos del archivo se codifican de acuerdo a un formato determinado que puede ser sin pérdida (WAV, FLAC) Ó con pérdida (MP3, AAC)
