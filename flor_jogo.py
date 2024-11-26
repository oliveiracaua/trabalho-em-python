import pygame
import random

# Inicializando o Pygame
pygame.init()

# Tamanho da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Coletor de Flores")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
rosa = (255, 182, 193)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)

# Definindo a fonte
fonte = pygame.font.SysFont("arial", 40)

# Parâmetros
tamanho_quadrado = 20
velocidade = 15
posicao_inicial = largura / 2, altura / 2
direcao = [0, 0]
flores_coletadas = 0

# Função para desenhar flores
def desenhar_flor(x, y):
    pygame.draw.circle(tela, vermelho, (x, y), 15)  # Petal 1
    pygame.draw.circle(tela, vermelho, (x + 20, y), 15)  # Petal 2
    pygame.draw.circle(tela, vermelho, (x - 20, y), 15)  # Petal 3
    pygame.draw.circle(tela, vermelho, (x, y + 20), 15)  # Petal 4
    pygame.draw.circle(tela, verde, (x, y), 10)  # Centro da flor

# Função para exibir a quantidade de flores coletadas
def mostrar_mensagem():
    mensagem = fonte.render(f"Flores Coletadas: {flores_coletadas}", True, rosa)
    tela.blit(mensagem, [largura / 4, altura / 8])

# Função para gerar uma nova flor em uma posição aleatória
def gerar_flor():
    flor_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    flor_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return flor_x, flor_y

# Função principal do jogo
def rodar_jogo():
    global flores_coletadas, direcao
    fim_jogo = False
    x, y = posicao_inicial

    # Gerando a primeira flor
    flor_x, flor_y = gerar_flor()

    while not fim_jogo:
        tela.fill(preto)

        # Mostrar o número de flores coletadas
        mostrar_mensagem()

        # Verificar eventos do jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    direcao = [-tamanho_quadrado, 0]
                elif evento.key == pygame.K_RIGHT:
                    direcao = [tamanho_quadrado, 0]
                elif evento.key == pygame.K_UP:
                    direcao = [0, -tamanho_quadrado]
                elif evento.key == pygame.K_DOWN:
                    direcao = [0, tamanho_quadrado]

        # Movimentar o "personagem" (ou "cobrinha")
        x += direcao[0]
        y += direcao[1]

        # Verificar se o personagem saiu da tela
        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_jogo = True

        # Desenhando a flor coletável
        desenhar_flor(flor_x, flor_y)

        # Verificando se o "personagem" pegou a flor
        if x == flor_x and y == flor_y:
            flores_coletadas += 1
            flor_x, flor_y = gerar_flor()  # Gerar uma nova flor

        # Exibindo o personagem (pode ser uma forma simples para esse exemplo)
        pygame.draw.rect(tela, amarelo, [x, y, tamanho_quadrado, tamanho_quadrado])

        # Atualizando a tela
        pygame.display.update()

        # Controlando a velocidade do jogo
        pygame.time.Clock().tick(velocidade)

    # Finalizando o Pygame
    pygame.quit()

# Rodando o jogo
rodar_jogo()
 