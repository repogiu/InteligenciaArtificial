# Inteligencia Artificial - Ejemplos de Algoritmos

Este repositorio recopila ejemplos sencillos de algoritmos y técnicas relacionadas con la inteligencia artificial y la visión por computadora.

## Contenido

- **BFS.py**: Implementación de una búsqueda en anchura (Breadth-First Search) para encontrar una posición objetivo considerando tolerancias en los ejes X, Y y Z.
- **Hough_linea.py**: Script que aplica la transformada de Hough para detectar líneas en la imagen `linea.png` utilizando OpenCV y Matplotlib para la visualización.
- **Hough_circunferencia.py**: Ejemplo de detección de circunferencias en la imagen `circulo.png` a través de la transformada de Hough circular.
- **circulo.png** y **linea.png**: Imágenes de ejemplo utilizadas por los scripts de detección.

## Requisitos

Para ejecutar los scripts que dependen de OpenCV y Matplotlib, instala las dependencias con:

```bash
pip install opencv-python matplotlib numpy
```

## Uso

1. Asegúrate de tener las imágenes de ejemplo en el mismo directorio que los scripts.
2. Ejecuta el script correspondiente según el algoritmo que desees probar, por ejemplo:

```bash
python Hough_linea.py
```

3. Sigue las instrucciones y observa las visualizaciones generadas por cada script.

Estos ejemplos están pensados como punto de partida para experimentar con conceptos básicos de visión por computadora y búsqueda en grafos.
