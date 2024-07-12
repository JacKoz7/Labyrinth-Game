# Function to display game instructions on the screen
def inst(screen, get_font, h):
    text = 'In this game, one must uncover the opponent’s hidden treasure. Each player possesses a board in the form'
    text1 = 'of two squares, each 10 x 10 squares in size. In any square of their board, players place a treasure'
    text2 = 'marked with a circle and designate a path to it, drawing a labyrinth of any length and a width of'
    text3 = 'one square. The labyrinth may be quite winding and must contain 35 segments, each one square long.'
    text4 = 'It should terminate at the edge of the square. In this terminal square, a cross is drawn, and its coordinates'
    text5 = 'are known to the opponent. From this point, they will set off to search for the treasure. The player starting'
    text6 = 'the game announces the coordinates of the field they wish to move to from point x. If the path is clear, meaning'
    text7 = 'there is no labyrinth wall, a move is permitted. The player may take five steps in this manner, unless'
    text8 = 'they encounter a labyrinth wall, which ends their turn. The player may traverse the same square multiple times,'
    text9 = 'trying to escape a dead end. To aid in the task, on the second square, players mark discovered labyrinth walls'
    text10 = 'and the traversed path. The victor is the one who reaches the opponent’s hidden treasure first.'

    inst_text = get_font.render(text, True, 'Red')
    inst_rect = inst_text.get_rect(center=(h - 35, 190))
    screen.blit(inst_text, inst_rect)

    inst_text1 = get_font.render(text1, True, 'Red')
    inst_rect1 = inst_text.get_rect(center=(h - 35, 230))
    screen.blit(inst_text1, inst_rect1)

    inst_text2 = get_font.render(text2, True, 'Red')
    inst_rect2 = inst_text.get_rect(center=(h - 35, 270))
    screen.blit(inst_text2, inst_rect2)

    inst_text3 = get_font.render(text3, True, 'Red')
    inst_rect3 = inst_text.get_rect(center=(h - 35, 310))
    screen.blit(inst_text3, inst_rect3)

    inst_text4 = get_font.render(text4, True, 'Red')
    inst_rect4 = inst_text.get_rect(center=(h - 35, 350))
    screen.blit(inst_text4, inst_rect4)

    inst_text5 = get_font.render(text5, True, 'Red')
    inst_rect5 = inst_text.get_rect(center=(h - 35, 390))
    screen.blit(inst_text5, inst_rect5)

    inst_text6 = get_font.render(text6, True, 'Red')
    inst_rect6 = inst_text.get_rect(center=(h - 35, 430))
    screen.blit(inst_text6, inst_rect6)

    inst_text7 = get_font.render(text7, True, 'Red')
    inst_rect7 = inst_text.get_rect(center=(h - 35, 470))
    screen.blit(inst_text7, inst_rect7)

    inst_text8 = get_font.render(text8, True, 'Red')
    inst_rect8 = inst_text.get_rect(center=(h - 35, 510))
    screen.blit(inst_text8, inst_rect8)

    inst_text9 = get_font.render(text9, True, 'Red')
    inst_rect9 = inst_text.get_rect(center=(h - 35, 550))
    screen.blit(inst_text9, inst_rect9)

    inst_text10 = get_font.render(text10, True, 'Red')
    inst_rect10 = inst_text.get_rect(center=(h - 35, 590))
    screen.blit(inst_text10, inst_rect10)

    # inst_text11 = get_font.render(text11, True, 'Red')
    # inst_rect11 = inst_text.get_rect(center=(h - 35, 630))
    # screen.blit(inst_text11, inst_rect11)
