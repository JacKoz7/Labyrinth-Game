# Importy wymagane do prawidłowego działania gry.
import pygame
from Board import GameState
from Button import button1

# Klasa Game_status służy do przechowywania informacji o stanie gry, takich jak ściany, znaleziony labirynt i zwycięzca.
class Game_status:
    def __init__(self, walls, found_labyrinth, winner):
        self.walls = walls
        self.found_labyrinth = found_labyrinth  # Znaleziony labirynt
        self.winner = winner

# Klasa Second_Stage reprezentuje kolejne etapy gry.
class Second_Stage:
    def __init__(self, treasure, labyrinth, cross):
        # Inicjalizacja zmiennych z pozycją skarbu, labiryntu i krzyża na planszy.
        self.treasure = treasure
        self.labyrinth = labyrinth
        self.cross = cross
        self.correct_squares = [cross]  # Lista zawierająca poprawne pola.

    # Metoda 'get_font' tworzy obiekt czcionki o określonym rozmiarze.
    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    # Metoda 'get_neighbours' zwraca listę sąsiednich pól dla danej pozycji.
    def get_neighbours(self, position):
        row, col = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbours = [(row + dr, col + dc) for dr, dc in directions]
        return neighbours

    # Metoda 'endgame' obsługuje logikę końca gry.
    def endgame(self, screen, txt, txt2, walls, labyrinth_temp, winner):
        # Inicjalizacja flag i zmiennych.
        cross_drawn = True
        treasure_drawn = False
        counter = 0

        # Inicjalizacja obiektu stanu planszy.
        BOARD = GameState()

        # Ładowanie obrazów.
        image_treasure = pygame.image.load('red_circle1.png')
        image_krzyzyk = pygame.image.load('red_krzyzyk1.png')
        image_point = pygame.image.load('red_point1.png')
        image_wall = pygame.image.load('wall.png')

        img = pygame.image.load('empty_button.png')

        # Tworzenie przycisku
        button_back = button1(image=img, pos=(1050, 600), text_input='Menu', font=self.get_font(65),
                              base_color='Black',
                              new_color='White')


        # Główna pętla gry.
        while True:
            play_mouse_pos = pygame.mouse.get_pos()
            location = BOARD.draw_board(screen)

            BOARD.draw_small_board(screen, counter)  # Szkicowanie zielonych green ticków

            # Rysowanie tekstu na ekranie.
            gracz1_text = self.get_font(180).render(txt, True, 'Red')
            gracz1_rect = gracz1_text.get_rect(center=(1050, 100))
            screen.blit(gracz1_text, gracz1_rect)

            button_back.ChangeColor(play_mouse_pos)
            button_back.update(screen)

            way_text = self.get_font(50).render('Odnajdz droge do skarbu ' + txt2, True, 'Red')
            way_rect = gracz1_text.get_rect(center=(1000, 300))

            if winner is False:
                screen.blit(way_text, way_rect)

            winner_text = self.get_font(100).render(txt + ' Wygrywa Gratulacje :)', True, 'Red')
            winner_rect = winner_text.get_rect(center=(700, 100))


            if cross_drawn:
                loc1, loc2 = self.cross
                screen.blit(image_krzyzyk, (102 + loc2 * 60, 52 + loc1 * 60))

            # Rysowanie scian
            for square in walls:
                loc1, loc2 = square
                screen.blit(image_wall, (102 + loc2 * 60, 52 + loc1 * 60))

            # rysowanie skarbu po narysowaniu scian
            if treasure_drawn:
                loc1, loc2 = self.treasure
                screen.blit(image_treasure, (102 + loc2 * 60, 52 + loc1 * 60))

            for square in labyrinth_temp:
                loc1, loc2 = square
                if square != self.cross and square != self.treasure:
                    screen.blit(image_point, (102 + loc2 * 60, 52 + loc1 * 60))

            if winner: #co się dzieje po tym jak ktoś wygra
                screen.fill('black')
                screen.blit(winner_text, winner_rect)

                winner_button_menu = button1(image=img, pos=(700, 500), text_input="Menu", font=self.get_font(65),
                                             base_color='Black',
                                             new_color='White')
                play_again_button = button1(image=img, pos=(700, 350), text_input="Od Nowa", font=self.get_font(65),
                                            base_color='Black', new_color='White')

                winner_button_menu.ChangeColor(play_mouse_pos)
                winner_button_menu.update(screen)

                play_again_button.ChangeColor(play_mouse_pos)
                play_again_button.update(screen)

                for event in pygame.event.get():
                    # Jeżeli kliknięto przycisk wygrywający...
                    if event.type == pygame.MOUSEBUTTONDOWN and winner_button_menu.CheckForInput(play_mouse_pos):
                        from Main import Labirynt
                        game = Labirynt()
                        game.main_menu()  # Przejście do menu głównego gry.

                    # Jeżeli kliknięto przycisk "Zagraj ponownie"...
                    if event.type == pygame.MOUSEBUTTONDOWN and play_again_button.CheckForInput(play_mouse_pos):
                        from Main import Labirynt
                        game = Labirynt(auto_start=False)
                        game.game_process()  # Rozpoczyna nową grę.

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and cross_drawn:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Sprawdza, czy kliknięcie myszy nastąpiło w granicach planszy.
                    if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
                        row = location[0]
                        col = location[1]

                        selected_square = (row, col)  # Zapisuje wybrane pole.
                        print(selected_square)  # Wyświetla wybrane pole.

                        # Jeżeli wybrane pole sąsiaduje z jakimkolwiek polem poprawnym i gra jeszcze się nie skończyła...
                        if any(selected_square in self.get_neighbours(correct_square) for correct_square in
                               self.correct_squares) and winner is False:
                            # Jeżeli wybrane pole jest częścią labiryntu...
                            if selected_square in self.labyrinth:
                                # Jeżeli wybrane pole nie jest jeszcze na liście poprawnych pól...
                                if selected_square not in self.correct_squares:
                                    labyrinth_temp.append(selected_square)  # Dodaje do listy tymczasowej labiryntu.
                                    self.correct_squares.append(selected_square)  # Dodaje do listy poprawnych pól.
                                    counter += 1  # Zwiększa licznik poprawnych ruchów.

                                # Jeżeli licznik wynosi 5 i wybrane pole to nie skarb...
                                if counter == 5 and selected_square != self.treasure:
                                    return  # Kończy działanie funkcji.

                                # Jeżeli licznik wynosi 4 i wybrane pole to skarb...
                                elif counter == 4 and selected_square == self.treasure:
                                    counter += 1  # Zwiększa licznik.

                                # Jeżeli wybrane pole to skarb...
                                if selected_square == self.treasure:
                                    treasure_drawn = True  # Ustawia rysowania skarbu na prawdę.
                                    winner = True  # Ustawia wartość wygranej na prawdę.

                            else:
                                # Jeżeli wybrane pole sąsiaduje z jakimkolwiek polem poprawnym, ale nie jest poprawnym ruchem...
                                if selected_square not in walls:
                                    walls.append(selected_square)  # Dodaje do listy ścian.
                                    return  # Kończy działanie funkcji.



                if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                    from Main import Labirynt
                    game = Labirynt()
                    game.main_menu()

                # Jeżeli zamknięto okno gry...
                if event.type == pygame.QUIT:
                    pygame.quit()  # Zamyka Pygame.
                    exit()  # Kończy działanie programu.

            pygame.display.update()  # Aktualizuje wyświetlaną grafikę gry.

