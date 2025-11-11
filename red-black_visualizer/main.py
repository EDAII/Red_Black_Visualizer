import pygame
from redblack import RedBlackTree
from draw import draw_node

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Red-Black Tree Visualizer")
clock = pygame.time.Clock()

tree = RedBlackTree()
root = None
input_value = ""

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and input_value != "":
                root = tree.insert(root, int(input_value))
                input_value = ""
            elif event.key == pygame.K_BACKSPACE:
                input_value = input_value[:-1]
            elif event.unicode.isdigit():
                input_value += event.unicode
            elif event.key == pygame.K_r and input_value != "":
                root = tree.delete(root, int(input_value))
                input_value = ""



    draw_node(screen, root, 450, 50, 200)

    font = pygame.font.Font(None, 40)
    txt = font.render("Número: " + input_value, True, (255, 255, 255))
    screen.blit(txt, (20, 550))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
