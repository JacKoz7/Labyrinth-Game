import pygame
from Board import GameState
from Button import Button
from Randomize import RandomizeButton, place_treasure, place_cross, generate_maze, place_random_point


# A class representing the First phase of the game
class First_Stage:
    # The constructor of the class, initializes basic attributes
    def __init__(self):
        self.treasure = (0, 0)  # The position of the treasure
        self.labyrinth = []  # A list storing the elements of the labyrinth
        self.cross = (0, 0)  # The position of the cross
        self.random_treasure = place_treasure()
        self.random_cross = place_cross(self.random_treasure)
        self.random_point = place_random_point(self.random_treasure, self.random_cross)
        self.maze = generate_maze(self.random_treasure, self.random_cross)
        # self.full_maze = generate_maze_points(self.rtreasure, self.rcross, self.rpoint, self.maze)

    # A method to return a font object of a specified size
    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    # A method to return the coordinates of the selected square
    def selected_square(self, location, mouse_x, mouse_y):
        if location is not None and (100 <= mouse_x <= 100 + 10 * 60 and 50 <= mouse_y <= 50 + 10 * 60):
            row = location[0]
            col = location[1]
            return row, col
        else:
            return None

    # A method responsible for gameplay
    def play(self, screen, txt, button_text):

        # Game logic
        treasure_drawn = False
        labyrinth_drawn = False
        cross_drawn = False
        random_treasure_drawn = False
        random_cross_drawn = False
        random_labyrinth_drawn = False

        show_step1 = True
        show_step2 = False
        show_step3 = False
        show_step4 = False
        random_mode = False

        show_next_move = False  # Whether to show the next move (when the labyrinth is already drawn)

        selected_treasure = None
        selected_cross = None

        must_restart = False

        board = GameState()  # Creating an instance of the GameState class

        # Loading images
        image_treasure = pygame.image.load('Images/red_circle1.png')
        image_labyrinth = pygame.image.load('Images/red_point1.png')
        image_cross = pygame.image.load('Images/red_krzyzyk1.png')

        img_undo = pygame.image.load('Images/return_button.png')
        img_return = pygame.image.load('Images/return.png')

        while True:

            player_mouse_pos = pygame.mouse.get_pos()

            location = board.draw_board(screen)

            # Drawing and displaying the steps of the game on the screen
            player_text = self.get_font(180).render(txt, True, 'Red')
            player_rect = player_text.get_rect(center=(1050, 100))
            screen.blit(player_text, player_rect)

            step1_text = self.get_font(50).render('1. Mark the treasure', True, 'Red')
            step1_rect = step1_text.get_rect(center=(1050, 300))

            step2_text = self.get_font(50).render('2. Draw the Labyrinth', True, 'Red')
            ste2_rect = step2_text.get_rect(center=(1050, 300))

            step3_text = self.get_font(50).render('3. Place the Cross', True, 'Red')
            ste3_rect = step2_text.get_rect(center=(1050, 300))

            step4_text = self.get_font(60).render(txt + ', try again!', True, 'Red')
            step4_rect = step1_text.get_rect(center=(1020, 230))

            # Creating and updating the button to return to the menu
            img_button = pygame.image.load('Images/empty_button.png')
            # randomizer_button_image = pygame.image.load(('Images/Randomizer_button.png'))

            menu_button = Button(image=img_button, pos=(1050, 600), text_input='Menu', font=self.get_font(65),
                                 base_color='Black',
                                 new_color='White')
            menu_button.ChangeColor(player_mouse_pos)
            menu_button.Update(screen)

            # Undo button
            undo_button = Button(image=img_undo, pos=(1290, 600), text_input='', font=self.get_font(65),
                                 base_color='Black',
                                 new_color='White')

            return_button = Button(image=img_return, pos=(1290, 600), text_input='', font=self.get_font(65),
                                   base_color='Black',
                                   new_color='White')

            # Randomize button (not working quite well)
            # randomize_button = RandomizeButton(image=randomizer_button_image, pos=(810,600))
            # randomize_button.ChangeColor(player_mouse_pos)
            # randomize_button.Update(screen)

            # Creating a button to move to the next Player / 2nd Stage of the game
            button_player2 = Button(image=img_button, pos=(1050, 480), text_input=button_text, font=self.get_font(65),
                                    base_color='Black',
                                    new_color='White')

            # Displaying the appropriate steps on the screen depending on the state of the game
            if show_step1:
                screen.blit(step1_text, step1_rect)
            if show_step2:
                screen.blit(step2_text, ste2_rect)
            if show_step3:
                screen.blit(step3_text, ste3_rect)
            if show_step4:
                screen.blit(step4_text, step4_rect)

            # Displaying the button to move to the next Player / 2nd Stage of the game
            if show_next_move:
                button_player2.ChangeColor(player_mouse_pos)
                button_player2.Update(screen)

            # Drawing the treasure, labyrinth, and cross on the board depending on the state of the game
            if treasure_drawn:
                row, col = selected_treasure
                screen.blit(image_treasure, (102 + col * 60, 52 + row * 60))

            if labyrinth_drawn:
                for square in self.labyrinth:
                    if square != selected_cross and square != selected_treasure:
                        row, col = square
                        screen.blit(image_labyrinth, (102 + col * 60, 52 + row * 60))

                        if 1 < len(self.labyrinth) <= 36:
                            return_button.ChangeColorImage(player_mouse_pos)

                            undo_button.Update(screen)
                            return_button.Update(screen)

            if random_labyrinth_drawn:
                for square in self.maze:
                    if square != place_cross(place_treasure()) and square != place_treasure():
                        row, col = square
                        screen.blit(image_labyrinth, (102 + col * 60, 52 + row * 60))

                    return_button.ChangeColorImage(player_mouse_pos)

                    undo_button.Update(screen)
                    return_button.Update(screen)
                    # for square1 in self.maze1:
                    #     row, col = square1
                    #     screen.blit(image_labyrinth, (102 + col * 60, 52 + row * 60))

            if cross_drawn:
                row, col = selected_cross
                screen.blit(image_cross, (102 + col * 60, 52 + row * 60))

            if random_cross_drawn:
                row, col = self.random_cross
                screen.blit(image_cross, (102 + col * 60, 52 + row * 60))

            if random_treasure_drawn:
                row, col = self.random_treasure
                screen.blit(image_treasure, (102 + col * 60, 52 + row * 60))

            # Event handling
            for event in pygame.event.get():

                # Reset the game if the player does not place the cross on the edge or corner
                if must_restart:
                    self.treasure = []
                    self.labyrinth = []

                    treasure_drawn = False
                    labyrinth_drawn = False

                    show_step1 = True
                    show_step2 = False
                    show_step3 = False
                    show_step4 = True

                    selected_treasure = None
                    selected_cross = None

                    must_restart = False

                if random_mode:  # randomize
                    self.treasure = []
                    self.labyrinth = []
                    self.cross = []
                    labyrinth_drawn = False
                    treasure_drawn = False
                    cross_drawn = False
                    random_treasure_drawn = True
                    random_cross_drawn = True
                    random_labyrinth_drawn = True
                    show_next_move = True
                    show_step1 = False
                    show_step2 = False
                    show_step3 = False
                    selected_treasure = None

                # Drawing the Treasure
                # Upon clicking the mouse and if no treasure has been previously drawn
                if event.type == pygame.MOUSEBUTTONDOWN and not treasure_drawn:

                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get the mouse position

                    # Get the position of the treasure
                    selected_treasure = self.selected_square(location, mouse_x, mouse_y)

                    # If the selected treasure is not empty, draw the treasure as drawn and move to the next step
                    if selected_treasure is not None:
                        treasure_drawn = True
                        show_step1 = False
                        show_step2 = True

                        # Add the treasure to the labyrinth
                        self.labyrinth.append(selected_treasure)
                    # print(selected_treasure)

                # Drawing the labyrinth
                if event.type == pygame.MOUSEBUTTONDOWN and treasure_drawn and len(self.labyrinth) < 37:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    selected_labyrinth = self.selected_square(location, mouse_x, mouse_y)

                    # If the selected labyrinth fragment is not empty
                    if selected_labyrinth is not None:

                        # If the selected labyrinth fragment is adjacent to another fragment, add it to the labyrinth
                        for last_square in self.labyrinth:
                            if selected_labyrinth == (last_square[0] - 1, last_square[1]) or \
                                    selected_labyrinth == (last_square[0] + 1, last_square[1]) or \
                                    selected_labyrinth == (last_square[0], last_square[1] - 1) or \
                                    selected_labyrinth == (last_square[0], last_square[1] + 1):

                                # To avoid adding the selected square and treasure to the labyrinth again
                                if selected_labyrinth not in self.labyrinth and selected_labyrinth != self.labyrinth[0]:
                                    self.labyrinth.append(selected_labyrinth)
                                    break  # break the loop if a matching square is found

                        labyrinth_drawn = True

                        # If the labyrinth is full, move to the next step
                        if len(self.labyrinth) == 36:
                            show_step2 = False
                            show_step3 = True

                # Drawing the cross
                if event.type == pygame.MOUSEBUTTONDOWN and treasure_drawn and len(
                        self.labyrinth) == 37 and not cross_drawn:

                    # Check if the selected square is on the edge
                    if location[0] == 0 or location[0] == 9 or location[1] == 0 or location[1] == 9:

                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        selected_cross = self.selected_square(location, mouse_x, mouse_y)

                        # If the selected cross is not empty,
                        # end the drawing process and save the positions of the treasure and cross
                        if selected_cross is not None:

                            cross_drawn = True
                            show_step3 = False
                            show_step4 = False

                            self.treasure = self.labyrinth[0]
                            self.cross = self.labyrinth[-1]

                            show_next_move = True
                    else:
                        # If the cross is not drawn on the edge, reset the game
                        cross_drawn = False
                        must_restart = True

                # Return to the main menu
                if event.type == pygame.MOUSEBUTTONDOWN and menu_button.CheckForInput(player_mouse_pos):
                    from Main import Labirynt
                    game = Labirynt()
                    game.main_menu()

                # Undo button
                if event.type == pygame.MOUSEBUTTONDOWN and undo_button.CheckForInput(player_mouse_pos) and \
                        return_button.CheckForInput(player_mouse_pos) and 1 < len(self.labyrinth) <= 36:

                    self.labyrinth.pop(-1)

                    if len(self.labyrinth) <= 36:
                        show_step3 = False
                        show_step2 = True

                # Undo button after pressing the random button
                if event.type == pygame.MOUSEBUTTONDOWN and undo_button.CheckForInput(player_mouse_pos) and \
                        return_button.CheckForInput(player_mouse_pos) and random_mode:

                    self.random_treasure = None
                    self.random_cross = None
                    self.random_point = None
                    self.maze = None
                    random_treasure_drawn = False
                    random_cross_drawn = False
                    random_labyrinth_drawn = False
                    show_next_move = False
                    show_step1 = True
                    random_mode = False

                # # Randomize button todo
                # if event.type == pygame.MOUSEBUTTONDOWN and randomize_button.CheckForInput(player_mouse_pos):
                #
                #     random_mode = True
                #     self.random_treasure = place_treasure()
                #     self.random_cross = place_cross(self.random_treasure)
                #     self.random_point = place_random_point(self.random_treasure, self.random_cross)
                #     self.maze = generate_maze(self.random_treasure, self.random_cross)
                #     # self.full_maze = generate_maze_points(self.rtreasure, self.rcross, self.rpoint, self.maze)
                #
                #     print(self.random_treasure)
                #     print(self.random_cross)
                #     print(self.random_point)
                #     print(self.maze)
                #     # print(self.full_maze)

                # Move to the next Player / to the 2nd Stage of the Game
                if show_next_move:
                    if event.type == pygame.MOUSEBUTTONDOWN and button_player2.CheckForInput(player_mouse_pos) and random_mode:
                        self.labyrinth = self.maze
                        self.cross = self.random_cross
                        self.treasure = self.random_treasure
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN and button_player2.CheckForInput(player_mouse_pos) and not random_mode:
                        return

                # Closing the game
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Pygame
                    exit()  # End the program

            pygame.display.update()  # Update the displayed game graphics
