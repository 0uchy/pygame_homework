import pygame
import sys

pygame.init()

music_file = "music.mp3"

pygame.mixer.music.load(music_file)
def baslangic_pozisyonlarini_ayarla():
    semih_rect.x = width // 4
    semih_rect.y = height // 4

    hatice_rect.x = width // 2 - hatice_rect.width // 2
    hatice_rect.y = height // 2 - hatice_rect.height // 2


def hosgeldiniz_ekrani():
    font = pygame.font.Font(None, 36)
    hosgeldiniz_metni = font.render("Semih'in Macerasına Hoş Geldiniz", True, (255, 255, 255))
    hosgeldiniz_rect = hosgeldiniz_metni.get_rect(center=(width // 2, height // 2))
    screen.blit(hosgeldiniz_metni, hosgeldiniz_rect)
    pygame.display.flip()
    pygame.time.wait(3000)


def kurtarildi_ekrani():
    font = pygame.font.Font(None, 36)
    kurtarildi_metni = font.render("Prenses Hatice'yi kurtardın!!!", True, (255, 255, 255))
    kurtarildi_rect = kurtarildi_metni.get_rect(center=(width // 2, height // 2))
    screen.blit(kurtarildi_metni, kurtarildi_rect)
    pygame.display.flip()
    pygame.time.wait(1000)


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Semih's Adventure")

background_image = pygame.image.load("background.jpeg")
background_rect = background_image.get_rect()

semih_image = pygame.image.load("semih.png")
semih_rect = semih_image.get_rect()

hatice_image = pygame.image.load("hatice.png")
hatice_rect = hatice_image.get_rect()

hosgeldiniz_ekrani()

baslangic_pozisyonlarini_ayarla()

speed = 1
prenses_kurtarıldı = False

pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    semih_speed = 5

    if keys[pygame.K_LEFT]:
        semih_rect.x -= semih_speed
    if keys[pygame.K_RIGHT]:
        semih_rect.x += semih_speed
    if keys[pygame.K_UP]:
        semih_rect.y -= semih_speed
    if keys[pygame.K_DOWN]:
        semih_rect.y += semih_speed

    if semih_rect.colliderect(hatice_rect) and not prenses_kurtarıldı:
        kurtarildi_ekrani()
        print("Prenses Hatice'yi kurtardın!!!")
        prenses_kurtarıldı = True
        pygame.time.delay(5000)
        running = False

    screen.fill((255, 255, 255))

    screen.blit(background_image, background_rect)
    screen.blit(semih_image, semih_rect)
    screen.blit(hatice_image, hatice_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
