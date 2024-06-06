import pygame

pygame.init()

SCREEN_WIDTH = 150
SCREEN_HEIGH = 150

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
pygame.display.set_caption("TicTacToe")

BLACK = (0,0,0)

class Block(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def change_image(self, new_image_path):
        self.image = pygame.image.load(new_image_path)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def get_position(self):
        return self.rect.topleft


blank_image_path = 'blank.png'
cross_image_path = 'cross.png'
circle_image_path = 'circle.png'

pygame.font.init()
font = pygame.font.Font(None, 24)
win_text = ''

pygame.mixer.music.load('Tequila.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

click = pygame.mixer.Sound('click.wav')
click.set_volume(0.8)

block1 = Block(blank_image_path, (0,0))
block2 = Block(blank_image_path, (50,0))
block3 = Block(blank_image_path, (100,0))
block4 = Block(blank_image_path, (0,50))
block5 = Block(blank_image_path, (50,50))
block6 = Block(blank_image_path, (100,50))
block7 = Block(blank_image_path, (0,100))
block8 = Block(blank_image_path, (50,100))
block9 = Block(blank_image_path, (100,100))

end = Block(blank_image_path, (0,0))

all_sprites = pygame.sprite.Group(
    block1, block2, block3, block4, block5, block6, block7, block8, block9
)

run = True
game_over = False

game_turn = 1

blockStatus1 = blockStatus2 = blockStatus3 = blockStatus4 = blockStatus5 = blockStatus6 = blockStatus7 = blockStatus8 = blockStatus9 = 0

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            click.play()
            if block1.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus1 == 0:
                block1.change_image(cross_image_path)
                game_turn += 1
                blockStatus1 = 1
            elif block1.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus1 == 0:
                block1.change_image(circle_image_path)
                game_turn += 1
                blockStatus1 = 2

            elif block2.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus2 == 0:
                block2.change_image(cross_image_path)
                game_turn += 1
                blockStatus2 = 1
            elif block2.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus2 == 0:
                block2.change_image(circle_image_path)
                game_turn += 1
                blockStatus2 = 2

            elif block3.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus3 == 0:
                block3.change_image(cross_image_path)
                game_turn += 1
                blockStatus3 = 1
            elif block3.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus3 == 0:
                block3.change_image(circle_image_path)
                game_turn += 1
                blockStatus3 = 2
          
            elif block4.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus4 == 0:
                block4.change_image(cross_image_path)
                game_turn += 1
                blockStatus4 = 1
            elif block4.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus4 == 0:
                block4.change_image(circle_image_path)
                game_turn += 1
                blockStatus4 = 2

            elif block5.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus5 == 0:
                block5.change_image(cross_image_path)
                game_turn += 1
                blockStatus5 = 1
            elif block5.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus5 == 0:
                block5.change_image(circle_image_path)
                game_turn += 1
                blockStatus5 = 2

            elif block6.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus6 == 0:
                block6.change_image(cross_image_path)
                game_turn += 1
                blockStatus6 = 1
            elif block6.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus6 == 0:
                block6.change_image(circle_image_path)
                game_turn += 1
                blockStatus6 = 2
          
            elif block7.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus7 == 0:
                block7.change_image(cross_image_path)
                game_turn += 1
                blockStatus7 = 1
            elif block7.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus7 == 0:
                block7.change_image(circle_image_path)
                game_turn += 1
                blockStatus7 = 2

            elif block8.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus8 == 0:
                block8.change_image(cross_image_path)
                game_turn += 1
                blockStatus8 = 1
            elif block8.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus8 == 0:
                block8.change_image(circle_image_path)
                game_turn += 1
                blockStatus8 = 2

            elif block9.rect.collidepoint(mouse_pos) and game_turn%2 == 1 and blockStatus9 == 0:
                block9.change_image(cross_image_path)
                game_turn += 1
                blockStatus9 = 1
            elif block9.rect.collidepoint(mouse_pos) and game_turn%2 == 0 and blockStatus9 == 0:
                block9.change_image(circle_image_path)
                game_turn += 1
                blockStatus9 = 2

            

    if blockStatus1 == blockStatus2 == blockStatus3 != 0:
        if blockStatus1 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus1 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus4 == blockStatus5 == blockStatus6 != 0:
        if blockStatus4 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus4 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus7 == blockStatus8 == blockStatus9 != 0:
        if blockStatus7 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus7 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus1 == blockStatus4 == blockStatus7 != 0:
        if blockStatus1 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus1 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus2 == blockStatus5 == blockStatus8 != 0:
        if blockStatus2 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus2 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus3 == blockStatus6 == blockStatus9 != 0:
        if blockStatus3 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus3 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus1 == blockStatus5 == blockStatus9 != 0:
        if blockStatus1 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus1 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus3 == blockStatus5 == blockStatus7 != 0:
        if blockStatus3 == 1:
            win_text = "Cross wins"
            game_over = True
        elif blockStatus3 == 2:
            win_text = "Circle wins"
            game_over = True

    elif blockStatus1 and blockStatus2 and blockStatus3 and blockStatus4 and blockStatus5 and blockStatus6 and blockStatus7 and blockStatus8 and blockStatus9 != 0:
        win_text = "Draw"
        game_over = True

    screen.fill((BLACK))

    all_sprites.draw(screen)

    if game_over:
        text_surface = font.render(win_text, True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_HEIGH // 2, SCREEN_WIDTH // 2))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()