import pygame

print("inicio")
pygame.init()
janela = pygame.display.set_mode((800, 600))
print("ligado")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("desliga")