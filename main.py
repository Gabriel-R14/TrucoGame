import pygame

pygame.init()

dimensoes_tela = (800, 600)
tela = pygame.display.set_mode(dimensoes_tela)
pygame.display.set_caption('Truco')

fundo = pygame.image.load('imagens/fundoTruco.jpg')
fundo = pygame.transform.scale(fundo, dimensoes_tela)

logo = pygame.image.load('imagens/trucoLogo.png')
logo = pygame.transform.scale(logo, (220, 150))

fonte = pygame.font.Font(None, 32)

textoInicio = fonte.render('Insira um nome de usuário:', True, (255, 255, 255))

botaoInicio = pygame.Rect(300, 420, 200, 60)
textoBotao = fonte.render('JOGAR', True, (255, 255, 255))
corBotao = (255, 140, 0)

inputNome = pygame.Rect(270, 350, 200, 32)
corInputNome = (255, 255, 255)

username = ''

execuntando = True
while execuntando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            execuntando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                texto = username.strip()
                print("Texto inserido:", texto)
            elif evento.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += evento.unicode
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if botaoInicio.collidepoint(evento.pos):
                tela.fill((255, 255, 255))
    
    tela.blit(fundo, (0, 0))
    tela.blit(logo, (300, 80))
    tela.blit(textoInicio, (270, 300))

    pygame.draw.rect(tela, corBotao, botaoInicio)
    tela.blit(textoBotao, (300 + (200 - textoBotao.get_width()) / 2, 420 + (60 - textoBotao.get_height()) / 2))

    pygame.draw.rect(tela, corInputNome, inputNome)
    texto_superficie = fonte.render(username, True, (0, 0, 0))
    tela.blit(texto_superficie, (inputNome.x + 5, inputNome.y + 5))

    pygame.display.flip()

pygame.quit()