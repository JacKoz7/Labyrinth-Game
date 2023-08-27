import random
class RandomizeButton:
    def __init__(self, image, pos):
        self.image = image
        self.original_image = image.copy()  # Przechowaj kopię oryginalnego obrazka
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # Rect obrazka (dla detekcji kolizji)


    def Update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)  # Rysowanie obrazka na ekranie

    def CheckForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def ChangeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
                and position[1] in range(self.rect.top, self.rect.bottom):
            # Pobierz maskę alfa obrazka
            alpha_mask = self.original_image.convert_alpha()

            # Ustaw kolor biały na obrazku tam, gdzie maska alfa zawiera kółko
            for x in range(alpha_mask.get_width()):
                for y in range(alpha_mask.get_height()):
                    pixel_color = alpha_mask.get_at((x, y))
                    if pixel_color[3] > 0:  # Sprawdź wartość kanału alfa (większa niż 0 oznacza nieprzezroczystość)
                        alpha_mask.set_at((x, y), (
                        255, 255, 255, pixel_color[3]))  # Ustaw piksel na biały (z zachowaniem wartości alfa)

            # Nałóż obrazek z kółkiem na obrazek główny, uwzględniając maskę alfa
            self.image.blit(alpha_mask, (0, 0))

def place_treasure():
    treasure = (random.randint(0, 9), random.randint(0, 9))
    return treasure

def place_cross(treasure):
    cross = random.choice([(0, i) for i in range(10)] + [(9, i) for i in range(10)] + [(i, 0) for i in range(1, 9)] +
                          [(i, 9) for i in range(1, 9)])
    while cross == treasure:
        cross = random.choice(
            [(0, i) for i in range(10)] + [(9, i) for i in range(10)] + [(i, 0) for i in range(1, 9)] +
            [(i, 9) for i in range(1, 9)])
    return cross

def place_random_point(treasure, cross):
    rpoint = (random.randint(0, 9), random.randint(0, 9))
    while rpoint == treasure or rpoint == cross:
        rpoint = (random.randint(0, 9), random.randint(0, 9))
    return rpoint



def generate_maze(treasure, cross):
    path = []

    x1, y1 = treasure
    x2, y2 = cross

    # # Dodajemy punkty startowe
    path.append((x1, y1))

    # Generujemy losową ścieżkę
    while x1 != x2 or y1 != y2:
        direction = random.choice(['horizontal', 'vertical'])

        if direction == 'horizontal':
            if x1 < x2:
                x1 += 1
            elif x1 > x2:
                x1 -= 1
        else:
            if y1 < y2:
                y1 += 1
            elif y1 > y2:
                y1 -= 1

        new_point = (x1, y1)

        if new_point != path[-1]:  # Sprawdź, czy nowy punkt jest różny od ostatniego punktu na ścieżce
            path.append(new_point)

    return path[1:-1]  # Zwracamy drogę bez punktu startowego i końcowego


# def generate_maze_points(treasure, cross, random_point, path1):
#     points = []
#     points.extend(path1)
#
#     # Generujemy ścieżki od treasure lub cross do random_point
#     remaining_points = 35 - len(points)
#     while remaining_points > 0:
#         path = generate_maze(treasure if random.random() < 0.5 else cross, random_point)
#         points.extend(path)
#         remaining_points -= len(path)
#
#     return points[:35]  # Ograniczamy liczbę punktów do 35









