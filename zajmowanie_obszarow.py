import pygame
import random
import sys


def quit():
    sys.exit(0)


class Game:

    def __init__(self):
        self.background()
        self.pole_gry()
        self.napisy()
        self.kwadraty()
        self.music()

        self.a = (0, 0, 0)
        self.aa = (0, 0, 0)
        self.gracze = [Gracz((150, 370), self), Gracz((1130, 370), self)]  # Początkowe pozycje graczy 1. i 2.

        while True:
            self.klik()

            pygame.display.update()

    def background(self):
        self.screen = pygame.display.set_mode((1300, 700))

        background_image = pygame.image.load('tlo.png').convert()
        self.screen.blit(background_image, (0, 0))

        pygame.display.set_caption("Moja gra")

    def pole_gry(self):
        self.lista = []
        self.tura = 0

        self.kolory = {
            1: (255, 149, 0),   # pomarańczowy
            2: (255, 204, 0),   # żółty
            3: (255, 0, 0),     # czerwony
            4: (52, 170, 220),  # niebieski
            5: (76, 217, 100),  # zielony
            6: (142, 142, 147)  # szary
        }

        pygame.draw.rect(self.screen, self.kolory[1], (600, 15, 80, 40))
        pygame.draw.rect(self.screen, self.kolory[2], (700, 15, 80, 40))
        pygame.draw.rect(self.screen, self.kolory[3], (800, 15, 80, 40))
        pygame.draw.rect(self.screen, self.kolory[4], (900, 15, 80, 40))
        pygame.draw.rect(self.screen, self.kolory[5], (1000, 15, 80, 40))
        pygame.draw.rect(self.screen, self.kolory[6], (1100, 15, 80, 40))
        pygame.draw.rect(self.screen, (100, 100, 100), (1180, 150, 80, 40))
        pygame.draw.rect(self.screen, (100, 100, 100), (1180, 210, 80, 40))

        x = 150
        self.w = 20
        for i in range(50):
            y = 70

            for j in range(31):
                z = random.randint(1, 6)

                if (x == 150 and y == 370) or (x == 1130 and y == 370):
                    pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 20, 20))
                else:
                    pygame.draw.rect(self.screen, self.kolory[z], (x, y, 20, 20))

                self.lista.append(z)
                y += self.w

            x += self.w

    def napisy(self):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.screen.blit(self.myfont.render('Wybierz kolor, na jaki chcesz się zmienić:', False, (0, 0, 0)), (10, 15))  # na jaki kolor...
        self.screen.blit(self.myfont.render('Licznik:', False, (0, 0, 0)), (10, 300))  # lewy licznik
        self.screen.blit(self.myfont.render('Licznik:', False, (0, 0, 0)), (1170, 300))  # prawy licznik
        self.screen.blit(self.myfont.render('Muzyka:', False, (0, 0, 0)), (1170, 100))  # Muzyka:
        self.screen.blit(self.myfont.render('ON', False, (0, 0, 0)), (1195, 150))  # ON
        self.screen.blit(self.myfont.render('OFF', False, (0, 0, 0)), (1190, 210))  # OFF
        self.screen.blit(self.myfont.render('Zostało:', False, (0, 0, 0)), (10, 100))  # Pozostało

    def kwadraty(self):
        self.obszar = []
        i = 0

        for column in range(50):
            self.obszar.append([])

            for row in range(31):
                self.obszar[column].append([pygame.Rect((20 * column) + 150, (20 * row) + 70, 20, 20), self.lista[i], -1])
                i += 1

    @staticmethod
    def music():
        pygame.mixer.music.load('muzyka.ogg')
        pygame.mixer.music.play(-1)
        pygame.event.wait()

    @staticmethod
    def stopmusic():
        pygame.mixer.music.stop()

    def klik(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

                if 600 <= self.mouse_x <= 680 and 15 <= self.mouse_y <= 55:
                    if (self.tura % 2) == 0 and self.aa != self.kolory[1]:
                        self.aa = self.kolory[1]
                        Gracz.laczenie(self.gracze[0], self)
                        self.tura += 1
                        self.a = self.kolory[1]
                        pygame.draw.rect(self.screen, self.a, (150, 370, 20, 20))
    
                    elif (self.tura % 2) == 1 and self.aa != self.kolory[1]:
                        self.aa = self.kolory[1]
                        Gracz.laczenie(self.gracze[1], self)
                        self.tura += 1
                        self.a = self.kolory[1]
                        pygame.draw.rect(self.screen, self.a, (1130, 370, 20, 20))
    
                elif 700 <= self.mouse_x <= 780 and 15 <= self.mouse_y <= 55:
                    if (self.tura % 2) == 0 and self.aa != self.kolory[2]:
                        self.aa = self.kolory[2]
                        Gracz.laczenie(self.gracze[0], self)
                        self.tura += 1
                        self.a = self.kolory[2]
                        pygame.draw.rect(self.screen, self.a, (150, 370, 20, 20))

                    elif (self.tura % 2) == 1 and self.aa != self.kolory[2]:
                        self.aa = self.kolory[2]
                        Gracz.laczenie(self.gracze[1], self)
                        self.tura += 1
                        self.a = self.kolory[2]
                        pygame.draw.rect(self.screen, self.a, (1130, 370, 20, 20))

                elif 800 <= self.mouse_x <= 880 and 15 <= self.mouse_y <= 55:
                    if (self.tura % 2) == 0 and self.aa != self.kolory[3]:
                        self.aa = self.kolory[3]
                        Gracz.laczenie(self.gracze[0], self)
                        self.tura += 1
                        self.a = self.kolory[3]
                        pygame.draw.rect(self.screen, self.a, (150, 370, 20, 20))

                    elif (self.tura % 2) == 1 and self.aa != self.kolory[3]:
                        self.aa = self.kolory[3]
                        Gracz.laczenie(self.gracze[1], self)
                        self.tura += 1
                        self.a = self.kolory[3]
                        pygame.draw.rect(self.screen, self.a, (1130, 370, 20, 20))

                elif 900 <= self.mouse_x <= 980 and 15 <= self.mouse_y <= 55:
                    if (self.tura % 2) == 0 and self.aa != self.kolory[4]:
                        self.aa = self.kolory[4]
                        Gracz.laczenie(self.gracze[0], self)
                        self.tura += 1
                        self.a = self.kolory[4]
                        pygame.draw.rect(self.screen, self.a, (150, 370, 20, 20))

                    elif (self.tura % 2) == 1 and self.aa != self.kolory[4]:
                        self.aa = self.kolory[4]
                        Gracz.laczenie(self.gracze[1], self)
                        self.tura += 1
                        self.a = self.kolory[4]
                        pygame.draw.rect(self.screen, self.a, (1130, 370, 20, 20))

                elif 1000 <= self.mouse_x <= 1080 and 15 <= self.mouse_y <= 55:
                    if (self.tura % 2) == 0 and self.aa != self.kolory[5]:
                        self.aa = self.kolory[5]
                        Gracz.laczenie(self.gracze[0], self)
                        self.tura += 1
                        self.a = self.kolory[5]
                        pygame.draw.rect(self.screen, self.a, (150, 370, 20, 20))

                    elif (self.tura % 2) == 1 and self.aa != self.kolory[5]:
                        self.aa = self.kolory[5]
                        Gracz.laczenie(self.gracze[1], self)
                        self.tura += 1
                        self.a = self.kolory[5]
                        pygame.draw.rect(self.screen, self.a, (1130, 370, 20, 20))

                elif 1100 <= self.mouse_x <= 1180 and 15 <= self.mouse_y <= 55:
                    if (self.tura % 2) == 0 and self.aa != self.kolory[6]:
                        self.aa = self.kolory[6]
                        Gracz.laczenie(self.gracze[0], self)
                        self.tura += 1
                        self.a = self.kolory[6]
                        pygame.draw.rect(self.screen, self.a, (150, 370, 20, 20))

                    elif (self.tura % 2) == 1 and self.aa != self.kolory[6]:
                        self.aa = self.kolory[6]
                        Gracz.laczenie(self.gracze[1], self)
                        self.tura += 1
                        self.a = self.kolory[6]
                        pygame.draw.rect(self.screen, self.a, (1130, 370, 20, 20))

                elif 1180 <= self.mouse_x <= 1260 and 150 <= self.mouse_y <= 190:
                    self.music()

                elif 1180 <= self.mouse_x <= 1260 and 210 <= self.mouse_y <= 250:
                    self.stopmusic()

            if event.type == pygame.QUIT:
                quit()

	
class Gracz:

    def __init__(self, gracz, gra):
        self.x = gracz[0]
        self.y = gracz[1]
        self.color = gra.aa  # Kolor początkowy (self.color), później gra.a to kolor, który w danej rundzie wybrałem
        self.kwadraciki = [[pygame.Rect(self.x, self.y, 20, 20), self.color]]  # lista kwadratów, które należą do gracza
        self.lista_zastepcza = []

    def laczenie(self, gra):  # sprawdzanie czy okalające kwadraty mają ten sam kolor'
        self.dodane_kwadraciki = self.kwadraciki[:]
        self.dodane_kwadraciki.append('cokolwiek')

        while len(self.dodane_kwadraciki) != len(self.kwadraciki):
            self.dodane_kwadraciki = self.kwadraciki[:]
            self.lista_zastepcza = []

            for kwadracik in self.kwadraciki:
                self.kwadrat = (kwadracik[0].x - 150) // 20  # kolumna kwadratu, który jest nade mną (góra 1,2; lewo 3,4; dół 1,5; prawo 6,4)
                self.kwadrat2 = (kwadracik[0].y - 20 - 70) // 20  # wiersz kwadratu, który jest nade mną
                self.kwadrat3 = (kwadracik[0].x - 20 - 150) // 20  # kolumna kwadratu, który jest w lewo
                self.kwadrat4 = (kwadracik[0].y - 70) // 20  # wiersz kwadratu, który jest w lewo
                self.kwadrat5 = (kwadracik[0].y + 20 - 70) // 20  # wiersz kwadratu, który jest pode mną 
                self.kwadrat6 = (kwadracik[0].x + 20 - 150) // 20  # kolumna kwadratu, który jest w prawo

                self.zmiana_koloru(gra)
                if kwadracik[0].y <= 70:
                    pass
                else:
                    if kwadracik[1] == gra.kolory[gra.obszar[self.kwadrat][self.kwadrat2][1]]:  # góra
                        self.dodawanie_kwadratow(gra, 0)
        
                if kwadracik[0].x <= 150:
                    pass
                else:
                    if kwadracik[1] == gra.kolory[gra.obszar[self.kwadrat3][self.kwadrat4][1]]:  # lewo
                        self.dodawanie_kwadratow(gra, 1)

                if kwadracik[0].y >= 670:
                    pass
                else:
                    if kwadracik[1] == gra.kolory[gra.obszar[self.kwadrat][self.kwadrat5][1]]:  # dół
                        self.dodawanie_kwadratow(gra, 2)

                if kwadracik[0].x >= 1130:
                    pass
                else:
                    if kwadracik[1] == gra.kolory[gra.obszar[self.kwadrat6][self.kwadrat4][1]]:  # prawo
                        self.dodawanie_kwadratow(gra, 3)

            self.rysowanie_kwadratow(gra)
            for kwadracik in self.kwadraciki:
                try:
                    kwadracik[1] = gra.kolory[kwadracik[1]]
                except:
                    pass

            self.zastepcza = self.kwadraciki[:]
            self.kwadraciki = []
            self.kwadraciki.extend(self.lista_zastepcza)
            self.kwadraciki.extend(self.zastepcza)

            przechowywanie_rectow = []
            for kwadracik in self.kwadraciki:
                przechowywanie_rectow.append((kwadracik[0].x, kwadracik[0].y))

            przechowywanie_rectow = list(set(przechowywanie_rectow))

            self.kwadraciki = []
            for kwadracik in przechowywanie_rectow:
                self.kwadraciki.append([pygame.Rect(kwadracik[0], kwadracik[1], 20, 20), self.color])
    
            self.moje_kwadraty(gra)

    def zmiana_koloru(self, gra):
        self.color = gra.aa

        for kwadrat in self.kwadraciki:
            kwadrat[1] = self.color  # kwadrat[1] to kolor, na który zmieniam

    def dodawanie_kwadratow(self, gra, opcja):
        self.ty = (gra.tura % 2)
        zmienna = (gra.tura + 1) % 2

        if opcja == 0:
            a = self.kwadrat
            b = self.kwadrat2

            if (([gra.obszar[a][b][0], gra.obszar[a][b][1]] not in self.kwadraciki) and [gra.obszar[a][b][0], gra.obszar[a][b][1]] not in self.lista_zastepcza) and gra.obszar[a][b][2] != zmienna:
                self.lista_zastepcza.append([gra.obszar[a][b][0], gra.obszar[a][b][1]])

        elif opcja == 1:
            c = self.kwadrat3
            d = self.kwadrat4

            if (([gra.obszar[c][d][0], gra.obszar[c][d][1]] not in self.kwadraciki) and [gra.obszar[c][d][0], gra.obszar[c][d][1]] not in self.lista_zastepcza) and gra.obszar[c][d][2] != zmienna:
                self.lista_zastepcza.append([gra.obszar[c][d][0], gra.obszar[c][d][1]])

        elif opcja == 2:
            e = self.kwadrat
            f = self.kwadrat5

            if (([gra.obszar[e][f][0], gra.obszar[e][f][1]] not in self.kwadraciki) and [gra.obszar[e][f][0], gra.obszar[e][f][1]] not in self.lista_zastepcza) and gra.obszar[e][f][2] != zmienna:
                self.lista_zastepcza.append([gra.obszar[e][f][0], gra.obszar[e][f][1]])

        elif opcja == 3:
            g = self.kwadrat6
            h = self.kwadrat4

            if (([gra.obszar[g][h][0], gra.obszar[g][h][1]] not in self.kwadraciki) and [gra.obszar[g][h][0], gra.obszar[g][h][1]] not in self.lista_zastepcza) and gra.obszar[g][h][2] != zmienna:
                self.lista_zastepcza.append([gra.obszar[g][h][0], gra.obszar[g][h][1]])

        for kwadracik in self.lista_zastepcza:
            try:
                kwadracik[1] = gra.kolory[kwadracik[1]]
            except:
                pass

    def rysowanie_kwadratow(self, gra):
        for kwadracik in self.kwadraciki:
            pygame.draw.rect(gra.screen, self.color, kwadracik[0])

            x = (kwadracik[0].x - 150) // 20
            y = (kwadracik[0].y - 70) // 20
            gra.obszar[x][y][2] = (gra.tura % 2)

    def moje_kwadraty(self, gra):
        pygame.draw.rect(gra.screen, (255, 255, 255), (25, 170, 80, 50))

        # POZOSTAŁE PUNKTY DO ZDOBYCIA
        punkty = len(self.kwadraciki)
        zostalo = 1550 - len(gra.gracze[0].kwadraciki) - len(gra.gracze[1].kwadraciki)
        gra.screen.blit(gra.myfont.render(f'{zostalo}', True, (0, 0, 0)), (25, 170))

        # WARUNEK ZWYCIĘSTWA
        if zostalo == 0:
            gra.background() 
            gra.screen.blit(pygame.font.SysFont('Comic Sans MS', 50).render('Koniec gry', False, (0, 0, 0)), (400, 320))  # prawy licznik

        # LICZNIKI
        tura = (gra.tura % 2)
        pygame.draw.rect(gra.screen, (255, 255, 255), (22 + (tura * 1138), 350, 80, 50))
        gra.screen.blit(gra.myfont.render(f'{punkty}', True, (0, 0, 0)), (25 + (tura * 1145), 350))

        pygame.display.update()

        
if __name__ == '__main__':
    pygame.init()

    Game()
