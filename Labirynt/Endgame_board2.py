import pygame #

from Board import GameState
from Button import button1


class Game_status:
    def __init__(self, walls, found_labyrinth, winner):
        self.walls = walls
        self.found_labyrinth = found_labyrinth  # Znaleziony labirynt
        self.winner = winner


class Second_Stage:
    def __init__(self, treasure, labyrinth, cross):
        self.treasure = treasure
        self.labyrinth = labyrinth
        self.cross = cross
        self.correct_squares = [cross]

    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    def get_neighbours(self, position):
        row, col = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbours = [(row + dr, col + dc) for dr, dc in directions]
        return neighbours

    def endgame(self, screen, txt, txt2, walls, labyrinth_temp, winner):

        cross_drawn = True
        treasure_drawn = False
        counter = 0

        BOARD = GameState()

        image_treasure = pygame.image.load('red_circle1.png')
        image_krzyzyk = pygame.image.load('red_krzyzyk1.png')
        image_point = pygame.image.load('red_point1.png')
        image_wall = pygame.image.load('wall.png')

        img = pygame.image.load('empty_button.png')

        winner_button = button1(image=img, pos=(1050, 500), text_input="Powrót", font=self.get_font(65),
                                base_color='Black',
                                new_color='White')

        while True:

            play_mouse_pos = pygame.mouse.get_pos()
            location = BOARD.draw_board(screen)

            BOARD.draw_small_board(screen, counter)  # Szkicowanie zielonych green ticków

            gracz1_text = self.get_font(180).render(txt, True, 'Red')
            gracz1_rect = gracz1_text.get_rect(center=(1050, 100))
            screen.blit(gracz1_text, gracz1_rect)

            way_text = self.get_font(50).render(txt + ', odnajdz droge do skarbu ' + txt2, True, 'Red')
            way_rect = gracz1_text.get_rect(center=(1000, 300))

            if winner is False:
                screen.blit(way_text, way_rect)

            winner_text = self.get_font(50).render('Witam ' + txt + ' wygrałeś/aś :)', True, 'Red')
            winner_rect = winner_text.get_rect(center=(1050, 300))

            if cross_drawn:
                loc1, loc2 = self.cross
                screen.blit(image_krzyzyk, (102 + loc2 * 60, 52 + loc1 * 60))

            # Rysowanie scian
            for square in walls:
                loc1, loc2 = square
                screen.blit(image_wall, (102 + loc2 * 60, 52 + loc1 * 60))

            # Draw the treasure after the walls
            if treasure_drawn:
                loc1, loc2 = self.treasure
                screen.blit(image_treasure, (102 + loc2 * 60, 52 + loc1 * 60))

            for square in labyrinth_temp:
                loc1, loc2 = square
                if square != self.cross and square != self.treasure:
                    screen.blit(image_point, (102 + loc2 * 60, 52 + loc1 * 60))

            if winner:
                screen.blit(winner_text, winner_rect)

                winner_button.ChangeColor(play_mouse_pos)
                winner_button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and cross_drawn:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
                        row = location[0]
                        col = location[1]

                        selected_square = (row, col)
                        print(selected_square)

                        if any(selected_square in self.get_neighbours(correct_square) for correct_square in
                               self.correct_squares) and winner is False:
                            # If the chosen square is next to any correct square
                            if selected_square in self.labyrinth:  # and is a correct move
                                if selected_square not in self.correct_squares:
                                    labyrinth_temp.append(selected_square)
                                    self.correct_squares.append(selected_square)
                                    counter += 1

                                if counter == 5 and selected_square != self.treasure:
                                    return

                                elif counter == 4 and selected_square == self.treasure:
                                    counter += 1

                                if selected_square == self.treasure:
                                    treasure_drawn = True
                                    winner = True

                            else:
                                # If the chosen square is next to any correct square, but is not a correct move
                                if selected_square not in walls:
                                    walls.append(selected_square)
                                    return

                if event.type == pygame.MOUSEBUTTONDOWN and winner_button.CheckForInput(play_mouse_pos):
                    from General import Labirynt
                    game = Labirynt()
                    game.main_menu()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
