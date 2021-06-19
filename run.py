#! /usr/bin/env python3

import time
import pygame as pg
import adt
import models
import textrect
from language import game_dict
import sys

pg.init()
pg.mixer.init()

# ==============================================================================
# konstanta global yang dipakai dalam game,
# ukuran windows game
GAME_WIDTH = 900
GAME_HEIGHT = 600

# Font yang dipakai dalam game.
# Jika ngga eksplisit disebut, fungsi akan menggunakan GAME_FONT secara default
GAME_FONT = "assets/fonto.ttf"
GAME_FONT2 = "assets/DK Jambo.otf"

# Musik yang dipakai dalam game
BG_MUSIC = 'assets/music.ogg'

GAME_CAPTION = 'Tower of Hanoi!'
BACK_BUTTON = "assets/back.png"



# ==============================================================================
# initialisasi game
gameDisplay = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
gameClock = pg.time.Clock()
gameIcon = pg.image.load('assets/logo.png')
pg.display.set_caption(GAME_CAPTION)
pg.display.set_icon(gameIcon)

# ==============================================================================
# definisi objek-objek pembangun game:
def pgText(text, pos, font_size=18, font_name=GAME_FONT):
    """Menulis teks rata tengah warna hitam pada layar."""
		
    
    #font = pg.font.Font(font_name, font_size)
    #font = pg.font.SysFont("Arial", font_size)
    font = pg.font.Font(pg.font.get_default_font(), font_size)
    textSurf = font.render(text, True, adt.color_use("black"))
    textRect = textSurf.get_rect()
    textRect.center = pos
    gameDisplay.blit(textSurf, textRect)


def pgParagraf(text, rect_info, font_name=GAME_FONT, font_size=18):
    """Menulis paragraf rata kiri warna hitam
    dengan warna background windows pada layar"""
    
    font = pg.font.Font(pg.font.get_default_font(), font_size)
    #font = pg.font.SysFont("Arial", 18)
    rect = pg.Rect(rect_info)
    rendered = textrect.render_textrect(text, font, rect,
                                        adt.color_use("black"),
                                        adt.color_use("background"), 0)
    if rendered:
        gameDisplay.blit(rendered, rect.topleft)


def pgButton(msg, pos, size, col_still, col_hover, action=None):
    """Membuat button berisi teks"""

    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # ubah warna button menjadi color_hover ketika mouse hover di button,
    # dan kembalikan jadi color_still ketika mouse tidak ada di button.
    if (pos[0] + size[0] > mouse[0] > pos[0]) and \
       (pos[1] + size[1] > mouse[1] > pos[1]):
        pg.draw.rect(gameDisplay, col_hover, (pos, size))
        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(gameDisplay, col_still, (pos, size))

    pgText(msg, (pos[0]+size[0]/2, pos[1]+size[1]/2), 20)


def pgSlider(pos, var=True):
    """Membuat slider on/off"""
    
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    size = (80, 80)

    global game_mouse_click

    # cek posisi dan perilaku mouse
    if (pos[0]+20 + size[0] > mouse[0] > pos[0]-20) and \
       (pos[1] + size[1] > mouse[1] > pos[1]):
        if click[0] == 1 and not game_mouse_click:
            var = not var
            game_mouse_click = True
        elif click[0] == 0:
            game_mouse_click = False

    # ubah gambar slider menurut state baru
    if var:
        # slider dalam posisi on
        pgImage(pos, size, "assets/tog-on.png", action=None)
    else:
        pgImage(pos, size, "assets/tog-off.png", action=None)

    return var


def pgImage(pos, size, file, action=None):
    """Membuat button berisi image"""

    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # cetak image ke layar
    raw = pg.image.load(file).convert_alpha()
    img = pg.transform.scale(raw, size)
    rect = pg.Rect(pos, size)
    gameDisplay.blit(img, rect)

    # ini akan diproses jika image berfungsi menjadi button
    if (pos[0]+size[0] > mouse[0] > pos[0]) and \
       (pos[1]+size[1] > mouse[1] > pos[1]) and \
       click[0] == 1 and action is not None:
        action()


def pgMusic():
    """Memainkan musik"""

    global game_data
    if game_data['sound']:
        # musik menyala
        pg.mixer.music.unpause()
    else:
        pg.mixer.music.pause()


# ==============================================================================
# definisi fungsi-fungsi di game:
def GameQuit():
    """Keluar dari game."""
    pg.quit()
    quit()


