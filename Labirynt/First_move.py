import pygame #
from Board import GameState
from Button import button1

class First_Stage:
    def __init__(self):
        self.treasure = (0, 0)
        self.labyrinth = []
        self.cross = (0, 0)

    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    def selected_square(self, location, mouse_x, mouse_y):
        if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
            row = location[0]
            col = location[1]
            return row, col
        else:
            return None

    def play(self, screen, txt, ButtonText):

        treasure_drawn = False
        labyrinth_drawn = False
        cross_drawn = False

        show_step1 = True
        show_step2 = False
        show_step3 = False
        show_step4 = False

        show_next_move = False

        selected_treasure = None
        selected_cross = None

        must_restart = False

        BOARD = GameState()

        image_treasure = pygame.image.load('red_circle1.png')
        image_labyrinth = pygame.image.load('red_point1.png')
        image_cross = pygame.image.load('red_krzyzyk1.png')

        img = pygame.image.load('empty_button.png')

        button_player2 = button1(image=img, pos=(1050, 500), text_input=ButtonText, font=self.get_font(65),
                                 base_color='Black',
                                 new_color='White')

        while True:
            play_mouse_pos = pygame.mouse.get_pos()

            BOARD.draw_board(screen)
            location = BOARD.draw_board(screen)

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

            # Powrót
            img = pygame.image.load('empty_button.png')

            button_back = button1(image=img, pos=(1050, 600), text_input='Powrót', font=self.get_font(65),
                                  base_color='Black',
                                  new_color='White')
            button_back.ChangeColor(play_mouse_pos)
            button_back.update(screen)
#
            if show_step1:
                screen.blit(step1_text, step1_rect)
            if show_step2:
                screen.blit(step2_text, ste2_rect)
            if show_step3:
                screen.blit(step3_text, ste3_rect)
            if show_step4:
                screen.blit(step4_text, step4_rect)

            if show_next_move:

                button_player2.ChangeColor(play_mouse_pos)
                button_player2.update(screen)

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

            for event in pygame.event.get():

                # ustawienie wartosci do domyślnej wartości
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

                # Szkicowanie Skarbu
                if event.type == pygame.MOUSEBUTTONDOWN and not treasure_drawn:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    selected_treasure = self.selected_square(location, mouse_x, mouse_y)

                    if selected_treasure is not None:
                        treasure_drawn = True
                        show_step1 = False
                        show_step2 = True

                        self.labyrinth.append(selected_treasure)  # Dodanie skarbu dla pozniejszegio warunku!

                # Szkicowanie labiryntu
                if event.type == pygame.MOUSEBUTTONDOWN and treasure_drawn and len(self.labyrinth) < 37:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    selected_labyrinth = self.selected_square(location, mouse_x, mouse_y)

                    if selected_labyrinth is not None:
                        # sprawdź, czy aktualnie wybrany kwadrat sąsiaduje z dowolnym kwadratem z listy
                        for last_square in self.labyrinth:
                            if selected_labyrinth == (last_square[0] - 1, last_square[1]) or \
                                    selected_labyrinth == (last_square[0] + 1, last_square[1]) or \
                                    selected_labyrinth == (last_square[0], last_square[1] - 1) or \
                                    selected_labyrinth == (last_square[0], last_square[1] + 1):
                                if selected_labyrinth not in self.labyrinth and selected_labyrinth != self.labyrinth[0]:
                                    self.labyrinth.append(selected_labyrinth)
                                    break  # przerwij pętlę, jeżeli znaleźliśmy pasujący kwadrat

                        labyrinth_drawn = True

                        if len(self.labyrinth) == 36:
                            show_step2 = False
                            show_step3 = True

                # Szkicowanie krzyzyka
                if event.type == pygame.MOUSEBUTTONDOWN and treasure_drawn and len(
                        self.labyrinth) == 37 and not cross_drawn:

                    # sprawdź, czy wybrany kwadrat jest na brzegu
                    if location[0] == 0 or location[0] == 9 or location[1] == 0 or location[1] == 9:

                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        selected_cross = self.selected_square(location, mouse_x, mouse_y)

                        if selected_cross is not None:
                            cross_drawn = True
                            show_step3 = False
                            show_step4 = False

                            self.treasure = self.labyrinth[
                                0]  # Zapisanie skarbu oraz krzyżyka, gdy labirynt jest spełniony
                            self.cross = self.labyrinth[-1]

                            show_next_move = True
                            print('rozpoczela sie nowa gra')
                    else:
                        cross_drawn = False
                        must_restart = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                    from General import Labirynt
                    game = Labirynt()
                    game.main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN and button_player2.CheckForInput(play_mouse_pos):
                    return

            pygame.display.update()