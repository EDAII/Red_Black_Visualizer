import pygame

def draw_node(screen, node, x, y, offset):
    if node:
        color = (255, 0, 0) if node.color else (255, 255, 255)
        pygame.draw.circle(screen, color, (x, y), 20, 2)

        font = pygame.font.Font(None, 30)
        text = font.render(str(node.key), True, (255, 255, 255))
        screen.blit(text, (x - 10, y - 10))

        if node.left:
            pygame.draw.line(screen, (200,200,200), (x, y), (x - offset, y + 80), 2)
            draw_node(screen, node.left, x - offset, y + 80, offset//1.4)

        if node.right:
            pygame.draw.line(screen, (200,200,200), (x, y), (x + offset, y + 80), 2)
            draw_node(screen, node.right, x + offset, y + 80, offset//1.4)
