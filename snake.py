import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dimensões da tela
largura_tela = 800
altura_tela = 600

# Tamanho da cobrinha e da maçã
tamanho = 20

# Velocidade da cobrinha
velocidade = 15

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobrinha")

# Função para desenhar a cobrinha
def desenhar_cobrinha(cobrinha):
    for posicao in cobrinha:
        pygame.draw.rect(tela, GREEN, [posicao[0], posicao[1], tamanho, tamanho])

# Função principal do jogo
def jogo():
    fim_jogo = False
    fim = False

    # Posição inicial da cobrinha
    posicao_x = largura_tela / 2
    posicao_y = altura_tela / 2

    # Mudança inicial de posição da cobrinha
    mudanca_x = 0
    mudanca_y = 0

    # Lista da cobrinha
    cobrinha = []
    comprimento = 1

    # Posição inicial da ponto
    ponto_x = round(random.randrange(0, largura_tela - tamanho) / 20) * 20
    ponto_y = round(random.randrange(0, altura_tela - tamanho) / 20) * 20

    while not fim_jogo:
        while fim:
            tela.fill(WHITE)
            fonte = pygame.font.SysFont(None, 50)
            texto = fonte.render("Game Over! C continuar. S sair.", True, RED)
            pos_texto = texto.get_rect(center=(largura_tela / 2, altura_tela / 2))
            tela.blit(texto, pos_texto)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        fim_jogo = True
                        fim = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mudanca_x = -tamanho
                    mudanca_y = 0
                elif event.key == pygame.K_RIGHT:
                    mudanca_x = tamanho
                    mudanca_y = 0
                elif event.key == pygame.K_UP:
                    mudanca_y = -tamanho
                    mudanca_x = 0
                elif event.key == pygame.K_DOWN:
                    mudanca_y = tamanho
                    mudanca_x = 0

        if posicao_x >= largura_tela or posicao_x < 0 or posicao_y >= altura_tela or posicao_y < 0:
            fim = True

        posicao_x += mudanca_x
        posicao_y += mudanca_y
        tela.fill(WHITE)
        pygame.draw.rect(tela, RED, [ponto_x, ponto_y, tamanho, tamanho])
        cobrinha_cabeca = []
        cobrinha_cabeca.append(posicao_x)
        cobrinha_cabeca.append(posicao_y)
        cobrinha.append(cobrinha_cabeca)
        if len(cobrinha) > comprimento:
            del cobrinha[0]

        for segmento in cobrinha[:-1]:
            if segmento == cobrinha_cabeca:
                fim = True

        desenhar_cobrinha(cobrinha)

        pygame.display.update()

        if posicao_x == ponto_x and posicao_y == ponto_y:
            ponto_x = round(random.randrange(0, largura_tela - tamanho) / 20) * 20
            ponto_y = round(random.randrange(0, altura_tela - tamanho) / 20) * 20
            comprimento += 1

        pygame.time.Clock().tick(velocidade)

    pygame.quit()


jogo()
