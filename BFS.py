from collections import deque

# Función para verificar si la posición es correcta
def verificar_posicion(posicion, tolerancia, posicion_esperada):
    x_correcto = posicion_esperada[0] - tolerancia <= posicion[0] <= posicion_esperada[0] + tolerancia
    y_correcto = posicion_esperada[1] - tolerancia <= posicion[1] <= posicion_esperada[1] + tolerancia
    return x_correcto and y_correcto

# Función BFS para buscar la posición correcta
def buscar_posicion_correcta_bfs(posicion_inicial, tolerancia, posicion_esperada):
    cola = deque([posicion_inicial])
    visitados = set()

    while cola:
        x, y, z = cola.popleft()  # Consideramos también la rotación sobre el eje Z
        if verificar_posicion((x, y), tolerancia, posicion_esperada):
            return (x, y, z)  # Posición correcta encontrada

        # Agregar posiciones adyacentes a la cola
        for dx in [-tolerancia, 0, tolerancia]:
            for dy in [-tolerancia, 0, tolerancia]:
                for dz in [-tolerancia, 0, tolerancia]:  # Incluimos variaciones en Z
                    nueva_posicion = (x + dx, y + dy, z + dz)
                    if nueva_posicion not in visitados:
                        cola.append(nueva_posicion)
                        visitados.add(nueva_posicion)

    return None  # No se encontró la posición correcta

# Ejemplo de uso de la función
posicion_inicial = (0, 0, 0)  # Incluimos la coordenada Z
tolerancia = 0.5  # Tolerancia ajustada para mayor precisión
posicion_esperada = (10, 5, 0)  # Posición esperada con coordenada Z

posicion_correcta = buscar_posicion_correcta_bfs(posicion_inicial, tolerancia, posicion_esperada)
if posicion_correcta:
    print(f"La posición correcta del block es: {posicion_correcta}")
else:
    print("No se encontró la posición correcta dentro de la tolerancia dada.")