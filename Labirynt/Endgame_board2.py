import pygame
from General import Labirynt
from Button import button1
from Board import GameState
from PlayerState import PlayerState

def get_font(size):
    return pygame.font.Font('Ancient Medium.ttf', size)

def get_neighbours(position):
    row, col = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbours = [(row + dr, col + dc) for dr, dc in directions]
    return neighbours

def player2_endgame(a3, b3, c3,
                    screen):  # parametry a b c to wspolrzedne skarbu labiryntu i krzyzyka z planszy gracza 2
    print('wspolrzedne drugiego gracza')

    """
    from Endgame_board1 import player1_endgame
    from Main import a, b, c
    """

    print(a3)
    print(b3)
    print(c3)


    #Dane do zapisania
    cross_drawn = True
    wrong_squares = []
    znaleziony_labiryt = []
    counter = 0  # licznik poprawnych zgadnięć
    treasure_position = None

    """
    player2_state = PlayerState()
    game_switch = False
    """

    game = Labirynt()
    BOARD = GameState()
    image_treasure = pygame.image.load('red_circle1.png')
    image_krzyzyk = pygame.image.load('red_krzyzyk1.png')
    image_point = pygame.image.load('red_point1.png')
    image_wall = pygame.image.load('wall.png')
    tick_image = pygame.image.load('green_tick.png')

    while True:

        """
        if game_switch:  # Jeśli gra powinna przejść do gracza 1
            cross_drawn = True
            wrong_squares = player2_state.wrong_squares
            znaleziony_labiryt = player2_state.znaleziony_labiryt
            counter = player2_state.counter
            treasure_position = player2_state.treasure_position
            game_switch = False  # Reset flagi
        """

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
        if treasure_position is not None:
            loc1, loc2 = treasure_position
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

                    # Add a wall if the selected square is not part of the maze but is a neighbour of the start
                    if selected_square not in b3 and any(
                            neighbour == c3[0] for neighbour in get_neighbours(selected_square)):
                        wrong_squares.append(selected_square)

                    if selected_square in b3:
                        # sprawdzanie, czy wybrana kratka jest sąsiadująca z którąkolwiek z już wybranych
                        if not znaleziony_labiryt or any(
                                neighbour in znaleziony_labiryt for neighbour in get_neighbours(selected_square)):
                            znaleziony_labiryt.append(selected_square)
                            counter += 1
                            # skracanie ścieżki
                            while znaleziony_labiryt and not any(
                                    neighbour in b3 for neighbour in get_neighbours(znaleziony_labiryt[-1])):
                                znaleziony_labiryt.pop()
                            if counter == 5:
                                #Tutaj gamestate
                                break
                    else:
                        # sprawdzanie, czy wybrana kratka jest sąsiadująca z którąkolwiek z kratek labiryntu
                        if selected_square != a3[0] and any(neighbour in znaleziony_labiryt for neighbour
                                                            in get_neighbours(selected_square)):
                            wrong_squares.append(selected_square)

                            """
                            # Zapisanie stanu gry gracza 1
                            cross_drawn = False
                            player2_state.wrong_squares = wrong_squares
                            player2_state.znaleziony_labiryt = znaleziony_labiryt
                            player2_state.counter = counter
                            player2_state.treasure_position = treasure_position

                            player1_endgame(a, b, c, screen)
                            game_switch = True  # Ustawienie flagi na true, aby gracz 1 mógł kontynuować grę
                            break
                            """

                    # Check if the selected square is the treasure
                    if selected_square == a3[0]:
                        treasure_position = selected_square

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                game.main_menu()

        pygame.display.update()