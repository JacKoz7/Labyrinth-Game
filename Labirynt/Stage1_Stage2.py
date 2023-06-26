import pygame  # Importowanie modułu pygame
from Board import GameState  # Import Klasy GameState
from Button import button  # Import Klasy button
#

# Klasa reprezentująca Pierwszą fazę gry
class First_Stage:
    # Konstruktor klasy, inicjalizuje podstawowe atrybuty
    def __init__(self):
        self.treasure = (0, 0)  # Pozycja skarbu
        self.labyrinth = []  # Lista przechowująca elementy labiryntu
        self.cross = (0, 0)  # Pozycja krzyża

    # Metoda zwracająca czcionkę o określonym rozmiarze
    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    # Metoda zwracająca współrzędne wybranego pola
    def selected_square(self, location, mouse_x, mouse_y):
        if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
            row = location[0]
            col = location[1]
            return row, col
        else:
            return None

    # Metoda odpowiedzialna za rozgrywkę
    def play(self, screen, txt, ButtonText):


        # Logika gry
        treasure_drawn = False  # Czy skarb został narysowany
        labyrinth_drawn = False  # Czy labirynt został narysowany
        cross_drawn = False  # Czy krzyż został narysowany

        show_step1 = True  # Czy pokazać krok 1
        show_step2 = False  # Czy pokazać krok 2
        show_step3 = False  # Czy pokazać krok 3
        show_step4 = False  # Czy pokazać krok 4

        show_next_move = False  # Czy pokazać następny ruch (Kiedy labirynt już jest narysowany)

        selected_treasure = None  # Wybrany skarb
        selected_cross = None  # Wybrany krzyż

        must_restart = False  # Czy należy zrestartować

        BOARD = GameState()  # Tworzenie instancji klasy GameState

        # Ładowanie obrazów
        image_treasure = pygame.image.load('red_circle1.png')
        image_labyrinth = pygame.image.load('red_point1.png')
        image_cross = pygame.image.load('red_krzyzyk1.png')
        img = pygame.image.load('empty_button.png')

        while True:

            play_mouse_pos = pygame.mouse.get_pos()

            location = BOARD.draw_board(screen)

            # Rysowanie i wyświetlanie na ekranie poszczególnych kroków gry
            gracz1_text = self.get_font(180).render(txt, True, 'Red')
            gracz1_rect = gracz1_text.get_rect(center=(1050, 100))
            screen.blit(gracz1_text, gracz1_rect)

            step1_text = self.get_font(50).render('1. Zaznacz skarb', True, 'Red')
            step1_rect = step1_text.get_rect(center=(1050, 300))

            step2_text = self.get_font(50).render('2. Narysuj Labirynt', True, 'Red')
            ste2_rect = step2_text.get_rect(center=(1050, 300))

            step3_text = self.get_font(50).render('3. Ustaw Krzyzyk', True, 'Red')
            ste3_rect = step2_text.get_rect(center=(1050, 300))

            step4_text = self.get_font(60).render(txt + ', spróbuj ponownie!', True, 'Red')
            step4_rect = step1_text.get_rect(center=(900, 230))

            # Tworzenie i aktualizowanie przycisku powrotu do menu
            img = pygame.image.load('empty_button.png')

            button_back = button(image=img, pos=(1050, 600), text_input='Menu', font=self.get_font(65),
                                 base_color='Black',
                                 new_color='White')
            button_back.ChangeColor(play_mouse_pos)
            button_back.update(screen)
            #
            # Wyświetlanie odpowiednich kroków na ekranie w zależności od stanu gry
            if show_step1:
                screen.blit(step1_text, step1_rect)
            if show_step2:
                screen.blit(step2_text, ste2_rect)
            if show_step3:
                screen.blit(step3_text, ste3_rect)
            if show_step4:
                screen.blit(step4_text, step4_rect)
            if show_next_move:
                # Tworzenie przycisku
                button_player2 = button(image=img, pos=(1050, 480), text_input=ButtonText, font=self.get_font(65),
                                        base_color='Black',
                                        new_color='White')
                button_player2.ChangeColor(play_mouse_pos)
                button_player2.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and button_player2.CheckForInput(play_mouse_pos):
                        return


            # Rysowanie skarbu, labiryntu i krzyża na planszy w zależności od stanu gry
            if treasure_drawn:
                row, col = selected_treasure
                screen.blit(image_treasure, (102 + col * 60, 52 + row * 60))

            if labyrinth_drawn:
                for square in self.labyrinth:
                    if square != selected_cross and square != selected_treasure:
                        row, col = square
                        screen.blit(image_labyrinth, (102 + col * 60, 52 + row * 60))

            if cross_drawn:
                row, col = selected_cross
                screen.blit(image_cross, (102 + col * 60, 52 + row * 60))

            # Obsługa zdarzeń
            for event in pygame.event.get():

                # Zresetowanie gry, gdy użytkownik nie ustawi krzyżyka na brzegu lub w rogu
                if must_restart:
                    self.treasure = []
                    self.labyrinth = []

                    treasure_drawn = False
                    labyrinth_drawn = False

                    show_step1 = True
                    show_step3 = False
                    show_step2 = False
                    show_step4 = True

                    selected_treasure = None
                    selected_cross = None

                    must_restart = False

                # Rysowanie Skarbu
                # W momencie kliknięcia myszą i braku wcześniej narysowanego skarbu
                if event.type == pygame.MOUSEBUTTONDOWN and not treasure_drawn:

                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Pobranie pozycji myszy

                    # Pobranie pozycji skarbu
                    selected_treasure = self.selected_square(location, mouse_x, mouse_y)

                    # Jeśli wybrany skarb nie jest pusty, rysujemy skarb jako narysowany i przechodzimy dalej
                    if selected_treasure is not None:
                        treasure_drawn = True
                        show_step1 = False
                        show_step2 = True

                        # Dodanie skarbu do labiryntu dla pożniejszej mechaniki gry
                        self.labyrinth.append(selected_treasure)

                # Rysowanie labiryntu
                if event.type == pygame.MOUSEBUTTONDOWN and treasure_drawn and len(self.labyrinth) < 37:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    selected_labyrinth = self.selected_square(location, mouse_x, mouse_y)

                    # Jeśli wybrany fragment labiryntu nie jest pusty
                    if selected_labyrinth is not None:

                        # Jeśli wybrany fragment labiryntu sąsiaduje z innym fragmentem, dodaj go do labiryntu
                        for last_square in self.labyrinth:
                            if selected_labyrinth == (last_square[0] - 1, last_square[1]) or \
                                    selected_labyrinth == (last_square[0] + 1, last_square[1]) or \
                                    selected_labyrinth == (last_square[0], last_square[1] - 1) or \
                                    selected_labyrinth == (last_square[0], last_square[1] + 1):

                                # Aby powtórnie nie dodać wybranej kratki oraz skarbu do labiryntu
                                if selected_labyrinth not in self.labyrinth and selected_labyrinth != self.labyrinth[0]:
                                    self.labyrinth.append(selected_labyrinth)
                                    break  # przerwanie pętli, jeżeli znaleźliśmy pasujący kwadrat

                        labyrinth_drawn = True

                        # Jeśli labirynt jest pełny, przechodzimy do następnego kroku
                        if len(self.labyrinth) == 36:
                            show_step2 = False
                            show_step3 = True

                # Rysowanie krzyzyka
                if event.type == pygame.MOUSEBUTTONDOWN and treasure_drawn and len(
                        self.labyrinth) == 37 and not cross_drawn:

                    # Sprawdzanie, czy wybrany kwadrat jest na brzegu
                    if location[0] == 0 or location[0] == 9 or location[1] == 0 or location[1] == 9:

                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        selected_cross = self.selected_square(location, mouse_x, mouse_y)

                        # Jeżeli wybrany krzyż nie jest pusty,
                        # zakończenie procesu rysowania i zapisanie pozycji skarbu oraz krzyża
                        if selected_cross is not None:
                            cross_drawn = True
                            show_step3 = False
                            show_step4 = False

                            self.treasure = self.labyrinth[0]
                            self.cross = self.labyrinth[-1]

                            show_next_move = True
                    else:
                        # Jeśli krzyż nie został narysowany na brzegu, zresetuj grę
                        cross_drawn = False
                        must_restart = True
                # Zamykanie gry
                if event.type == pygame.QUIT:
                    pygame.quit()  # Zamyka Pygame
                    exit()  # Kończy działanie programu
                # Powrót do głównego menu
                if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                    from Main import Labirynt
                    game = Labirynt()
                    game.main_menu()
                # Przejście do następnego Gracza / do 2 Etapu Gry


            pygame.display.update()  # Aktualizuje wyświetlaną grafikę gry
