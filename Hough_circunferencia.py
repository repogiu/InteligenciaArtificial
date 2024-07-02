import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread("circulo.png")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar el algoritmo de detección de bordes de Canny
edges = cv2.Canny(gray, 50, 150)

# Detectar círculos usando la Transformada de Hough
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 4, param1=200, param2=10, minRadius=15, maxRadius=80)

# Verificar si se detectaron círculos
if circles is not None:
    circles = np.uint16(np.around(circles))  # Redondear los valores de los círculos

    for i in circles[0, :]:  # Iterar a través de los círculos detectados
        # Dibujar los círculos detectados en la imagen original
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 4)

# Mostrar la imagen original
cv2.imshow("Imagen Original", img)
cv2.waitKey(0)

# Mostrar los bordes detectados
cv2.imshow("Bordes Detectados", edges)
cv2.waitKey(0)

# Mostrar las líneas detectadas
cv2.imshow("Líneas Detectadas", img)
cv2.waitKey(0)

# Cerrar todas las ventanas
cv2.destroyAllWindows()

