import pygame  # Importowanie modułu pygame
from sys import exit  # Import metody exit
from Button import Button  # Import Klasy button
from instruction import inst  # Import funkcji
from Stage1_Stage2 import First_Stage  # Import Klasy First_Stage
from Stage3_Stage4 import Second_Stage, Game_status  # Import Klas Second_Stage oraz Game_status


# Definicja głównej klasy Labirynt
class Labirynt:
    # Konstruktor klasy, inicjalizuje podstawowe atrybuty
    def __init__(self, auto_start=True):
        pygame.init()  # Inicjalizacja modułu pygame
        self.clock = pygame.time.Clock()  # Tworzenie obiektu zegara
        self.h = 700
        self.screen = pygame.display.set_mode((2 * self.h, self.h))  # Ustawianie trybu wyświetlania
        pygame.display.set_caption('Labirynt')  # Ustawianie tytułu okna
        self.txt2 = 'Gracz 2'
        self.txt = 'Gracz 1'
        self.icon = pygame.image.load("Images/game_icon.png")
        pygame.display.set_icon(self.icon)

        if auto_start:
            self.main_menu()  # Wywołanie metody main_menu przy tworzeniu obiektu

    # Metoda zwracająca czcionkę o określonym rozmiarze
    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    # Metoda reprezentująca proces gry
    def game_process(self):

        # Tworzenie obiektów 1 etapu gry dla obu Graczy
        Player1_beginning = First_Stage()
        Player2_beginning = First_Stage()

        # Tworzenie obiektów przechowywujących status gry dla obu Graczy
        Player1_status = Game_status(walls=[], found_labyrinth=[], winner=False)
        Player2_status = Game_status(walls=[], found_labyrinth=[], winner=False)

        # Wyłowanie metody pierwszego etapu gry dla Gracza 1
        Player1_beginning.play(self.screen, self.txt, 'Gracz 2 ')

        # Tworzenie obiektu 2 etapu gry dla Gracza 1 przy pomocy 'konstruktora z parametrami'
        Player1_ending = Second_Stage(Player1_beginning.treasure,
                                      Player1_beginning.labyrinth,
                                      Player1_beginning.cross)

        # Analogicznie dla Gracza 2
        Player2_beginning.play(self.screen, self.txt2, 'Kontynuuj ')
        Player2_ending = Second_Stage(Player2_beginning.treasure,
                                      Player2_beginning.labyrinth,
                                      Player2_beginning.cross)

        # Pętla wykonująca się do momentu wygrania jednego z graczy (pole 'winner' jest ciągle aktualizowane)
        while Player1_status.winner is False and Player2_status.winner is False:
            if Player1_status.winner is False:
                Player2_ending.endgame(self.screen, self.txt, self.txt2, Player1_status.walls,
                                       Player1_status.found_labyrinth, Player2_status.winner)

            if Player2_status.winner is False:
                Player1_ending.endgame(self.screen, self.txt2, self.txt, Player2_status.walls,
                                       Player2_status.found_labyrinth, Player1_status.winner)

    # Metoda wyświetlająca instrukcje gry
    def instructions(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()  # Pobranie pozycji myszy
            self.screen.fill('Black')  # Wypełnienie ekranu kolorem czarnym

            # Stworzenie i wyświetlenie tytułu 'Instrukcja gry:'
            options_text = self.get_font(55).render('Instrukcja gry:', True, 'Red')
            options_rect = options_text.get_rect(center=(self.h, 100))
            self.screen.blit(options_text, options_rect)

            inst(self.screen, self.get_font(35),
                 self.h)  # Wywołanie funkcji inst z pliku instructions, która wyświetla właściwe instrukcje

            img_button = pygame.image.load('Images/empty_button.png')  # Ładowanie obrazu dla przycisku.

            # Stworzenie przycisku 'Menu'
            menu_button = Button(image=img_button, pos=(180, 80), text_input='Menu', font=self.get_font(65),
                                 base_color='Black', new_color='White')

            menu_button.ChangeColor(options_mouse_pos)  # Zmiana koloru przycisku, jeśli mysz jest nad nim
            menu_button.Update(self.screen)  # Aktualizacja wyświetlanego przycisku na ekranie

            for event in pygame.event.get():  # Obsługa zdarzeń
                if event.type == pygame.QUIT:  # Jeżeli zamknięto okno gry
                    pygame.quit()  # Zamyka Pygame
                    exit()  # Kończy działanie programu

                if event.type == pygame.MOUSEBUTTONDOWN:  # Jeżeli kliknięto przycisk myszy
                    if menu_button.CheckForInput(options_mouse_pos):
                        self.main_menu()  # Przejście do menu głównego

            pygame.display.update()  # Aktualizacja wyświetlanego obrazu gry

    # Metoda implementująca menu gry
    def main_menu(self):
        while True:
            menu_mouse_pos = pygame.mouse.get_pos()
            bg = pygame.image.load("Images/game_background.png")
            self.screen.blit(bg, (0, 0))
            menu_text = self.get_font(200).render('Labirynt', True, 'Red')
            menu_rect = menu_text.get_rect(center=(self.h, 100))

            img = pygame.image.load('Images/empty_button.png')

            play_button = Button(image=img, pos=(self.h, 280), text_input='Graj', font=self.get_font(65),
                                 base_color='Black', new_color='White')

            instruction_button = Button(image=img, pos=(self.h, 430), text_input='Instrukcja', font=self.get_font(65),
                                    base_color='Black', new_color='White')

            quit_button = Button(image=img, pos=(self.h, 580), text_input='Wyjscie', font=self.get_font(65),
                                 base_color='Black', new_color='White')

            self.screen.blit(menu_text, menu_rect)

            for buttons in [play_button, instruction_button, quit_button]:  # Iteracja przez listę przycisków
                buttons.ChangeColor(menu_mouse_pos)
                buttons.Update(self.screen)

            # Obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.CheckForInput(menu_mouse_pos):
                        self.game_process()

                    if instruction_button.CheckForInput(menu_mouse_pos):
                        self.instructions()

                    if quit_button.CheckForInput(menu_mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

    # Metoda slużąca do uruchomienia gry
    def run(self):
        self.main_menu()


# Instrukcja warunkowa sprawdzająca, czy skrypt jest uruchamiany bezpośrednio czy importowany
if __name__ == "__main__":
    game = Labirynt()  # Tworzenie obiektu klasy Labirynt
    game.run()  # Wywołanie metody run na obiekcie game