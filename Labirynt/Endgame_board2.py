import pygame

from Board import GameState
from Button import button1


class Game_status:
    def __init__(self, walls, labyrinth_temp, counter):
        self.walls = walls
        self.labyrinth_temp = labyrinth_temp # Znaleziony labirynt
        self.counter = counter # licznik poprawnych zgadnięć

class Second_Stage:
    def __init__(self, treasure, labyrinth, cross):
        self.treasure = treasure
        self.labyrinth = labyrinth
        self.cross = cross

    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    def get_neighbours(self, position):
        row, col = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbours = [(row + dr, col + dc) for dr, dc in directions]
        return neighbours

    def endgame(self, screen, txt, walls, labyrinth_temp, counter):

        # Dane do zapisania
        cross_drawn = True
        treasure_position = False

        BOARD = GameState()

        image_treasure = pygame.image.load('red_circle1.png')
        image_krzyzyk = pygame.image.load('red_krzyzyk1.png')
        image_point = pygame.image.load('red_point1.png')
        image_wall = pygame.image.load('wall.png')
        tick_image = pygame.image.load('green_tick.png')

        while True:

            play_mouse_pos = pygame.mouse.get_pos()
            location = BOARD.draw_board(screen)

            # BOARD.draw_small_board(screen, counter, tick_image)  #Szkicowanie zielonych green ticków

            gracz1_text = self.get_font(180).render(txt, True, 'Red')
            gracz1_rect = gracz1_text.get_rect(center=(1050, 100))
            screen.blit(gracz1_text, gracz1_rect)

            way_text = self.get_font(50).render('Odnajdz droge do skarbu ' + txt, True, 'Red')
            way_rect = gracz1_text.get_rect(center=(1000, 300))
            screen.blit(way_text, way_rect)

            if cross_drawn:
                loc1, loc2 = self.cross[0]
                screen.blit(image_krzyzyk, (102 + loc2 * 60, 52 + loc1 * 60))

            # Rysowanie scian
            for square in walls:
                loc1, loc2 = square
                screen.blit(image_wall, (102 + loc2 * 60, 52 + loc1 * 60))

            # Draw the treasure after the walls
            if treasure_position:
                loc1, loc2 = self.treasure
                screen.blit(image_treasure, (102 + loc2 * 60, 52 + loc1 * 60))

            for square in labyrinth_temp:
                loc1, loc2 = square
                screen.blit(image_point, (102 + loc2 * 60, 52 + loc1 * 60))

            img = pygame.image.load('empty_button.png')
            button_back = button1(image=img, pos=(1050, 600), text_input='Menu', font=self.get_font(65),
                                  base_color='Black', new_color='White')
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
                        #
                        # Czy wybrana kratka jest skarbem i czy jest sąsiadująca z jakąkolwiek kratką labiryntu
                        if selected_square == self.treasure and any(
                                neighbour in labyrinth_temp for neighbour in self.get_neighbours(selected_square)):
                            treasure_position = True  # Zmieniamy flagę wskazującą na znalezienie skarbu
                            continue  # Przechodzimy do następnego zdarzenia

                        # Czy wybrana kratka jest sąsiadująca z ostatnią wybraną kratką labiryntu,
                        # nie jest ścianą i nie jest krzyżykiem
                        if labyrinth_temp and selected_square not in self.labyrinth and selected_square != self.treasure and any(
                                neighbour == labyrinth_temp[-1] for neighbour in self.get_neighbours(selected_square)):
                            walls.append(selected_square)  # Dodajemy kratkę do listy niewłaściwych ruchów
                            return


                        elif selected_square in self.labyrinth:  # Czy wybrana kratka jest w liście poprawnych kwadratów

                            # Czy wybrana kratka jest sąsiadująca z którąkolwiek z już wybranych
                            if not labyrinth_temp or any(
                                    neighbour in labyrinth_temp for neighbour in self.get_neighbours(selected_square)):
                                if selected_square not in labyrinth_temp:  # Czy kratka nie jest już częścią labiryntu
                                    labyrinth_temp.append(selected_square)  # Dodajemy kratkę do labiryntu
                                    #counter += 1  #Zwiększamy ilość poprawnych kratek

                                   # if counter == 5:
                                      #  return

                                # skracanie ścieżki, jeżeli ostatnia wybrana kratka nie jest sąsiadująca z żadną ścianą
                                while labyrinth_temp and not any(
                                        neighbour in self.labyrinth for neighbour in
                                        self.get_neighbours(labyrinth_temp[-1])):
                                    labyrinth_temp.pop()

                        else:
                            # Czy wybrana kratka jest sąsiadująca z którąkolwiek z kratek labiryntu i nie jest krzyżykiem
                            if selected_square != self.cross and any(neighbour in labyrinth_temp for neighbour in
                                                                     self.get_neighbours(selected_square)):
                                walls.append(selected_square)
                                return

                            # Pozwolenie na umieszczenie ściany obok krzyżyka
                            elif self.cross in self.get_neighbours(
                                    selected_square) and selected_square not in self.labyrinth:
                                walls.append(selected_square)
                                return

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and button_back.CheckForInput(play_mouse_pos):
                    from General import Labirynt
                    game = Labirynt()
                    game.main_menu()

            pygame.display.update()
