import pygame
import random
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulação de Estrelas Incrível")

clock = pygame.time.Clock()

stars = []
explosions = []

def create_explosion(x, y):
    for _ in range(100):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 8)
        explosions.append({
            'pos': [x, y],
            'vel': [speed * math.cos(angle), speed * math.sin(angle)],
            'color': (random.randint(200, 255), random.randint(100, 200), 255)
        })

def update_explosions():
    for explosion in explosions:
        explosion['pos'][0] += explosion['vel'][0]
        explosion['pos'][1] += explosion['vel'][1]
        explosion['vel'][0] *= 0.98  # Simulando a desaceleração
        explosion['vel'][1] *= 0.98

def draw_explosions():
    for explosion in explosions:
        pygame.draw.circle(screen, explosion['color'], (int(explosion['pos'][0]), int(explosion['pos'][1])), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            create_explosion(*pygame.mouse.get_pos())

    screen.fill((0, 0, 0))

    # Adicionando novas estrelas ao fundo
    for _ in range(5):
        stars.append((random.randint(0, width), random.randint(0, height)))

    # Movendo estrelas em direção ao cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(len(stars)):
        star_x, star_y = stars[i]
        angle = math.atan2(mouse_y - star_y, mouse_x - star_x)
        speed = 5
        stars[i] = (star_x + speed * math.cos(angle), star_y + speed * math.sin(angle))

    # Desenhando estrelas com efeito de trilha
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (int(star[0]), int(star[1])), 2)

    # Atualizando e desenhando explosões
    update_explosions()
    draw_explosions()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
