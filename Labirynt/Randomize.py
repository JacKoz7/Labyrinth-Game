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

def generate_maze():
    def is_valid(x, y, maze, treasure, cross):
        return 0 <= x < 10 and 0 <= y < 10 and (x, y) not in maze and (x, y) != treasure and (x, y) != cross

    def get_valid_neighbors(x, y, maze, treasure, cross):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, maze, treasure, cross):
                neighbors.append((nx, ny))

        return neighbors

    treasure = place_treasure()
    cross = place_cross(treasure)

    maze = [treasure]
    visited = set(maze)

    while True:
        neighbors = get_valid_neighbors(*maze[-1], visited, treasure, cross)

        if not neighbors:
            break

        neighbor = random.choice(neighbors)
        maze.append(neighbor)
        visited.add(neighbor)

        if neighbor == cross:
            break

    while len(maze) < 35:
        x, y = random.randint(0, 9), random.randint(0, 9)
        if (x, y) != treasure and (x, y) != cross and (x, y) not in visited:
            maze.append((x, y))
            visited.add((x, y))

    return maze

