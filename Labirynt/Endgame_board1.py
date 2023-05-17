import pygame
from General import Labirynt
from Button import button1
from Board import GameState

def get_font(size):
    return pygame.font.Font('Ancient Medium.ttf', size)

def player1_endgame(a3, b3, c3, screen):  # parametry a b c to wspolrzedne skarbu labiryntu i krzyzyka z planszy gracza 2
    print('wspolrzedne drugiego gracza')
    print(a3)
    b3.reverse()
    print(b3)
    print(c3)

    cross_drawn = True
    wrong_squares = []
    treasure_position = None

    point_counter = 0
    selected_squares = []

    game = Labirynt()
    BOARD = GameState()
    image_treasure = pygame.image.load('red_circle1.png')
    image_krzyzyk = pygame.image.load('red_krzyzyk1.png')
    image_point = pygame.image.load('red_point1.png')
    image_wall = pygame.image.load('wall.png')
    tick_image = pygame.image.load('green_tick.png')

    while True:
        play_mouse_pos = pygame.mouse.get_pos()
        location = BOARD.draw_board(screen)

        BOARD.draw_small_board(screen)

        gracz1_text = get_font(180).render('Gracz 1', True, 'Red')
        gracz1_rect = gracz1_text.get_rect(center=(1050, 100))
        screen.blit(gracz1_text, gracz1_rect)

        way_text = get_font(50).render('Odnajdz droge do skarbu gracza 2', True, 'Red')
        way_rect = gracz1_text.get_rect(center=(1000, 300))
        screen.blit(way_text, way_rect)

        if cross_drawn:
            loc1, loc2 = c3[0]
            screen.blit(image_krzyzyk, (102 + loc2 * 60, 52 + loc1 * 60))

        if treasure_position is not None:
            loc1, loc2 = treasure_position
            screen.blit(image_treasure, (102 + loc2 * 60, 52 + loc1 * 60))

        for square in wrong_squares:
            loc1, loc2 = square
            screen.blit(image_wall, (102 + loc2 * 60, 52 + loc1 * 60))

        for square in selected_squares:
            loc1, loc2 = square
            screen.blit(image_point, (102 + loc2 * 60, 52 + loc1 * 60))

        def is_adjacent(sq1, sq2):
            """Funkcja sprawdzająca, czy dwa kwadraty sąsiadują ze sobą"""
            return abs(sq1[0] - sq2[0]) + abs(sq1[1] - sq2[1]) == 1

        img = pygame.image.load('empty_button.png')
        button_back = button1(image=img, pos=(1050, 600), text_input='Menu', font=get_font(65), base_color='Black',
                              new_color='White')
        button_back.ChangeColor(play_mouse_pos)
        button_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and cross_drawn:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
                    row = location[0]
                    col = location[1]
                    selected_square = (row, col)
                    print(selected_square)
                    # Sprawdzamy, czy naciśnięta kratka jest sąsiadująca z ostatnim poprawnie zaznaczonym polem
                    if selected_squares and not is_adjacent(selected_square, selected_squares[-1]):
                        continue  # Jeżeli nie jest sąsiadująca, ignorujemy tę akcję
                    if point_counter == len(b3) and selected_square == a3[0]:  # Nowy warunek tutaj
                        treasure_position = selected_square  # Zapamiętujemy pozycję skarbu
                        print("Treasure found!")  # Dodajemy komunikat
                    # Sprawdzamy, czy naciśnięta kratka odpowiada kolejnemu punktowi na liście b3
                    elif point_counter < len(b3) and selected_square == b3[point_counter]:
                        selected_squares.append(selected_square)  # Dodajemy naciśnięty punkt do listy
                        point_counter += 1  # Zwiększamy licznik
                        if selected_square in wrong_squares:  # Jeśli ten kwadrat był wcześniej zaznaczony jako błędny, usuń go
                            wrong_squares.remove(selected_square)
                    elif selected_square not in selected_squares and selected_square not in b3 and selected_square != \
                            c3[0]:  # Dodajemy dodatkowe sprawdzenie tutaj
                        print('nieprawidlowa pozycja')
                        wrong_squares.append(selected_square)

            if point_counter == len(b3) and event.type == pygame.MOUSEBUTTONDOWN and cross_drawn:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
                    row = location[0]
                    col = location[1]
                    selected_square = (row, col)
                    if selected_square == a3[0]:  # Nowy warunek tutaj
                        treasure_position = selected_square  # Zapamiętujemy pozycję skarbu
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                game.main_menu()

        pygame.display.update()


def Costam():
    return 1
