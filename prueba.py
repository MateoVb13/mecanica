import pygame
import sys
import math

# Clase para el jugador
# Clase para el jugador
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 50
        self.longitud_y = 300

    def dibujar(self, pantalla, angulo):
        # Dibujar la parte inferior del palo
        pygame.draw.line(pantalla, (139, 69, 19), (self.x, self.y), (self.x, self.y - self.longitud_y // 2), 20)
        # Dibujar la cuerda y la bola aquí
        cuerda_x = self.x
        cuerda_y = self.y - self.longitud_y // 2
        pygame.draw.line(pantalla, (0, 0, 0), (cuerda_x, cuerda_y), (bola.x, bola.y), 5)
        bola.dibujar(pantalla)
        # Dibujar la parte superior del palo
        pygame.draw.line(pantalla, (139, 69, 19), (self.x, self.y + self.longitud_y // 2), (self.x, self.y), 20)


# Clase para la bola
class Bola:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 20
        self.angulo = 0
        self.velocidad_inicial = 0
        self.aceleracion = 0.000021
        self.velocidad_actual = 0
        self.imagen = pygame.image.load("C:/Users/mateo/Downloads/proyecto mecanic/imagenes/pelotatetherball.png")  # Nueva imagen de la pelota
        self.imagen = pygame.transform.scale(self.imagen, (self.radio * 2, self.radio * 2))  # Escalar la imagen

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x - self.radio, self.y - self.radio))

    def mover(self, dt):
        self.velocidad_actual += self.aceleracion * dt
        self.angulo += self.velocidad_actual
        self.x = palo.x + int(palo.radio * math.cos(self.angulo))
        self.y = palo.y + int(palo.radio * math.sin(self.angulo))
        
        

    def obtener_velocidad_kmh(self):
        # Convertir la velocidad de píxeles por milisegundo a kilómetros por hora
        velocidad_km_h = self.velocidad_actual * 100 * (3600 / (2 * math.pi * 1000))
        return velocidad_km_h

# Inicialización de Pygame
pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Tetherball")

# Fuente para el texto
fuente = pygame.font.Font(None, 36)

# Crear objetos de jugador y bola
palo = Jugador(ancho // 2, alto // 2)
bola = Bola(palo.x + 100, palo.y)

# Estado del juego
esperando_inicio = True

# Bucle principal
reloj = pygame.time.Clock()
tiempo_anterior = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos
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
        tiempo_actual = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos
        dt = tiempo_actual - tiempo_anterior  # Calcular el tiempo transcurrido desde la última actualización
        tiempo_anterior = tiempo_actual  # Actualizar el tiempo anterior
        bola.mover(dt)

    palo.dibujar(pantalla, bola.angulo)
    bola.dibujar(pantalla)

    # Mostrar la velocidad actual en pantalla
    velocidad_kmh = bola.obtener_velocidad_kmh()
    texto_velocidad = fuente.render("Velocidad Actual: {:.2f} km/h".format(velocidad_kmh), True, (0, 0, 0))
    pantalla.blit(texto_velocidad, (10, 10))

    pygame.display.flip()
    reloj.tick(60)