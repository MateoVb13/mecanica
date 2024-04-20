import pygame
import sys
import math

# Clase para el jugador
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 50
        self.longitud_y = 300  # Aumentamos la longitud del palo en Y

    def dibujar(self, pantalla, angulo):
        # Dibujar el palo con mayor longitud en Y
        pygame.draw.line(pantalla, (139, 69, 19), (self.x, self.y + self.longitud_y // 2), (self.x, self.y - self.longitud_y // 2), 20)
        # Calcular las coordenadas de la cuerda
        cuerda_x = self.x
        cuerda_y = self.y - self.longitud_y // 2
        # Dibujar la cuerda desde la punta superior del palo a la pelota
        pygame.draw.line(pantalla, (0, 0, 0), (cuerda_x, cuerda_y), (bola.x, bola.y), 5)

# Clase para la bola
class Bola:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 20
        self.angulo = 0  # Inicializamos el atributo angulo
        self.velocidad_inicial = 0  # Velocidad inicial en m/s
        self.aceleracion = 0.00021  # Ajusta la aceleración según tus necesidades

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, (0, 0, 255), (self.x, self.y), self.radio)

    def mover(self):
        self.velocidad_inicial += self.aceleracion  # Aumentar la velocidad con la aceleración
        self.angulo += self.velocidad_inicial  # Actualizar el ángulo con la velocidad
        # Actualizar la posición de la bola en función del ángulo y la longitud de la cuerda
        self.x = palo.x + int(100 * math.cos(self.angulo))
        self.y = palo.y + int(100 * math.sin(self.angulo))

# Inicialización de Pygame
pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Tetherball")

# Crear objetos de jugador y bola
palo = Jugador(ancho // 2, alto // 2)
bola = Bola(palo.x + 100, palo.y)

# Estado del juego
esperando_inicio = True

# Bucle principal
reloj = pygame.time.Clock()
while True:
    pantalla.fill((255, 255, 255))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                esperando_inicio = False

    if not esperando_inicio:
        # Mover la pelota automáticamente si el juego no está en modo de espera
        bola.mover()

    # Dibujar el jugador y la pelota
    palo.dibujar(pantalla, bola.angulo)
    bola.dibujar(pantalla)

    pygame.display.flip()
    reloj.tick(60)  # Limitar el juego a 60 FPS