def GameHomePage():
    """Menu utama dari game"""

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgText(game_dict[lang]['game_title'], (GAME_WIDTH/2, 100), 90)

        # buat pilihan menu utama
        pgImage((GAME_WIDTH/2-100, GAME_HEIGHT/2-100), (200, 200), "assets/play-h.png", GameHistory)
        pgImage((GAME_WIDTH/6-40, 450), (80, 80), "assets/about.png", GameAbout)
        pgImage((GAME_WIDTH/6*2-40, 450), (80, 80), "assets/secret.png", GameSecret1)
        pgImage((GAME_WIDTH/6*3-40, 450), (80, 80), "assets/hof.png", GameHOF)
        pgImage((GAME_WIDTH/6*4-40, 450), (80, 80), "assets/setting.png", GameSetting)
        pgImage((GAME_WIDTH/6*5-40, 450), (80, 80), "assets/exit.png", GameQuit)

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)


def GamePlay():
    """literally game hanoi-nya."""
    global username
	
    # Create main menu object
    menu = models.MainMenu(GAME_WIDTH, GAME_HEIGHT)

    # Create game object
    game = models.Game(GAME_WIDTH, GAME_HEIGHT)

    # Discs' move variables
    done = False
    drag = False
    drop = False
    move = False
    game_over = False
    init_game = False
    disc_index = None
    last_pos = [0, 0]

    # Moves counter
    moves_counter = 0
    play_time = 0
	
    # -------- Main Game Loop -----------
    while not done:

        # --- Main event loop
        for event in pg.event.get():

            if event.type == pg.QUIT:
                done = True

            elif event.type == pg.MOUSEBUTTONDOWN:
                drag = True
                drop = False

                if init_game:
                    if not game_over:
                        for i in range(0, game.n_discs):
                            if game.discs[i].is_clicked():
                                current_pos = game.discs[i].current_pos
                                pos_length = len(game.pos[current_pos].discs)
                                if game.discs[i] == game.pos[current_pos].discs[pos_length-1]:
                                    disc_index = i
                                    last_pos = [game.discs[i].rect.x, game.discs[i].rect.y]
                                    move = True
                    else:

                        # ranking hasil user
                        game_data['hof'] = adt.algo_addSorted(game_data['hof'],
                                                              game.n_discs,
                                                              [username, play_time, moves_counter])
                        # masukkan ke database
                        adt.data_write(game_data)
                        
                        if menu.btn_quit.is_clicked():
                            done = True
                            GameHomePage()

                        if menu.btn_play_again.is_clicked():
                            game.sprites_list.remove(game.discs)
                            game.pos[2].discs = []
                            moves_counter = 0
                            game.discs = []
                            game.draw_discs()
                            game_over = False

                        if menu.btn_return.is_clicked():
                            menu.sprites_list.remove([menu.btn_play_again, menu.btn_return, menu.btn_quit])
                            menu.sprites_list.add([menu.btn_discs, menu.label])
                            game.sprites_list.remove(game.discs)
                            init_game = False
                else:
                    start_ticks = pg.time.get_ticks()  # Waktu semenjak pg.init() dimulai

                    for i in range(0, len(menu.btn_discs)):
                        if menu.btn_discs[i].is_clicked():
                            game.set_n_discs(menu.btn_discs[i].value)
                            game.sprites_list.remove(game.discs)
                            game.discs = []
                            game.pos[2].discs = []
                            moves_counter = 0
                            game.draw_discs()
                            init_game = True
                            game_over = False
                            break

            elif event.type == pg.MOUSEBUTTONUP:
                drag = False
                drop = True

        gameDisplay.fill(adt.color_use("background"))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        if init_game:

            pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)
            pgText(game_dict[lang]['play_info'].format(str(moves_counter), str(round(play_time, 1))), (GAME_WIDTH/2, 120), 18)

            if game_over:
                start_ticks = pg.time.get_ticks()  # Waktu semenjak pg.init() dimulai part 2, bisa lebih efisien enggak ya?
                menu.sprites_list.draw(gameDisplay)

                if len(game.pos[2].discs) == game.n_discs:
                    if moves_counter == game.min_moves:
                        pgText(game_dict[lang]['congrats_min'], (GAME_WIDTH/2, GAME_HEIGHT/3), 18)
                    else:
                        pgText(game_dict[lang]['congrats_aja'], (GAME_WIDTH/2, GAME_HEIGHT/3), 18)

            else:
                play_time = (pg.time.get_ticks() - start_ticks)/1000  # Actual timer

                if drag:
                    if move:
                        pos = pg.mouse.get_pos()
                        game.discs[disc_index].rect.x = pos[0] - (game.discs[disc_index].width/2)
                        game.discs[disc_index].rect.y = pos[1] - (game.discs[disc_index].height/2)

                elif drop:
                    if move:
                        current_pos = game.discs[disc_index].current_pos
                        new_pos = None
                        change = False
                        turn_back = True
                        position = pg.sprite.spritecollideany(game.discs[disc_index], game.pos_sprites_list)

                        if position is not None:
                            new_pos = position.pos_index
                            if new_pos != current_pos:
                                disc_length = len(position.discs)
                                if disc_length == 0:
                                    turn_back = False
                                    change = True
                                elif game.discs[disc_index].id > position.discs[disc_length-1].id:
                                    turn_back = False
                                    change = True

                        if change:
                            moves_counter = moves_counter + 1
                            game.pos[current_pos].discs.remove(game.discs[disc_index])
                            game.discs[disc_index].current_pos = new_pos
                            game.pos[new_pos].discs.append(game.discs[disc_index])
                            new_pos_length = len(game.pos[new_pos].discs)
                            game.discs[disc_index].rect.x = game.pos[new_pos].rect.x - \
                                                            ((game.DISC_WIDTH/(game.discs[disc_index].id+1)/2)-(game.DISC_HEIGHT/2))
                            game.discs[disc_index].rect.y = (game.BOARD_Y - game.DISC_HEIGHT) - (game.DISC_HEIGHT*(new_pos_length-1))

                            # Check if the game is over
                            if len(game.pos[2].discs) == game.n_discs:
                                game_over = True
                                menu.sprites_list.add([menu.btn_play_again, menu.btn_quit, menu.btn_return])
                                menu.sprites_list.remove([menu.label, menu.btn_discs])

                        # ngatur kalau dilepas diudara
                        if turn_back:
                            game.discs[disc_index].rect.x = last_pos[0]
                            game.discs[disc_index].rect.y = last_pos[1]

                        move = False
            game.sprites_list.draw(gameDisplay)

        else:
            menu.sprites_list.draw(gameDisplay)

        # update gameDisplay.
        pg.display.flip()
        gameClock.tick(60)

    pg.quit()


