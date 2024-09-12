import pygame


class Button:
    def __init__(self, image, pos, text_input, font, base_color, new_color):
        self.image = image  # The visual depiction upon the button
        self.x_pos = pos[0]  # The X coordinate of the button's position
        self.y_pos = pos[1]  # The Y coordinate of the button's position
        self.font = font  # The typeface for the text on the button
        self.base_color = base_color  # The primary hue of the text
        self.new_color = (
            new_color  # The altered hue of the text (e.g., upon mouse hover)
        )
        self.text_input = text_input  # The text to be displayed upon the button
        self.text = self.font.render(
            self.text_input, True, self.base_color
        )  # Rendering the text with its colour

        # If no image is provided, utilize the rendered text as the button's image
        if self.image is None:
            self.image = self.text

        self.rect = self.image.get_rect(
            center=(self.x_pos, self.y_pos)
        )  # The rectangle of the image (for collision detection)
        self.text_rect = self.text.get_rect(
            center=(self.x_pos, self.y_pos)
        )  # The rectangle of the text

    # A method to refresh the button's appearance on the screen
    def Update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)  # Depicting the image upon the screen
        screen.blit(self.text, self.text_rect)  # Depicting the text upon the screen

    # A method to verify if the mouse is hovering over the button (i.e., if the click occurred on the button)
    def CheckForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    # A method to alter the text's colour if the mouse is hovering over the button
    def ChangeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.new_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def ChangeColorImage(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            new_image = self.image.copy()  # Crafting a replica of the image

            for x in range(new_image.get_width()):
                for y in range(new_image.get_height()):
                    pixel_color = new_image.get_at((x, y))
                    if pixel_color.a > 0:  # Ensuring the pixel's opacity
                        new_color = pygame.Color("white")  # The new hue for the pixel
                        new_color.a = (
                            pixel_color.a
                        )  # Retaining the original opacity value
                        new_image.set_at(
                            (x, y), new_color
                        )  # Assigning the new hue to the pixel

            self.image = new_image
        else:
            self.image = self.image.copy()
