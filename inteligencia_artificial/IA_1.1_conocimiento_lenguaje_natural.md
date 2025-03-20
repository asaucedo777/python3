# REPRESENTACIÓN DEL CONOCIMIENTO

1. Representación del conocimiento
- Lenguaje natural y representación simbólica
- Lenguaje matemático
- Diagramas
- Gráficos
- Tablas y bases de datos
- Imágenes, videos y audios


## 1. Lenguaje natural y representación simbólica.

El **lenguaje natural** es el sistema que utilizamos los seres humanos para comunicarnos. 

El lenguaje natural tiene carácterísticas que lo hacen idóneo para cumplir dicha función:
- Ambigüedad: Una misma palabra o representación (e. chino o japonés) puede tener **múltiples significados**
- Flexibilidad: Existen infinitas formas de expresar la misma idea o información
- Contexto-dependiente: La ambigüedad puede resolverse a través del contexto en el que se utiliza
- Evolución: El lenguaje natural evoluciona, incorporando nuevas palabras o dando nuevos significados a palabras existentes.

La representación simbólica es un sistema **normalizado** que utiliza símbolos y reglas precisas para expresar conocimiento.

Las características del lenguaje simbólico permiten su uso en matemáticas, lógica, programación y ciencias formales:
- **Precisión**: Cada símbolo o secuencia de símbolos tienen un único significado
- Estructura formal: Tiene reglas estrictas de sintáxis y semántica
- Independencia del contexto: El significado de los símbolos no depende del contexto
- Abstracción: Los símbolos representa conceptos abstractos complejos de manera simplificada


### Relación entre lenguaje natural y representación simbólica
Ambos sistemas están relacionados, pero sirven para propósitos diferentes:
1. Traducción entre ambos:
El lenguaje natural puede traducirse a representación simbólica, eliminando ambigüedades y facilitando el análisis formal
2. Complementariedad:
El lenguaje natural es más adecuado para la comunicación humana, aunque en determinados contextos se usa el lenguaje simbólico para contextos técnicos o científicos.
3. Aplicaciones:
En IA se utilizan modelos para convertir lenguaje natural en representaciones simbólicas (por ejemplo en procesamiento de lenguaje natural NLP)
En programación, los algoritmos se expresan en lenguajes formales, pero los comentarios en lenguaje natural

### Procesamiento del lenguaje natural
El procesamiento del lenguaje natural consiste utilizar técnicas que permitan representar el lenguaje natural de forma simbólica y de esta forma construir algoritmos que puedan tratar esa representación dando resultados similares ante problemas o preguntas de naturaleza similar.
Ej. La frase "El gato come pescado" puede representarse simbólicamente de diferentes formas. Si queremos construir un sistema que conteste a preguntar relacionadas con la alimentación animal, dicho sistema utilizará dicho conocimiento en forma simbólica para elaborar las respuestas.


Algunos de los métodos utilizados para representar simbólicamente el lenguaje son:
- Análisis sintáctico: estructura gramatical de la oración (sujeto, verbo, ...)
- Análisis semántico: significado de la oración
- Lógica proposicional: proposiciones lógicas 
- Lógica de primer order: representa relaciones y las cuantifica

Ejemplo: Supongamos la frase: "El gato come pescado". ¿Cuál es el resultado de cada uno de los métodos de representación enunciados?
- Análisis Sintáctico   = Sujeto="El gato", Verbo="come", Objeto="pescado"
- Análisis Semántico    = Comer(Gato, Pescado)
- Lógica proposicional  = P -> Q, donde P es "El gato" y Q es "come pescado"
- Lógica 1º orden       = ∀x("Gato"(x) → "ComedoresDePescado"(x)).

El resultado de la representación puede dar lugar a las siguientes representaciones:
- Ontologías: Expresan conceptos y relaciones en un dominio específico
- Grafos: Representan información en forma de nodos (entidades) y aristas (relaciones)

Algunas de las técnicas computacionales utilizadas en NLP:
- Tokenización: dividir el texto en unidades individuales (palabras)
["El", "gato", "come", "pescado"],
- Etiquetado de partes del discurso (POS tagging): 
["Determinante", "Sustantivo", "Verbo", "Sustantivo"]
- Extracción de relaciones: identifica relaciones entre entidades
Comer(Gato, Pescado)

