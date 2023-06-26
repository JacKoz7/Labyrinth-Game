# Funkcja służąca do wyświetlania instrukcji gry na ekran
def inst(screen, get_font, h):        #
    napis = """
    to jest 
    dlugi
    tekst
    """
    text = 'W tej grze nalezy odnalezc ukryty skarb przeciwnika. Kazdy z graczy posiada plansze w postaci '
    text1 = 'dwoch kwadratow wielkosci 10 x 10 kratek. W dowolnej kratce swojego kwadratu umieszczamy skarb'
    text2 = 'oznaczony kólkiem i wyznaczamy droge do niego, rysujac labirynt dowolnej dlugosci i szerokosci '
    text3 = 'jednej kratki. Labirynt moze byc dosc krety i ma posiadac 35 odcinków, kazdy po jednej kratce.'
    text4 = 'Powinien sie konczyc na brzegu kwadratu. W tej koncowej kratce rysujemy krzyzyk i jego wspólrzedne'
    text5 = 'sa znane przeciwnikowi. To stad wyruszy na poszukiwanie naszego skarbu. Osoba rozpoczynajaca gre'
    text6 = 'podaje wspólrzedne pola, na które chce sie przesunac z punktu x. Jesli droga jest wolna, bo nie'
    text7 = 'ma tam sciany labiryntu, mozliwe jest wykonanie ruchu. Grajacy moze w ten sposób postawic piec kroków,'
    text8 = 'chyba ze natknie sie na sciane labiryntu, wtedy konczy marsz. Grajacy moze przechodzic przez jedno '
    text9 = 'pole nawet po kilka razy, chcac sie wydostac ze slepej uliczki. Aby sobie ulatwic zadanie, na drugim '
    text10 = 'kwadracie zaznaczamy odkryte sciany labiryntu przeciwnika i przebyta droge. Wygrywa ten, kto pierwszy'
    text11 = 'dotrze do ukrytego przez przeciwnika skarbu.'
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
    inst_text11 = get_font.render(text11, True, 'Red')
    inst_rect11 = inst_text.get_rect(center=(h - 35, 630))
    screen.blit(inst_text11, inst_rect11)

    creators = "Twórcy: Jacek Kozlowski i Mykhailo Kapustianyk"
    creators_text = get_font.render(creators, True, 'Red')
    creators_rect = creators_text.get_rect(center=(1070, 30))
    screen.blit(creators_text, creators_rect)
