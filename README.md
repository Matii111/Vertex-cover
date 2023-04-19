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


