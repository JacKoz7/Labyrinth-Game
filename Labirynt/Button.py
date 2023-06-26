# Klasa przycisk #
class button:
    # Konstruktor z parametrami, przyjmujący argumenty
    def __init__(self, image, pos, text_input, font, base_color, new_color):
        self.image = image  # Obrazek na przycisku.
        self.x_pos = pos[0]  # Pozycja X przycisku
        self.y_pos = pos[1]  # Pozycja Y przycisku
        self.font = font  # Czcionka dla tekstu na przycisku.
        self.base_color = base_color  # Podstawowy kolor tekstu
        self.new_color = new_color  # Nowy kolor tekstu (na przykład po najechaniu myszką)
        self.text_input = text_input  # Tekst do wyświetlenia na przycisku
        self.text = self.font.render(self.text_input, True, self.base_color)  # Renderowanie tekstu z kolorem

        # Jeśli obrazek nie jest dostarczony, używanie renderowanego tekstu jako obrazka przycisku
        if self.image is None:
            self.image = self.text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # Rect obrazka (dla detekcji kolizji)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))  # Rect tekstu

    # Metoda aktualizująca wygląd przycisku na ekranie
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)  # Rysowanie obrazka na ekranie
        screen.blit(self.text, self.text_rect)  # Rysowanie tekstu na ekranie

    # Metoda sprawdzająca, czy mysz jest nad przyciskiem (czyli czy kliknięcie nastąpiło na przycisku)
    def CheckForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    # Metoda zmieniająca kolor tekstu, jeśli mysz jest nad przyciskiem.
    def ChangeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
                and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.new_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)