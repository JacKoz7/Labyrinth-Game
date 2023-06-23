import pygame #
class GameState():
    def __init__(self):
        self.selected_point = None
        self.square_size = 60
        self.tick_image = pygame.image.load('green_tick.png')
    def draw_board(self, SCREEN):
        SCREEN.fill('Black')

        for row in range(10):
            for col in range(10):
                pygame.draw.rect(SCREEN, 'Red', (100 + col * self.square_size, 50 + row * self.square_size, self.square_size, self.square_size), 2)
#
        # Sprawdzenie, czy kursorem myszy jest zaznaczona komórka
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 100 <= mouse_x <= 100 + 10 * self.square_size and 50 <= mouse_y <= 50 + 10 * self.square_size:
            selected_col = (mouse_x - 100) // self.square_size #square size = 60 pierwszy index w tablicy
            selected_row = (mouse_y - 50) // self.square_size #drugi index w tablicy

            # Zaznaczanie wybranej komórki
            pygame.draw.rect(SCREEN, 'Red', (
            100 + selected_col * self.square_size, 50 + selected_row * self.square_size, self.square_size, self.square_size), 5)

            # Aktualizacja wybranej komórki w obiekcie GameState
            self.selected_point = (selected_row, selected_col)
            return self.selected_point
        else:
            return None
    def draw_small_board(self, SCREEN, counter):
        for x in range(5):
            pygame.draw.rect(SCREEN, 'Red', (900 + x * self.square_size, 330 + self.square_size, self.square_size, self.square_size), 7)
            if x < counter:  # Jeżeli mamy mniej zielonych zaznaczeń niż licznik
                SCREEN.blit(self.tick_image, (900 + x * self.square_size, 330 + self.square_size))  # Rysujemy zielone zaznaczenie
