import pygame
from src.Board import GameState
from src.Button import Button


# The Game_status class serves to store information for both Players
class Game_status:
    def __init__(self, walls, found_labyrinth, winner):
        self.walls = walls  # The walls encountered by the opponent
        self.found_labyrinth = (
            found_labyrinth  # The labyrinth discovered by the opponent
        )
        self.winner = winner  # The status of the victorious Player


# A class representing the Second phase of the game
class Second_Stage:
    # Constructor initializing with parameters
    def __init__(self, treasure, labyrinth, cross):
        self.treasure = treasure  # The position of the treasure
        self.labyrinth = (
            labyrinth  # A list containing the labyrinth's positions on the board
        )
        self.cross = cross  # The position of the cross
        self.correct_squares = [
            cross
        ]  # A list containing the correct squares, initially containing only the cross position

    # The 'get_font' method creates a font object of a specified size
    def get_font(self, size):
        return pygame.font.Font("../Ancient Medium.ttf", size)

    # The 'get_neighbors' method returns a list of neighbouring squares for a given position
    def get_neighbors(self, position):
        row, col = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = [(row + dr, col + dc) for dr, dc in directions]
        return neighbors

    # The 'endgame' method handles the endgame logic
    def endgame(self, screen, txt, txt2, walls, labyrinth_temp, winner):
        # Initialization of flags and variables
        cross_drawn = True
        counter = 0

        point = False
        wall = False
        pause = False

        # Initialization of the game state object
        board = GameState()

        # Loading images
        image_treasure = pygame.image.load("Images/red_circle1.png")
        image_cross = pygame.image.load("Images/red_krzyzyk1.png")
        image_point = pygame.image.load("Images/red_point1.png")
        image_wall = pygame.image.load("Images/wall.png")

        img_button = pygame.image.load("Images/empty_button.png")

        # Creating a button
        button_back = Button(
            image=img_button,
            pos=(1050, 600),
            text_input="Menu",
            font=self.get_font(65),
            base_color="Black",
            new_color="White",
        )

        # Main game loop
        while True:
            play_mouse_pos = pygame.mouse.get_pos()
            location = board.draw_board(screen)

            board.draw_small_board(screen, counter, wall)  # Sketching the green ticks

            # Drawing and displaying textual information on the screen
            player_text = self.get_font(180).render(txt, True, "Red")
            player_rect = player_text.get_rect(center=(1050, 100))
            screen.blit(player_text, player_rect)

            path_text = self.get_font(45).render(
                "Find the way to the opponent's treasure", True, "Red"
            )
            path_rect = player_text.get_rect(center=(990, 300))

            winner_text = self.get_font(70).render(f"{txt} Wins", True, "Red")
            winner_rect = winner_text.get_rect(center=(700, 185))

            congrats = self.get_font(160).render("Congratulations", True, "Red")
            congrats_rect = congrats.get_rect(center=(700, 80))

            button_back.ChangeColor(play_mouse_pos)  # Updating the 'back' button colour
            button_back.Update(screen)

            if winner is False:
                screen.blit(
                    path_text, path_rect
                )  # Displaying text if there is no winner

            # Drawing the cross, walls, and treasure on the board depending on the game state
            if cross_drawn:
                loc1, loc2 = self.cross
                screen.blit(image_cross, (102 + loc2 * 60, 52 + loc1 * 60))

            for square in walls:
                loc1, loc2 = square
                screen.blit(image_wall, (102 + loc2 * 60, 52 + loc1 * 60))

            for square in labyrinth_temp:
                loc1, loc2 = square
                if square != self.cross and square != self.treasure:
                    screen.blit(image_point, (102 + loc2 * 60, 52 + loc1 * 60))

            # Pausing the game to observe the last wall and labyrinth square
            if point or wall:
                pygame.time.delay(800)
                return

            if pause:  # Pausing the game to observe the found treasure
                pygame.time.delay(2000)
                pause = False

            if winner:  # If there is a winner
                screen.fill("black")  # Filling the screen with black
                bg = pygame.image.load("Images/game_background.png")
                screen.blit(bg, (0, 0))

                screen.blit(winner_text, winner_rect)  # Displaying the winner text
                screen.blit(congrats, congrats_rect)

                # Creating menu and play again buttons
                winner_button_menu = Button(
                    image=img_button,
                    pos=(700, 500),
                    text_input="Menu",
                    font=self.get_font(65),
                    base_color="Black",
                    new_color="White",
                )
                play_again_button = Button(
                    image=img_button,
                    pos=(700, 350),
                    text_input="Play Again",
                    font=self.get_font(65),
                    base_color="Black",
                    new_color="White",
                )

                # Updating buttons
                winner_button_menu.ChangeColor(play_mouse_pos)
                winner_button_menu.Update(screen)

                play_again_button.ChangeColor(play_mouse_pos)
                play_again_button.Update(screen)

                # Displaying the creators
                creators = "Creators: Jacek Kozlowski and Mykhailo Kapustianyk"
                creators_text = self.get_font(30).render(creators, True, "Red")
                creators_rect = creators_text.get_rect(center=(700, 665))
                screen.blit(creators_text, creators_rect)

                for event in pygame.event.get():
                    # If the winning button is clicked
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                        and winner_button_menu.CheckForInput(play_mouse_pos)
                        and event.button == 1
                    ):  # If the left mouse button is depressed.:
                        from Main import Labirynt

                        game = Labirynt()
                        game.main_menu()  # Transition to the main menu of the game

                    # If the 'Play Again' button is clicked
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                        and play_again_button.CheckForInput(play_mouse_pos)
                        and event.button == 1
                    ):  # If the left mouse button is depressed.:
                        from Main import Labirynt

                        game = Labirynt(auto_start=False)
                        game.game_process()  # Start a new game

                        # The auto_start parameter set to False ensures the game starts anew upon creating the object

                    # Closing the game
                    if event.type == pygame.QUIT:
                        pygame.quit()  # Terminate Pygame
                        exit()  # End the program

            # Event handling
            for event in pygame.event.get():
                # When the mouse is clicked and the cross is already drawn
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and cross_drawn
                    and event.button == 1
                ):  # If the left mouse button is depressed.:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Checking if the mouse click is within the board boundaries
                    if location is not None and (
                        100 <= mouse_x <= 100 + 10 * 60
                        and 50 <= mouse_y <= 50 + 10 * 60
                    ):
                        row = location[0]
                        col = location[1]

                        selected_square = (row, col)  # Record the selected square

                        # If the selected square is adjacent to any correct square and the game is not yet over
                        if (
                            any(
                                selected_square in self.get_neighbors(correct_square)
                                for correct_square in self.correct_squares
                            )
                            and not winner
                        ):
                            # If the selected square is part of the labyrinth
                            if selected_square in self.labyrinth:
                                # If the selected square is not already in the list of correct squares
                                if selected_square not in self.correct_squares:
                                    labyrinth_temp.append(
                                        selected_square
                                    )  # Add to the temporary labyrinth list
                                    self.correct_squares.append(
                                        selected_square
                                    )  # Add to the list of correct squares
                                    counter += 1  # Increment the count of correct moves

                                # If the count is 5 and the selected square is not the treasure
                                if counter == 5 and selected_square != self.treasure:
                                    # Display the last user-clicked square when the count is 5
                                    loc1, loc2 = selected_square
                                    screen.blit(
                                        image_point, (102 + loc2 * 60, 52 + loc1 * 60)
                                    )

                                    # Display the 5th green tick for the square
                                    board.draw_small_board(screen, counter, wall)

                                    point = True  # Helper variable

                                # If the selected square is the treasure
                                if selected_square == self.treasure:
                                    # Display the treasure
                                    loc1, loc2 = self.treasure
                                    screen.blit(
                                        image_treasure,
                                        (102 + loc2 * 60, 52 + loc1 * 60),
                                    )

                                    board.draw_small_board(screen, counter, wall)

                                    pause = True
                                    winner = True  # Set the winner status to true

                            else:  # If the selected square is adjacent to a correct one but not in the labyrinth
                                # If the selected square is not already in the list of found walls
                                if selected_square not in walls:
                                    walls.append(
                                        selected_square
                                    )  # Add to the list of walls

                                    # Display the last user-clicked wall
                                    loc1, loc2 = selected_square
                                    screen.blit(
                                        image_wall, (102 + loc2 * 60, 52 + loc1 * 60)
                                    )

                                    wall = True  # Helper variable
                                    board.draw_small_board(screen, counter, wall)

                # Return to the main menu
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and button_back.CheckForInput(play_mouse_pos)
                    and event.button == 1
                ):  # If the left mouse button is depressed.:
                    from Main import Labirynt

                    game = Labirynt()
                    game.main_menu()
                # Closing the game
                if event.type == pygame.QUIT:
                    pygame.quit()  # Terminate Pygame
                    exit()  # End the program

            pygame.display.update()  # Update the displayed game graphics
