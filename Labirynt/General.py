import pygame
from sys import exit
from Button import button1
from instruction import inst

from First_move import First_Stage
from Endgame_board2 import Second_Stage, Game_status



class Labirynt:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.h = 700
        self.SCREEN = pygame.display.set_mode((2 * self.h, self.h))
        pygame.display.set_caption('Labirynt')
        self.txt2 = 'Gracz 2'
        self.txt = 'Gracz 1'

    def get_font(self, size):
        return pygame.font.Font('Ancient Medium.ttf', size)

    def options(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()
            self.SCREEN.fill('Black')
            options_text = self.get_font(55).render('Instrukcja gry:', True, 'Red')
            options_rect = options_text.get_rect(center=(self.h, 100))
            self.SCREEN.blit(options_text, options_rect)
            inst(self.SCREEN, self.get_font(35), self.h)  # wywolanie funkcji inst z pliku instructions

            img = pygame.image.load('empty_button.png')

            button_back = button1(image=img, pos=(180, 80), text_input='Powrót', font=self.get_font(65),
                                  base_color='Black', new_color='White')

            button_back.ChangeColor(options_mouse_pos)
            button_back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_back.CheckForInput(options_mouse_pos):
                        self.main_menu()

            pygame.display.update()

    def main_menu(self):

        Player1_beginning = First_Stage()
        Player2_beginning = First_Stage()

        Player1_ending = Second_Stage(Player1_beginning.treasure,
                                      Player1_beginning.labyrinth,
                                      Player1_beginning.cross)

        Player1_status = Game_status(walls=[], labyrinth_temp=[], counter=0)

        while True:
            menu_mouse_pos = pygame.mouse.get_pos()
            self.SCREEN.fill('Black')
            menu_text = self.get_font(200).render('Labirynt', True, 'Red')
            menu_rect = menu_text.get_rect(center=(self.h, 100))

            img = pygame.image.load('empty_button.png')

            play_button = button1(image=img, pos=(self.h, 280), text_input='Graj', font=self.get_font(65),
                                  base_color='Black', new_color='White')

            options_button = button1(image=img, pos=(self.h, 430), text_input='Instrukcja', font=self.get_font(65),
                                     base_color='Black', new_color='White')

            quit_button = button1(image=img, pos=(self.h, 580), text_input='Wyjscie', font=self.get_font(65),
                                  base_color='Black', new_color='White')

            self.SCREEN.blit(menu_text, menu_rect)

            for button in [play_button, options_button, quit_button]:
                button.ChangeColor(menu_mouse_pos)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.CheckForInput(menu_mouse_pos):
                            Player1_beginning.play(self.SCREEN, self.txt, 'Gracz 2 :)')
                            print(Player1_beginning.treasure)
                            print(Player1_beginning.labyrinth)
                            print(Player1_beginning.cross)

                            #Player2_beginning.play(self.SCREEN, self.txt2, 'Kontynuuj ')
                            i = 0
                            while(i <= 3):
                                Player1_ending.endgame(self.SCREEN, self.txt, Player1_status.walls,
                                                   Player1_status.labyrinth_temp, Player1_status.counter)
                                i += 1




                    if options_button.CheckForInput(menu_mouse_pos):
                        self.options()
                    if quit_button.CheckForInput(menu_mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

    def run(self):
        self.main_menu()

game = Labirynt()
game.run()
