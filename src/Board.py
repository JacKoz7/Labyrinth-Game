import pygame


# A class representing the state of the game
class GameState:
    def __init__(self):
        self.selected_point = None  # Initially, no square is selected
        self.square_size = 60  # The size of each square
        self.tick_image = pygame.image.load(
            "Images/green_tick.png"
        )  # The image of a green tick
        self.x_image = pygame.image.load(
            "Images/Red_X.png"
        )  # The image of a red cross

    # A method to return a font object of a specified size
    def get_font(self, size):
        return pygame.font.Font("Ancient Medium.ttf", size)

    # A method to draw the game board
    def draw_board(self, screen):
        screen.fill("Black")  # Fill the screen with black

        # Drawing a 10x10 board
        for row in range(10):
            for col in range(10):
                pygame.draw.rect(
                    screen,
                    "Red",
                    (
                        100 + col * self.square_size,
                        50 + row * self.square_size,
                        self.square_size,
                        self.square_size,
                    ),
                    2,
                )

        # Check if a square on the board is selected
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get the mouse cursor position
        if (
            100 <= mouse_x <= 99 + 10 * self.square_size
            and 50 <= mouse_y <= 49 + 10 * self.square_size
        ):
            selected_col = (
                mouse_x - 100
            ) // self.square_size  # Calculate the selected column
            selected_row = (
                mouse_y - 50
            ) // self.square_size  # Calculate the selected row

            # Highlight the selected square
            pygame.draw.rect(
                screen,
                "Red",
                (
                    100 + selected_col * self.square_size,
                    50 + selected_row * self.square_size,
                    self.square_size,
                    self.square_size,
                ),
                5,
            )

            # Update the selected square
            self.selected_point = (selected_row, selected_col)

            return self.selected_point
        else:
            return None

    # A method to draw a small board used for marking ticks in the second stage of the game
    def draw_small_board(self, screen, counter, wall):
        for x in range(5):  # Loop through 5 squares
            pygame.draw.rect(
                screen,
                "Red",
                (
                    900 + x * self.square_size,
                    330 + self.square_size,
                    self.square_size,
                    self.square_size,
                ),
                7,
            )
            if x < counter:  # If there are fewer marked squares than the counter
                screen.blit(
                    self.tick_image,
                    (900 + x * self.square_size, 330 + self.square_size),
                )  # Draw the green tick
        if wall:
            screen.blit(
                self.x_image, (900 + counter * self.square_size, 330 + self.square_size)
            )  # Draw the red cross