def GameAbout():
    """Menu utama dari game"""

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)
        
        pgText(game_dict[lang]['about'], (GAME_WIDTH/2, 50), 50)
        pgParagraf(game_dict[lang]['about_text'], (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))
        pgParagraf(game_dict[lang]['citation_text'], (GAME_WIDTH/2-250, 350, 500, GAME_HEIGHT))


        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)


def GameHOF():
    """Menu utama dari game"""

    teks_hof = adt.algo_makeHOF(game_data['hof'])

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        pgText(game_dict[lang]['highscore'], (GAME_WIDTH/2, 50), 50)

        pgParagraf(teks_hof, (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)


def GameSetting():
    """Menu utama dari game"""

    global game_data
    global lang

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        pgText(game_dict[lang]['settings'], (GAME_WIDTH/2, 50), 50)
        pgText(game_dict[lang]['sound'], (GAME_WIDTH/2-200, GAME_HEIGHT/2-50), 40)
        pgText(game_dict[lang]['language'], (GAME_WIDTH/2-200, GAME_HEIGHT/2+50), 40)

        # Slider untuk music
        game_data['sound'] = pgSlider((GAME_WIDTH/2+200,
                                       GAME_HEIGHT/2-75),
                                      game_data['sound'])
        pgMusic()

        # Slider untuk bahasa
        game_data['lang'] = pgSlider((GAME_WIDTH/2+200,
                                      GAME_HEIGHT/2+25),
                                     game_data['lang'])
        if game_data['lang']:
            # True berarti memilih Bahasa Inggris
            lang = 'en'
        else:
            lang = 'id'

        # Simpan semua setting ke database
        adt.data_write(game_data)

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)


