import pygame
from sys import exit

pygame.init()

windowSize = w, h = 800, 400

screen = pygame.display.set_mode((windowSize))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

test_font = pygame.font.Font('C:\\Users\\willcj2\\Documents\\VSCode\\Python\\PygameStuff\\Assets\\Font\\Jersey25-Regular.ttf', 122)


# CALLS AND SETS PARAMS FOR SKY TEXTURE
backGround = pygame.image.load('C:\\Users\\willcj2\\Documents\\VSCode\\Python\\PygameStuff\\Assets\\Sky.png').convert()
BACKGROUND_IMAGE_SIZE = (800, 400)
BACKGROUND_IMAGE_POSITION = (0, 0)
backGround = pygame.transform.scale(backGround, BACKGROUND_IMAGE_SIZE)

# CALLS AND SETS PARAMS FOR GROUND TEXTURE
groundTexture = pygame.image.load('C:\\Users\\willcj2\\Documents\\VSCode\\Python\\PygameStuff\\Assets\\Ground.png').convert()
GROUND_IMAGE_SIZE = (800, 100)
GROUND_IMAGE_POSITION = (0, 300) # When using '[1]' later in the code, this is a reference to the 'y' value.
groundTexture = pygame.transform.scale(groundTexture, GROUND_IMAGE_SIZE)

# CREATES TEXT VARIABLES
textSurface = test_font.render('My Game', False, 'Black')

# CREATES SNAIL ENEMIES
snail_x_pos = 600
SNAIL_SPEED = 4
snailSurface = pygame.image.load('C:\\Users\\willcj2\\Documents\\VSCode\\Python\\PygameStuff\\Assets\\snail\\snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(midbottom = [snail_x_pos, GROUND_IMAGE_POSITION[1]])

# CREATES PLAYER
player_x_pos = 80
playerSurface = pygame.image.load('C:\\Users\\willcj2\\Documents\\VSCode\\Python\\PygameStuff\\Assets\\Player\\player_walk_1.png').convert_alpha()
playerRect = playerSurface.get_rect(midbottom = [player_x_pos, GROUND_IMAGE_POSITION[1]])

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if playerRect.collidepoint(event.pos):
        #         print("Collision")
    
    # DRAWS THE BACKGROUND PNG
    screen.blit(backGround, BACKGROUND_IMAGE_POSITION)
    
    # DRAWS THE GROUND PNG
    screen.blit(groundTexture, GROUND_IMAGE_POSITION)
    
    # DRAWS THE TEXT ON SCREEN
    screen.blit(textSurface, (200, 50))
    
    # DRAWS THE PLAYER ON SCREEN
    screen.blit(playerSurface, playerRect)
    
    
    
    # DRAWS THE SNAIL ON SCREEN
    snailRect.x -= SNAIL_SPEED # Moves the snail LEFT
    screen.blit(snailSurface, snailRect)
    if snailRect.right <= 0:
        snailRect.left = 800
    
    # if playerRect.colliderect(snailRect):
    #     print("Collision")
    
    # mouse_pos = pygame.mouse.get_pos()
    # if playerRect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
    
    
    pygame.display.update()
    clock.tick(60)