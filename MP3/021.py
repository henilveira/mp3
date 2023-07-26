import pygame
import random

musicas = ['Flawles_ -_Yeat.mp3', 'Too_Many_Nights_-_Don_Toliver.mp3', 'On_the_line_-_Yeat.mp3']
r_musica = random.choice(musicas)


def tocar_musica(musica):
    pygame.mixer.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()


def parar_musica():
    pygame.mixer.music.stop()


def main():
    print("MP3 do HS")
    print("-------------------")

    while True:
        print("1. Tocar Musica")
        print("2. Parar Musica")
        print("3. Sair")

        menu = input('Escolha uma das opções: ')
        if menu == "1":
            print('Tocando "{}" em Python!'.format(r_musica))
            musica = r_musica
            tocar_musica(musica)
        elif menu == "2":
            print('Musica pausada!')
            parar_musica()
        elif menu == "3":
            print('Até mais!')
            parar_musica()
            break
        else:
            print('Digite uma opção válida')


if __name__ == "__main__":
    main()