def GameLogin():
    """"bagian user ngasih nama"""
    global username
    global game_data
    global sound
    global lang

    #font = pg.font.Font(GAME_FONT, 20)
    font = pg.font.SysFont("Arial", 18)
    input_box = pg.Rect((GAME_WIDTH/2-100, GAME_HEIGHT/2), (200, 32))
    color_inactive = pg.Color(139, 195, 74)
    color_active = pg.Color(104, 159, 56)
    color = color_inactive
    active = False
    username = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    username = ''
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        GameHomePage()
                    elif event.key == pg.K_BACKSPACE:
                        username = username[:-1]
                    elif len(username) == 11:
                        username = username
                    else:
                        username += event.unicode


        gameDisplay.fill((225, 225, 225))
        # Render the current text.
        txt_surface = font.render(username, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(gameDisplay, color, input_box, 2)

        pgImage((GAME_WIDTH/2-100, GAME_HEIGHT/2-250), (200, 200), "assets/play-h.png")

        pgText(game_dict[lang]['enter_name'], (GAME_WIDTH/2, GAME_HEIGHT/2-40), 18)

        "Slider background musik"
        pgText(game_dict[lang]['sound'], (GAME_WIDTH/2-80, GAME_HEIGHT/2+160), 40)
        game_data['sound'] = pgSlider((GAME_WIDTH/2+80, GAME_HEIGHT/2+120), game_data['sound'])
        pgMusic()

        "Slider bahasa"
        pgText(game_dict[lang]['language'], (GAME_WIDTH/2-80, GAME_HEIGHT/2+90), 40)
        game_data['lang'] = pgSlider((GAME_WIDTH/2+80, GAME_HEIGHT/2+50), game_data['lang'])
        if game_data['lang']:
            lang = 'en'
        else:
            lang = 'id'

        adt.data_write(game_data)

        pg.display.flip()
        gameClock.tick(15)


def GameHistory():
    "bagian history"
    global game_dict

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        pgText(game_dict[lang]['history'], (GAME_WIDTH/2, 50), 50)
        pgParagraf(game_dict[lang]['history_text'], (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))
        pgButton((game_dict[lang]['next']), (GAME_WIDTH/2-100, GAME_HEIGHT-50), (200, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameInstruction)



        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)


def GameInstruction():
    """bagian cara bermain"""
    global game_dict

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHistory)

        pgText(game_dict[lang]['instruction'], (GAME_WIDTH/2, 50), 50)
        pgParagraf(game_dict[lang]['instruction_text'], (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))
        pgButton((game_dict[lang]['play_now']), (GAME_WIDTH/2-100, GAME_HEIGHT-100), (200, 50),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GamePlay)

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)


def GameSecret1():
    """the mathematics behind the game, part 1"""
    global game_dict

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        pgText(game_dict[lang]['secret'], (GAME_WIDTH/2, 50), 50)
        pgParagraf(game_dict[lang]['secret_text1'], (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))

        pgButton("1", (100, GAME_HEIGHT/2-130), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret1)
        pgButton("2", (100, GAME_HEIGHT/2-60), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret2)
        pgButton("3", (100, GAME_HEIGHT/2+10), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret3)
        pgButton("4", (100, GAME_HEIGHT/2+80), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret4)

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)
        
def GameSecret2():
    """the mathematics behind the game, part 1"""
    global game_dict

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        pgText(game_dict[lang]['secret'], (GAME_WIDTH/2, 50), 50)
        pgParagraf(game_dict[lang]['secret_text2'], (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))

        pgButton("1", (100, GAME_HEIGHT/2-130), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret1)
        pgButton("2", (100, GAME_HEIGHT/2-60), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret2)
        pgButton("3", (100, GAME_HEIGHT/2+10), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret3)
        pgButton("4", (100, GAME_HEIGHT/2+80), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret4)

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)
        
def GameSecret3():
    """the mathematics behind the game, part 1"""
    global game_dict

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        pgText(game_dict[lang]['secret'], (GAME_WIDTH/2, 50), 50)
        pgParagraf(game_dict[lang]['secret_text3'], (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))

        pgButton("1", (100, GAME_HEIGHT/2-130), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret1)
        pgButton("2", (100, GAME_HEIGHT/2-60), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret2)
        pgButton("3", (100, GAME_HEIGHT/2+10), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret3)
        pgButton("4", (100, GAME_HEIGHT/2+80), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret4)

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)
        
def GameSecret4():
    """the mathematics behind the game, part 1"""
    global game_dict

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameQuit()

        gameDisplay.fill(adt.color_use('background'))
        pgImage((10, 10), (80, 80), BACK_BUTTON, GameHomePage)

        pgText(game_dict[lang]['secret'], (GAME_WIDTH/2, 50), 50)
        pgParagraf(game_dict[lang]['secret_text4'], (GAME_WIDTH/2-250, 100, 500, GAME_HEIGHT))

        pgButton("1", (100, GAME_HEIGHT/2-130), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret1)
        pgButton("2", (100, GAME_HEIGHT/2-60), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret2)
        pgButton("3", (100, GAME_HEIGHT/2+10), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret3)
        pgButton("4", (100, GAME_HEIGHT/2+80), (50, 35),
                 adt.color_use('button_ok'), adt.color_use('button_ok_hover'), GameSecret4)

        # refresh tampilan game
        pg.display.update()
        gameClock.tick(15)


# ==========================================================================================
# Program Utama

global sound
global lang

# music
pg.mixer.init()
pg.mixer.music.load(BG_MUSIC)
pg.mixer.music.play(-1)

# variabel dummy untuk ngecek apakah user ngeklik mouse.
game_mouse_click = False    

# variabel yang berisi database program
game_data = adt.data_read() 

# initialisasi bahasa dari database
if game_data['lang']:
    lang = 'en'
else:
    lang = 'id'

#GamePlay()
GameLogin()
input()
