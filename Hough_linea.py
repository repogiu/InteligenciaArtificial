
import cv2 # pip install opencv-python
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
image = cv2.imread('linea.png', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro de Canny para la detección de bordes
edges = cv2.Canny(image, 50, 150, apertureSize=3)

# Aplicar la Transformada de Hough para detectar líneas
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Crear una copia de la imagen original para dibujar las líneas detectadas
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Dibujar las líneas detectadas

if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)


# Mostrar la imagen original, los bordes y la imagen con las líneas detectadas
plt.figure(figsize=(20,10))
plt.subplot(131), plt.imshow(image, cmap='gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(edges, cmap='gray')
plt.title('Bordes Detectados'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(output_image)
plt.title('Líneas Detectadas'), plt.xticks([]), plt.yticks([])
plt.show()
