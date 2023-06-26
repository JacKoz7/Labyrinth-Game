import pygame  # Importowanie modułu pygame
#

# Klasa reprezentująca stan gry
class GameState:
    # Konstruktor klasy, inicjalizuje podstawowe atrybuty
    def __init__(self):
        self.selected_point = None  # Początkowo żadne pole nie jest zaznaczone
        self.square_size = 60  # Rozmiar pola
        self.tick_image = pygame.image.load('green_tick.png')  # Obrazek zielonej fajki
        self.x = pygame.image.load("Red_X.png")

    # Metoda zwracająca obiekt czcionki
    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    # Metoda rysująca planszę
    def draw_board(self, SCREEN):
        SCREEN.fill('Black')  # Wypełnienie ekranu kolorem czarnym

        # Rysowanie planszy 10x10
        for row in range(10):
            for col in range(10):
                pygame.draw.rect(SCREEN, 'Red', (
                    100 + col * self.square_size, 50 + row * self.square_size, self.square_size, self.square_size), 2)

        # Sprawdzenie, czy wybrano pole na planszy
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Pobranie pozycji kursora myszy
        if 100 <= mouse_x <= 99 + 10 * self.square_size and 50 <= mouse_y <= 49 + 10 * self.square_size:
            selected_col = (mouse_x - 100) // self.square_size  # Obliczenie wybranej kolumny
            selected_row = (mouse_y - 50) // self.square_size  # Obliczenie wybranego wiersza

            # Zaznaczanie wybranego pola
            pygame.draw.rect(SCREEN, 'Red', (
                100 + selected_col * self.square_size, 50 + selected_row * self.square_size, self.square_size,
                self.square_size), 5)

            # Aktualizacja wybranego pola
            self.selected_point = (selected_row, selected_col)

            return self.selected_point
        else:
            return None

    # Metoda rysująca małą planszę służącą do zaznaczania fajek w 2 etapie gry
    def draw_small_board(self, SCREEN, counter, wall):
        for x in range(5):  # Pętla przez 5 pól
            pygame.draw.rect(SCREEN, 'Red',
                             (900 + x * self.square_size, 330 + self.square_size, self.square_size, self.square_size),
                             7)
            if x < counter:  # Jeżeli jest mniej zaznaczonych pól niż licznik
                SCREEN.blit(self.tick_image,
                            (900 + x * self.square_size, 330 + self.square_size))  # Rysowanie zielonej fajki
        if wall:
            SCREEN.blit(self.x,
                        (900 + counter * self.square_size, 330 + self.square_size))  # Rysowanie zielonej fajki
