# Vertex-cover
Análisis del problema de cobertura de vértices (*Vertex cover*). Para el analisis del problema de cobertura de vertices se presentan tres codigos, almacenados en sus respectivos archivos:

### VertexCover en python
  Contiene una representacion del problema Vertex Cover en grafos, es decir, permite resolver un problmea de minimizacion entregando el conjunto minimo de que cubre con todas las aristas para luego mostrarlo en un grafico junto al conjunto encontrado. El grafico entregado marca con gris los vertices y con gris oscuro aquellos que forman parte del conjunto como se muestra en la ilustracion a continuacion. [vertexCover.py](vertexCover.py).
  
<p align="center">
  <img src="https://user-images.githubusercontent.com/101642846/233218091-939c265c-4b42-4fa1-9d3d-badff5922c9e.png">
</p>

Resultado en consola: 
```
Minimum vertex cover: 
{2,3,5}
```

Para el correcto funcionamiento del codigo son requeridos los siguientes paquetes: 
  
``` 
pip install pulp
pip install networkx
pip install matplotlib
```
### VertexCover en AMPL
Dentro de la carpeta ampl se encuentran tres archivos que forman en su conjunto un programa que resuelve un problema de cobertura de vertices. [ampl](ampl).

Mas especificamente: 
* *vertex.mod* define el modelo matematico 
* *vertex.dat* tiene los datos de ejemplo.
* *vertex.run* es el script que ejecuta el modelo.

Tras ejecutar el codigo deberia entregar una de las varias soluciones optimas al problema, es por esto que puede ser distinta a la proporcionada por python. En consola se mostrara el resultado de la forma:
```
x [*] :=
1  1
2  0
3  1
4  1
5  0
;
```
Donde la columna izquierda "x" representa a cada vertice del grafo, mientras que la columna derecha "[*]" muestra valores booleanos para verificar si un vertice forma parte de la solucion o no. Para este caso la cobertura minima optima que ha encontrado esta compuesta por los vertices {1,3,4}.
### VertexCover en Mathlab
De la misma manera que los codigos anteriores, el codigo desarrollado en *Mathlab* plantea un grafo G con sus respectivos vertices y aristas, para ser luego graficado. Si bien la grafica a continuacion es acorde a lo esperado, no son asi los resultados, requiere un repaso. [vertexCover.m](vertexCover.m).
<p align="center">
  <img src="https://github.com/Matii111/Vertex-cover/blob/master/imgs/mathWorks.png">
</p>
