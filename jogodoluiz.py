import pygame

# Tamanho da tela
width = 100 * 14
height = 76 * 10

# Variáveis do herói
hero_walk = []  # Lista de imagens da animação
hero_anim_frame = 0
hero_pos = [100,225]
hero_pos_x = hero_pos[0]
hero_pos_y = hero_pos[1]
hero_anim_time = 0  # Controle de tempo da animação

# Mapa e dicionário de tiles
mapa = []
tile = {}

# Função para carregar o mapa a partir de um arquivo
def load_mapa(filename):
    global mapa
    with open(filename, "r") as file:
        for line in file:
            mapa.append(line.strip())  # Remove quebras de linha

# Função para carregar imagens e recursos
def load():
    global clock, tile, hero_walk, collider_mapa,collider_mapa1,collider_mapa2,collider_mapa3,collider_mapa4
    clock = pygame.time.Clock()
    load_mapa("mapa.txt")
    
    collider_mapa = pygame.Rect(-110, 0, 80, 900)
    collider_mapa1 = pygame.Rect(0, 955, 1400, 100)
    collider_mapa2 = pygame.Rect(0, -130, 1400, 100)
    collider_mapa4 = pygame.Rect(0, 715, 1400, 90)
    collider_mapa3 = pygame.Rect(1375, 0, 80, 900)
    # Carregar tiles
    tile['G'] = pygame.transform.scale(pygame.image.load("grama.png"), (50, 50))
    tile['P'] = pygame.transform.scale(pygame.image.load("areia.png"), (50, 50))
    tile['A'] = pygame.transform.scale(pygame.image.load("agua.png"), (50, 50))
    
 
    for i in range(1, 17):
        img = pygame.image.load(f"Hero_Walk_{i:02d}.png").convert_alpha()
        img = pygame.transform.scale(img, (80, 80))
        hero_walk.append(img)

# Função de atualização
def update(dt):
    global hero_walk, hero_anim_frame, hero_pos_x, hero_anim_time, hero_pos_y,collider_jogador
    old_x, old_y = hero_pos_x, hero_pos_y
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        hero_pos_x += 0.1 * dt
        hero_anim_time += dt
        if hero_anim_time > 100:
            hero_anim_frame += 1
            if hero_anim_frame > 3:
                hero_anim_frame = 0
            hero_anim_time = 0

    elif keys[pygame.K_LEFT]:
        if hero_anim_frame < 4 or hero_anim_frame > 7:
            hero_anim_frame = 4
        hero_pos_x -= 0.1 * dt
        hero_anim_time += dt
        if hero_anim_time > 100:
            hero_anim_frame += 1
            if hero_anim_frame > 7:
                hero_anim_frame = 4
            hero_anim_time = 0

    elif keys[pygame.K_UP]:
        if hero_anim_frame < 8 or hero_anim_frame > 11:
            hero_anim_frame = 8
        hero_pos_y -= 0.1 * dt
        hero_anim_time += dt
        if hero_anim_time > 100:
            hero_anim_frame += 1
            if hero_anim_frame > 11:
                hero_anim_frame = 8
            hero_anim_time = 0

    elif keys[pygame.K_DOWN]:
        if hero_anim_frame < 12 or hero_anim_frame > 15:
            hero_anim_frame = 12
        hero_pos_y += 0.1 * dt
        hero_anim_time += dt
        if hero_anim_time > 100:
            hero_anim_frame += 1
            if hero_anim_frame > 15:
                hero_anim_frame = 12
            hero_anim_time = 0
    collider_jogador = pygame.Rect(hero_pos_x, hero_pos_y, 32, 32)
    if collider_jogador.colliderect(collider_mapa):
        hero_pos_x = old_x
        hero_pos_y = old_y
    if collider_jogador.colliderect(collider_mapa1):
        hero_pos_x = old_x
        hero_pos_y = old_y
    if collider_jogador.colliderect(collider_mapa2):
        hero_pos_x = old_x
        hero_pos_y = old_y
    if collider_jogador.colliderect(collider_mapa3):
        hero_pos_x = old_x
        hero_pos_y = old_y
    if collider_jogador.colliderect(collider_mapa4):
        hero_pos_x = old_x
        hero_pos_y = old_y


# Função para desenhar o conteúdo na tela
def draw_screen(screen):
    screen.fill((255, 255, 255))
    for i in range(20):  # Linhas
        for j in range(28):  # Colunas
            char = mapa[i][j]
            screen.blit(tile[char], (j * 50, i * 50))
    screen.blit(hero_walk[hero_anim_frame], (hero_pos_x, hero_pos_y))
    pygame.draw.rect(screen, (0, 255, 0), (collider_jogador.x, collider_jogador.y, collider_jogador.width, collider_jogador.height), 2)
    #pygame.draw.rect(screen, (225, 0, 225), (collider_mapa1.x, collider_mapa1.y , collider_mapa1.width, collider_mapa1.height), 5)
    pygame.draw.rect(screen, (225, 0, 225), (collider_mapa.x, collider_mapa.y , collider_mapa.width, collider_mapa.height), 5)
    pygame.draw.rect(screen, (225, 0, 225), (collider_mapa2.x, collider_mapa2.y , collider_mapa2.width, collider_mapa2.height), 5)
    #pygame.draw.rect(screen, (225, 0, 225), (collider_mapa3.x, collider_mapa3.y , collider_mapa3.width, collider_mapa3.height), 5)
    #pygame.draw.rect(screen, (225, 0, 225), (collider_mapa4.x, collider_mapa4.y , collider_mapa4.width, collider_mapa4.height), 5)



# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mapa com Tiles")
    load()

    running = True
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(dt)
        draw_screen(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()