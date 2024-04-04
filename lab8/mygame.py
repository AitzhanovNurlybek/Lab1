import pygame
clock = pygame.time.Clock()


pygame.init()
pygame.display.set_caption("Nurlybeks game")



screen = pygame.display.set_mode((700,400))
bg = pygame.image.load("background.png")

walk_left = [
    pygame.image.load("player_left/player_left1.png"),
    pygame.image.load("player_left/player_left2.png"),
    pygame.image.load("player_left/player_left3.png"),
    pygame.image.load("player_left/player_left4.png"),
]

walk_right=[
    pygame.image.load("player_right/player_right1.png"),
    pygame.image.load("player_right/player_right2.png"),
    pygame.image.load("player_right/player_right3.png"),
    pygame.image.load("player_right/player_right4.png"),
]


bg_x = 0
player_anim_count = 0

running = True

while running:

    pygame.display.update()

    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x + 700,0))
    screen.blit(walk_right[player_anim_count],(200,227))

    if player_anim_count == 3:
        player_anim_count == 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -700:
        bg_x = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    clock.tick(14)
