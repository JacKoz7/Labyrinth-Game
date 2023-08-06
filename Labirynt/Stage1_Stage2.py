import pygame  # Importowanie modułu pygame
from Board import GameState  # Import Klasy GameState
from Button import Button  # Import Klasy button
from Randomize import RandomizeButton, place_treasure, place_cross, generate_maze


# Klasa reprezentująca Pierwszą fazę gry
class First_Stage:
    # Konstruktor klasy, inicjalizuje podstawowe atrybuty
    def __init__(self):
        self.treasure = (0, 0)  # Pozycja skarbu
        self.labyrinth = []  # Lista przechowująca elementy labiryntu
        self.cross = (0, 0)  # Pozycja krzyża
        self.maze = generate_maze()
        self.rtreasure = place_treasure()
        self.rcross = place_cross(self.rtreasure)

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
    def play(self, screen, txt, button_text):

        # Logika gry
        treasure_drawn = False
        labyrinth_drawn = False
        cross_drawn = False
        random_treasure_drawn = False
        random_cross_drawn = False
        random_labyrinth_drawn = False

        show_step1 = True
        show_step2 = False
        show_step3 = False
        show_step4 = False

        show_next_move = False  # Czy pokazać następny ruch (Kiedy labirynt już jest narysowany)

        selected_treasure = None
        selected_cross = None

        must_restart = False

        board = GameState()  # Tworzenie instancji klasy GameState

        # Ładowanie obrazów
        image_treasure = pygame.image.load('Images/red_circle1.png')
        image_labyrinth = pygame.image.load('Images/red_point1.png')
        image_cross = pygame.image.load('Images/red_krzyzyk1.png')

        img_undo = pygame.image.load('Images/return_button.png')
        img_return = pygame.image.load('Images/return.png')

        while True:

            player_mouse_pos = pygame.mouse.get_pos()

            location = board.draw_board(screen)

            # Rysowanie i wyświetlanie na ekranie poszczególnych kroków gry
            player_text = self.get_font(180).render(txt, True, 'Red')
            player_rect = player_text.get_rect(center=(1050, 100))
            screen.blit(player_text, player_rect)

            step1_text = self.get_font(50).render('1. Zaznacz skarb', True, 'Red')
            step1_rect = step1_text.get_rect(center=(1050, 300))

            step2_text = self.get_font(50).render('2. Narysuj Labirynt', True, 'Red')
            ste2_rect = step2_text.get_rect(center=(1050, 300))

            step3_text = self.get_font(50).render('3. Ustaw Krzyzyk', True, 'Red')
            ste3_rect = step2_text.get_rect(center=(1050, 300))

            step4_text = self.get_font(60).render(txt + ', spróbuj ponownie!', True, 'Red')
            step4_rect = step1_text.get_rect(center=(900, 230))

            # Tworzenie i aktualizowanie przycisku powrotu do menu
            img_button = pygame.image.load('Images/empty_button.png')
            randomizer_button_image = pygame.image.load(('Images/Randomizer_button.png'))

            menu_button = Button(image=img_button, pos=(1050, 600), text_input='Menu', font=self.get_font(65),
                                 base_color='Black',
                                 new_color='White')
            menu_button.ChangeColor(player_mouse_pos)
            menu_button.Update(screen)

            # Prycisk Undo
            undo_button = Button(image=img_undo, pos=(1290, 600), text_input='', font=self.get_font(65),
                                 base_color='Black',
                                 new_color='White')

            return_button = Button(image=img_return, pos=(1290, 600), text_input='', font=self.get_font(65),
                                   base_color='Black',
                                   new_color='White')

            # Przycisk Randomize
            randomize_button = RandomizeButton(image=randomizer_button_image, pos=(810,600))
            randomize_button.ChangeColor(player_mouse_pos)
            randomize_button.Update(screen)

            # Tworzenie przycisku przejścia do następnego Gracza / 2 Etapu gry
            button_player2 = Button(image=img_button, pos=(1050, 480), text_input=button_text, font=self.get_font(65),
                                    base_color='Black',
                                    new_color='White')

            # Wyświetlanie odpowiednich kroków na ekranie w zależności od stanu gry
            if show_step1:
                screen.blit(step1_text, step1_rect)
            if show_step2:
                screen.blit(step2_text, ste2_rect)
            if show_step3:
                screen.blit(step3_text, ste3_rect)
            if show_step4:
                screen.blit(step4_text, step4_rect)

            # Wyświetlenie przycisku przejścia do następnego Gracza / 2 Etapu gry
            if show_next_move:
                button_player2.ChangeColor(player_mouse_pos)
                button_player2.Update(screen)

            # Rysowanie skarbu, labiryntu i krzyża na planszy w zależności od stanu gry
            if treasure_drawn:
                row, col = selected_treasure
                screen.blit(image_treasure, (102 + col * 60, 52 + row * 60))

            if labyrinth_drawn:
                for square in self.labyrinth:
                    if square != selected_cross and square != selected_treasure:
                        row, col = square
                        screen.blit(image_labyrinth, (102 + col * 60, 52 + row * 60))

                        if 1 < len(self.labyrinth) <= 36:
                            return_button.ChangeColorImage(player_mouse_pos)

                            undo_button.Update(screen)
                            return_button.Update(screen)

            if random_labyrinth_drawn:
                for square in self.maze:
                    if square != place_cross(place_treasure()) and square != place_treasure():
                        row, col = square
                        screen.blit(image_labyrinth, (102 + col * 60, 52 + row * 60))


            if cross_drawn:
                row, col = selected_cross
                screen.blit(image_cross, (102 + col * 60, 52 + row * 60))

            if random_cross_drawn:
                row, col = self.rcross
                screen.blit(image_cross, (102 + col * 60, 52 + row * 60))

            if random_treasure_drawn:
                row, col = self.rtreasure
                screen.blit(image_treasure, (102 + col * 60, 52 + row * 60))

            # Obsługa zdarzeń
            for event in pygame.event.get():

                # Zresetowanie gry, gdy użytkownik nie ustawi krzyżyka na brzegu lub w rogu
                if must_restart:
                    self.treasure = []
                    self.labyrinth = []

                    treasure_drawn = False
                    labyrinth_drawn = False

                    show_step1 = True
                    show_step2 = False
                    show_step3 = False
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

                        # Dodanie skarbu do labiryntu
                        self.labyrinth.append(selected_treasure)
                    # print(selected_treasure)

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

                # Rysowanie krzyżyka
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

                # Powrót do głównego menu
                if event.type == pygame.MOUSEBUTTONDOWN and menu_button.CheckForInput(player_mouse_pos):
                    from Main import Labirynt
                    game = Labirynt()
                    game.main_menu()

                # Przycisk Undo
                if event.type == pygame.MOUSEBUTTONDOWN and undo_button.CheckForInput(player_mouse_pos) and \
                        return_button.CheckForInput(player_mouse_pos) and 1 < len(self.labyrinth) <= 36:

                    self.labyrinth.pop(-1)

                    if len(self.labyrinth) <= 36:
                        show_step3 = False
                        show_step2 = True

                # Przycisk Randomize
                if event.type == pygame.MOUSEBUTTONDOWN and randomize_button.CheckForInput(player_mouse_pos):

                    labyrinth_drawn = False
                    treasure_drawn = False
                    cross_drawn = False
                    random_treasure_drawn = True
                    random_cross_drawn = True
                    random_labyrinth_drawn = True
                    show_next_move = True

                # Przejście do następnego Gracza / do 2 Etapu Gry
                if show_next_move:
                    if event.type == pygame.MOUSEBUTTONDOWN and button_player2.CheckForInput(player_mouse_pos):
                        return

                # Zamykanie gry
                if event.type == pygame.QUIT:
                    pygame.quit()  # Zamyka Pygame
                    exit()  # Kończy działanie programu

            pygame.display.update()  # Aktualizuje wyświetlaną grafikę gry
