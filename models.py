#! /usr/bin/env python3
import pygame as pg
import adt
from language import game_dict

GAME_FONT = "assets/fonto.ttf"

# Generic Block class
class Block(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def is_clicked(self):
        return pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())


# Game pos class
class Position(Block):
    def __init__(self, pos_index, color, width, height):
        Block.__init__(self, color, width, height)
        self.pos_index = pos_index
        self.discs = []


# Game discs class
class Disc(Block):
    def __init__(self, current_pos, id, color, width, height):
        Block.__init__(self, color, width, height)
        self.current_pos = current_pos
        self.id = id


# Buttons class
class Button(Block):
    def __init__(self, text, color, width, height, text_color=adt.color_use("black"), text_size=30, text_font=GAME_FONT):
        Block.__init__(self, color, width, height)
        self.text = text
        self.text_color = text_color
        self.font = pg.font.SysFont(text_font, text_size, False, False)
        self.text_render = self.font.render(text, 1, text_color)
        self.value = None

    def set_value(self, value):
        self.value = value

    def render_text(self):
        w = (self.width/2-(self.text_render.get_width()/2))
        h = (self.height/2-(self.text_render.get_height()/2))
        self.image.blit(self.text_render, [w, h])


# Main Menu
class MainMenu():


    def __init__(self, GAME_WIDTH, GAME_HEIGHT):

        game_data = adt.data_read() # baca database

        if game_data['lang']:
            lang = 'en'
        else:
            lang = 'id'

        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.sprites_list = pg.sprite.Group()
        self.btn_discs = []

        self.label = Button(game_dict[lang]['number_discs'],
                            adt.color_use("background"),
                            GAME_WIDTH/2, GAME_HEIGHT/3-150)

        self.label.rect.x = self.GAME_WIDTH/4
        self.label.rect.y = self.GAME_HEIGHT/2 - 60
        
        # pilihan menu
        for i in range(3, 8):
            btn = Button(str(i), adt.color_use("button_ok"), 20, 30)
            btn.rect.x = self.GAME_WIDTH/3 + 50*(i-2) - 12
            btn.rect.y = self.GAME_HEIGHT/2
            btn.render_text()
            btn.set_value(i)
            self.btn_discs.append(btn)

        self.sprites_list.add(self.btn_discs)

        self.label.render_text()
        self.sprites_list.add(self.label)

        # Game over buttons
        self.btn_play_again = Button(game_dict[lang]['play_again'],
                                     adt.color_use("button_ok"),
                                     len(game_dict[lang]['play_again'])*14, 30)
        
        self.btn_return = Button(game_dict[lang]['change_disc'],
                                 adt.color_use("button_normal"),
                                 len(game_dict[lang]['change_disc'])*12, 30)

        self.btn_quit = Button(game_dict[lang]['main_menu'],
                               adt.color_use("button_normal"),
                               len(game_dict[lang]['main_menu'])*14, 30)

        self.btn_play_again.rect.x = self.GAME_WIDTH/2 - (self.btn_return.image.get_width()) - 25
        self.btn_play_again.rect.y = self.GAME_HEIGHT/2 - 40
        self.btn_play_again.render_text()

        self.btn_return.rect.x = self.GAME_WIDTH/2 - self.btn_return.image.get_width()/2
        self.btn_return.rect.y = self.GAME_HEIGHT/2 - 40
        self.btn_return.render_text()

        self.btn_quit.rect.x = self.GAME_WIDTH/2 + (self.btn_return.image.get_width())/2 + 14
        self.btn_quit.rect.y = self.GAME_HEIGHT/2 - 40
        self.btn_quit.render_text()


# Game main class
class Game():
    def __init__(self, GAME_WIDTH, GAME_HEIGHT):
        # Game sprites groups
        self.sprites_list = pg.sprite.Group()
        self.pos_sprites_list = pg.sprite.Group()

        # Game constants
        self.BOARD_WIDTH = GAME_WIDTH/2
        self.BOARD_HEIGHT = 50
        self.BOARD_X = GAME_WIDTH * 0.25
        self.BOARD_Y = GAME_HEIGHT - 55
        self.POS_WIDTH = 20
        self.POS_HEIGHT = 200
        self.DISC_WIDTH = 200
        self.DISC_HEIGHT = self.POS_WIDTH

        # pos and discs lists
        self.pos = []
        self.discs = []

        # Draw the game board and it's pos
        self.game_board = Block(adt.color_use("board_color"), self.BOARD_WIDTH, self.BOARD_HEIGHT)
        self.game_board.rect.x = self.BOARD_X
        self.game_board.rect.y = self.BOARD_Y
        first_pos = Position(0, adt.color_use("board_color"), self.POS_WIDTH, self.POS_HEIGHT)
        first_pos.rect.x = self.BOARD_X
        first_pos.rect.y = self.BOARD_Y - self.POS_HEIGHT
        second_pos = Position(1, adt.color_use("board_color"), self.POS_WIDTH, self.POS_HEIGHT)
        second_pos.rect.x = (self.BOARD_X + (self.BOARD_WIDTH/2)) - (self.POS_WIDTH/2)
        second_pos.rect.y = self.BOARD_Y - self.POS_HEIGHT
        third_pos = Position(2, adt.color_use("board_color"), self.POS_WIDTH, self.POS_HEIGHT)
        third_pos.rect.x = (self.BOARD_X + self.BOARD_WIDTH) - self.POS_WIDTH
        third_pos.rect.y = self.BOARD_Y - self.POS_HEIGHT
        self.pos = [first_pos, second_pos, third_pos]
        self.sprites_list.add([self.game_board, self.pos])
        self.pos_sprites_list.add(self.pos)

    # Set discs number and mim movements
    def set_n_discs(self, n_discs):
        self.n_discs = n_discs
        self.min_moves = ((2**self.n_discs)-1)

    # Draw discs method
    def draw_discs(self):
        DISC_WIDTH = 200
        DISC_HEIGHT = self.POS_WIDTH
        
        for i in range(0, self.n_discs):
            scale = 1/(i+1)
            zzz = int((DISC_WIDTH*scale))
            
            if i % 2 == 0:
                disc = Disc(0,i,adt.color_random(),(DISC_WIDTH/(i+1)),DISC_HEIGHT)
            else:
                disc = Disc(0,i,adt.color_random(),(DISC_WIDTH/(i+1)),DISC_HEIGHT)
            disc.rect.x = self.BOARD_X - ((zzz/2)-(DISC_HEIGHT/2))
            disc.rect.y = (self.BOARD_Y - DISC_HEIGHT) - (DISC_HEIGHT*i)
            self.discs.append(disc)
            self.pos[0].discs.append(disc)

        self.sprites_list.add(self.discs)
		
		
