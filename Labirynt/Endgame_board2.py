import pygame
from General import Labirynt
from Button import button1
from Board import GameState

def get_font(size):
    return pygame.font.Font('Ancient Medium.ttf', size)

def get_neighbours(position):
    row, col = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbours = [(row + dr, col + dc) for dr, dc in directions]
    return neighbours
#
def player2_endgame(a3, b3, c3, e4, screen):  # parametry a b c to wspolrzedne skarbu labiryntu i krzyzyka z planszy gracza 1
    print('wspolrzedne drugiego gracza')

    print(a3)
    print(b3)
    print(c3)


    #Dane do zapisania
    cross_drawn = True

    wrong_squares = []
    znaleziony_labiryt = []

    counter = 0  # licznik poprawnych zgadnięć
    treasure_position = False

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

        BOARD.draw_small_board(screen, counter, tick_image)

        gracz1_text = get_font(180).render('Gracz 2', True, 'Red')
        gracz1_rect = gracz1_text.get_rect(center=(1050, 100))
        screen.blit(gracz1_text, gracz1_rect)

        way_text = get_font(50).render('Odnajdz droge do skarbu gracza 1', True, 'Red')
        way_rect = gracz1_text.get_rect(center=(1000, 300))
        screen.blit(way_text, way_rect)

        if cross_drawn:
            loc1, loc2 = c3[0]
            screen.blit(image_krzyzyk, (102 + loc2 * 60, 52 + loc1 * 60))

        # Rysowanie scian
        for square in wrong_squares:
            loc1, loc2 = square
            screen.blit(image_wall, (102 + loc2 * 60, 52 + loc1 * 60))

        # Draw the treasure after the walls
        if treasure_position:
            loc1, loc2 = a3[0]
            screen.blit(image_treasure, (102 + loc2 * 60, 52 + loc1 * 60))

        for square in znaleziony_labiryt:
            loc1, loc2 = square
            screen.blit(image_point, (102 + loc2 * 60, 52 + loc1 * 60))

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

                    # Czy wybrana kratka jest skarbem i czy jest sąsiadująca z jakąkolwiek kratką labiryntu
                    if selected_square == a3[0] and any(
                            neighbour in znaleziony_labiryt for neighbour in get_neighbours(selected_square)):
                        treasure_position = True  # Zmieniamy flagę wskazującą na znalezienie skarbu
                        continue  # Przechodzimy do następnego zdarzenia

                    # Czy wybrana kratka jest sąsiadująca z ostatnią wybraną kratką labiryntu,
                    # nie jest ścianą i nie jest krzyżykiem
                    if znaleziony_labiryt and selected_square not in b3 and selected_square != c3[0] and any(
                            neighbour == znaleziony_labiryt[-1] for neighbour in get_neighbours(selected_square)):
                        wrong_squares.append(selected_square) # Dodajemy kratkę do listy niewłaściwych ruchów

                    elif selected_square in b3:  # Czy wybrana kratka jest w liście poprawnych kwadratów
                        # Czy wybrana kratka jest sąsiadująca z którąkolwiek z już wybranych
                        if not znaleziony_labiryt or any(
                                neighbour in znaleziony_labiryt for neighbour in get_neighbours(selected_square)):
                            if selected_square not in znaleziony_labiryt:  # Czy kratka nie jest już częścią labiryntu
                                znaleziony_labiryt.append(selected_square) # Dodajemy kratkę do labiryntu
                                counter += 1 # Dodajemy kratkę do labiryntu

                            # skracanie ścieżki, jeżeli ostatnia wybrana kratka nie jest sąsiadująca z żadną ścianą
                            while znaleziony_labiryt and not any(
                                    neighbour in b3 for neighbour in get_neighbours(znaleziony_labiryt[-1])):
                                znaleziony_labiryt.pop()

                    else:
                        # Czy wybrana kratka jest sąsiadująca z którąkolwiek z kratek labiryntu i nie jest krzyżykiem
                        if selected_square != c3[0] and any(neighbour in znaleziony_labiryt for neighbour in
                                                            get_neighbours(selected_square)):
                            wrong_squares.append(selected_square)

                        # Pozwolenie na umieszczenie ściany obok krzyżyka
                        elif c3[0] in get_neighbours(selected_square) and selected_square not in b3:
                            wrong_squares.append(selected_square)


            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                game.main_menu()

        pygame.display.update()