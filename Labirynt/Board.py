import pygame #
class GameState():
    def __init__(self):
        self.selected_point = None
    def draw_board(self, SCREEN):
        SCREEN.fill('Black')
        global square_size
        square_size = 60
        for row in range(10):
            for col in range(10):
                pygame.draw.rect(SCREEN, 'Red', (100 + col * square_size, 50 + row * square_size, square_size, square_size), 2)
#
        # Sprawdzenie, czy kursorem myszy jest zaznaczona komórka
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 100 <= mouse_x <= 100 + 10 * square_size and 50 <= mouse_y <= 50 + 10 * square_size:
            selected_col = (mouse_x - 100) // square_size #square size = 60 pierwszy index w tablicy
            selected_row = (mouse_y - 50) // square_size #drugi index w tablicy

            # Zaznaczanie wybranej komórki
            pygame.draw.rect(SCREEN, 'Red', (
            100 + selected_col * square_size, 50 + selected_row * square_size, square_size, square_size), 5)

            # Aktualizacja wybranej komórki w obiekcie GameState
            self.selected_point = (selected_row, selected_col)
            return self.selected_point
        else:
            return None
    def draw_small_board(self, SCREEN):
        for x in range(5):
            pygame.draw.rect(SCREEN, 'Red', (900 + x * square_size, 330 + square_size, square_size, square_size), 7)
