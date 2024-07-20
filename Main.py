import pygame
from sys import exit
from Button import Button
from instruction import inst
from Stage1_Stage2 import First_Stage
from Stage3_Stage4 import Second_Stage, Game_status


class Labirynt:
    def __init__(self, auto_start=True):
        pygame.init()
        pygame.mixer.init()
        self.music_playing = False
        self.clock = pygame.time.Clock()
        self.h = 700
        self.screen = pygame.display.set_mode((2 * self.h, self.h))
        pygame.display.set_caption('Labirynt')
        self.txt2 = 'Player 2'
        self.txt = 'Player 1'
        self.icon = pygame.image.load("Images/game_icon.png")
        pygame.display.set_icon(self.icon)

        if auto_start:
            self.main_menu()

    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    def play_menu_music(self):
        pygame.mixer.music.load('soundtrack/MenuMusic.mp3')
        pygame.mixer.music.play(-1) #loop music
        self.music_playing = True

    def play_game_music(self):
        pygame.mixer.music.load('soundtrack/GameMusic.mp3')
        pygame.mixer.music.play(-1)
        self.music_playing = True

    def game_process(self):
        self.play_game_music() # play battle music during gameplay

        Player1_beginning = First_Stage()
        Player2_beginning = First_Stage()

        Player1_status = Game_status(walls=[], found_labyrinth=[], winner=False)
        Player2_status = Game_status(walls=[], found_labyrinth=[], winner=False)

        Player1_beginning.play(self.screen, self.txt, 'Player 2 ')

        Player1_ending = Second_Stage(Player1_beginning.treasure,
                                      Player1_beginning.labyrinth,
                                      Player1_beginning.cross)

        Player2_beginning.play(self.screen, self.txt2, 'Continue ')
        Player2_ending = Second_Stage(Player2_beginning.treasure,
                                      Player2_beginning.labyrinth,
                                      Player2_beginning.cross)

        while Player1_status.winner is False and Player2_status.winner is False:
            if Player1_status.winner is False:
                Player2_ending.endgame(self.screen, self.txt, self.txt2, Player1_status.walls,
                                       Player1_status.found_labyrinth, Player2_status.winner)

            if Player2_status.winner is False:
                Player1_ending.endgame(self.screen, self.txt2, self.txt, Player2_status.walls,
                                       Player2_status.found_labyrinth, Player1_status.winner)

        self.play_menu_music()
        self.main_menu()

    def instructions(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()
            self.screen.fill('Black')

            options_text = self.get_font(55).render('Game Instructions:', True, 'Red')
            options_rect = options_text.get_rect(center=(self.h, 100))
            self.screen.blit(options_text, options_rect)

            inst(self.screen, self.get_font(35), self.h)

            img_button = pygame.image.load('Images/empty_button.png')

            menu_button = Button(image=img_button, pos=(180, 80), text_input='Menu', font=self.get_font(65),
                                 base_color='Black', new_color='White')

            menu_button.ChangeColor(options_mouse_pos)
            menu_button.Update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if menu_button.CheckForInput(options_mouse_pos):
                        return

            pygame.display.update()

    def main_menu(self):
        if not self.music_playing: # play menu music
            self.play_menu_music()
        while True:
            menu_mouse_pos = pygame.mouse.get_pos()
            bg = pygame.image.load("Images/game_background.png")
            self.screen.blit(bg, (0, 0))
            menu_text = self.get_font(180).render('The Labirynth', True, 'Red')
            menu_rect = menu_text.get_rect(center=(self.h, 100))

            img = pygame.image.load('Images/empty_button.png')

            play_button = Button(image=img, pos=(self.h, 280), text_input='Play', font=self.get_font(65),
                                 base_color='Black', new_color='White')

            instruction_button = Button(image=img, pos=(self.h, 430), text_input='Instructions', font=self.get_font(60),
                                    base_color='Black', new_color='White')

            quit_button = Button(image=img, pos=(self.h, 580), text_input='Exit', font=self.get_font(65),
                                 base_color='Black', new_color='White')

            self.screen.blit(menu_text, menu_rect)

            for buttons in [play_button, instruction_button, quit_button]:
                buttons.ChangeColor(menu_mouse_pos)
                buttons.Update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if play_button.CheckForInput(menu_mouse_pos):
                        pygame.mixer.music.stop()
                        self.music_playing = False
                        self.game_process()

                    if instruction_button.CheckForInput(menu_mouse_pos):
                        self.instructions()

                    if quit_button.CheckForInput(menu_mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

    def run(self):
        self.main_menu()


if __name__ == "__main__":
    game = Labirynt()
    game.run()