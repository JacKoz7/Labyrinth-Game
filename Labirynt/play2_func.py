import pygame
from Board import GameState
from Button import button1
from General import Labirynt
from cords import Player
from Endgame_board1 import player1_endgame

x = None
y = None
z = None

def get_font(size):
    return pygame.font.Font('Ancient Medium.ttf', size)
def play2(screen, txt):
    global x, y, z

    game = Labirynt()     #utworzenie obiektu game z pliku Main
    skarb_drawn = False
    krzyzyk_drawn = False
    labirynt_drawn = False

    show_step1 = True
    show_step2 = False
    show_step3 = False
    show_step4 = False

    selected_square = None
    selected_squares = []
    selected_squareX = None

    must_restart = False

    BOARD = GameState()

    image_treasure = pygame.image.load('red_circle1.png')
    image_labyrinth = pygame.image.load('red_point1.png')
    image_krzyzyk = pygame.image.load('red_krzyzyk1.png')

    gracz1_skarb = []
    labirynt_temp = []
    cross_cords2 = []

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        BOARD.draw_board(screen)
        location = BOARD.draw_board(screen)

        gracz1_text = get_font(180).render(txt, True, 'Red')
        gracz1_rect = gracz1_text.get_rect(center=(1050, 100))
        screen.blit(gracz1_text, gracz1_rect)

        step1_text = get_font(50).render('1. Zaznacz skarb', True, 'Red')
        step1_rect = step1_text.get_rect(center=(1050, 300))

        step2_text = get_font(50).render('2. Narysuj Labirynt', True, 'Red')
        ste2_rect = step2_text.get_rect(center=(1050, 300))

        step3_text = get_font(50).render('3. Ustaw Krzyzyk', True, 'Red')
        ste3_rect = step2_text.get_rect(center=(1050, 300))

        step4_text = get_font(60).render(txt + ', spróbuj ponownie!', True, 'Red')
        step4_rect = step1_text.get_rect(center=(900, 230))

        if show_step1:
            screen.blit(step1_text, step1_rect)
        if show_step2:
            screen.blit(step2_text, ste2_rect)
        if show_step3:
            screen.blit(step3_text, ste3_rect)
        if show_step4:
            screen.blit(step4_text, step4_rect)

        if skarb_drawn:
            row, col = selected_square
            screen.blit(image_treasure, (102 + col * 60, 52 + row * 60))

        if labirynt_drawn:
            for square in selected_squares:
                if square != selected_squareX:
                    row, col = square
                    screen.blit(image_labyrinth, (102 + col * 60, 52 + row * 60))

        if krzyzyk_drawn:
            row, col = selected_squareX
            screen.blit(image_krzyzyk, (102 + col * 60, 52 + row * 60))

        img = pygame.image.load('empty_button.png')

        button_back = button1(image=img, pos=(1050, 600), text_input='Powrót', font=get_font(65), base_color='Black',
                              new_color='White')
        button_back.ChangeColor(play_mouse_pos)
        button_back.update(screen)

        for event in pygame.event.get():

            # ustawienie wartosci do domyślnej wartości
            if must_restart:
                skarb_drawn = False
                krzyzyk_drawn = False
                labirynt_drawn = False

                show_step1 = True
                show_step3 = False
                show_step2 = False
                show_step4 = True

                selected_square = None
                selected_squares = []
                selected_squareX = None

                gracz1_skarb = []
                labirynt_temp = []
                must_restart = False

            # Szkicowanie Skarbu
            if event.type == pygame.MOUSEBUTTONDOWN and not skarb_drawn:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
                    row = location[0]
                    col = location[1]

                    selected_square = (row, col)
                    skarb_drawn = True
                    show_step1 = False
                    show_step2 = True

                    gracz1_skarb.append(selected_square)
                    labirynt_temp.append(selected_square)  # Dodanie skarbu dla pozniejszegio warunku!

            # Szkicowanie labiryntu
            if event.type == pygame.MOUSEBUTTONDOWN and skarb_drawn and len(selected_squares) < 35:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
                    row = location[0]
                    col = location[1]

                    # Mozliwosc ustawienia kwadratow
                    if len(selected_squares) == 0:
                        # sprawdź, czy aktualnie wybrany kwadrat sąsiaduje z kwadratem skarbu
                        if (row, col) == (gracz1_skarb[0][0] - 1, gracz1_skarb[0][1]) or \
                                (row, col) == (gracz1_skarb[0][0] + 1, gracz1_skarb[0][1]) or \
                                (row, col) == (gracz1_skarb[0][0], gracz1_skarb[0][1] - 1) or \
                                (row, col) == (gracz1_skarb[0][0], gracz1_skarb[0][1] + 1):
                            selected_squares.append((row, col))
                            labirynt_temp.append((row, col))

                            # sprawdź, czy aktualnie wybrany kwadrat sąsiaduje z poprzednim kwadratem na liście
                            # last_square = selected_squares[-1] zamiast petli
                    else:
                        # sprawdź, czy aktualnie wybrany kwadrat sąsiaduje z dowolnym kwadratem z listy
                        for last_square in selected_squares:
                            if (row, col) == (last_square[0] - 1, last_square[1]) or \
                                    (row, col) == (last_square[0] + 1, last_square[1]) or \
                                    (row, col) == (last_square[0], last_square[1] - 1) or \
                                    (row, col) == (last_square[0], last_square[1] + 1):
                                if (row, col) not in selected_squares and (row, col) != gracz1_skarb[0]:
                                    selected_squares.append((row, col))
                                    labirynt_temp.append((row, col))
                                    break  # przerwij pętlę, jeżeli znaleźliśmy pasujący kwadrat

                    labirynt_drawn = True
                    # Logika sprawdzania czy jest labirynt zamkniety

                    # sprawdź, czy dany kwadrat zablokował drogę do celu
                    # Rownierz, sprawdzenie czy skarb nie zablokował drogę do celu (wczesniej labirynt temp)
                    blocked = False
                    if len(selected_squares) > 1:
                        last_square = selected_squares[-1]
                        if (last_square[0] + 1, last_square[1]) in labirynt_temp and \
                                (last_square[0] - 1, last_square[1]) in labirynt_temp and \
                                (last_square[0], last_square[1] + 1) in labirynt_temp and \
                                (last_square[0], last_square[1] - 1) in labirynt_temp:
                            blocked = True

                    # Czy jest zablokowany na brzegu
                    if row == 0 and (row + 1, col) in labirynt_temp and \
                            (row, col + 1) in labirynt_temp and (row, col - 1) in labirynt_temp:
                        blocked = True
                    elif row == 9 and (row - 1, col) in labirynt_temp and \
                            (row, col + 1) in labirynt_temp and (row, col - 1) in labirynt_temp:
                        blocked = True
                    elif col == 0 and (row + 1, col) in labirynt_temp and \
                            (row - 1, col) in labirynt_temp and (row, col + 1) in labirynt_temp:
                        blocked = True
                    elif col == 9 and (row + 1, col) in labirynt_temp and \
                            (row - 1, col) in labirynt_temp and (row, col - 1) in labirynt_temp:
                        blocked = True

                    # Czy jest zablokowany w rogu
                    if row == 0 and col == 0 and (row + 1, col) in labirynt_temp and \
                            (row, col + 1) in labirynt_temp:
                        blocked = True
                    elif row == 0 and col == 9 and (row + 1, col) in labirynt_temp and \
                            (row, col - 1) in labirynt_temp:
                        blocked = True
                    elif row == 9 and col == 0 and (row - 1, col) in labirynt_temp and \
                            (row, col + 1) in labirynt_temp:
                        blocked = True
                    elif row == 9 and col == 9 and (row - 1, col) in labirynt_temp and \
                            (row, col - 1) in labirynt_temp:
                        blocked = True

                    if blocked:
                        print("The path is blocked. Please start over.")
                        must_restart = True

                    if len(selected_squares) == 34:
                        show_step2 = False
                        show_step3 = True

            # Szkicowanie krzyzyka
            if event.type == pygame.MOUSEBUTTONDOWN and skarb_drawn and len(
                    selected_squares) == 35 and not krzyzyk_drawn:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
                    row = location[0]
                    col = location[1]

                    # sprawdź, czy wybrany kwadrat jest na brzegu
                    if (row == 0 or row == 9 or col == 0 or col == 9):
                        selected_squareX = (row, col)
                        krzyzyk_drawn = True
                        show_step3 = False
                        show_step4 = False

                        cross_cords2.append(selected_squares[-1])
                        points2 = Player(gracz1_skarb, selected_squares[:-1], cross_cords2)
                        points2.print()     #wywołanie metody obiektu zwracającego współrzędne wszystkich punktów
                        x, y, z = points2.return_treasure(), points2.return_way35(), points2.return_cross()
                        player1_endgame(x, y, z, screen)     #parametry wspolrzednych z play_func2

                    else:
                        selected_squareX = (row, col)
                        krzyzyk_drawn = True
                        must_restart = True

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                game.main_menu()

        pygame.display.update()


