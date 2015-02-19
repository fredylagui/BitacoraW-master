# -*- coding: utf-8 *-*
# input lib
from pygame.locals import *
import pygame, string

class ConfigError(KeyError): pass

class Config:
    """ A utility for configuration """
    def __init__(self, options, *look_for):
        assertions = []
        for key in look_for:
            if key[0] in options.keys(): exec('self.'+key[0]+' = options[\''+key[0]+'\']')
            else: exec('self.'+key[0]+' = '+key[1])
            assertions.append(key[0])
        for key in options.keys():
            if key not in assertions: raise ConfigError(key+' not expected as option')

class Input:
    """ A text input for pygame apps """
    def __init__(self, **options):
        """ Options: x, y, font, color, restricted, maxlength, prompt """
        self.options = Config(options, ['x', '0'], ['y', '0'], ['font', 'pygame.font.Font(None, 32)'],
                              ['color', '(0,0,0)'], ['restricted', '\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\\\'()*+,-./:;<=>?@[\]^_`{|}~\''],
                              ['maxlength', '-1'], ['prompt', '\'\''])
        self.x = self.options.x; self.y = self.options.y
        self.font = self.options.font
        self.color = self.options.color
        self.restricted = self.options.restricted
        self.maxlength = self.options.maxlength
        self.prompt = self.options.prompt; self.value = ''
        self.shifted = False
        self.pause = 0
    
    def set_pos(self, x, y):
        """ Set the position to x, y """
        self.x = x
        self.y = y

    def set_font(self, font):
        """ Set the font for the input """
        self.font = font

    def draw(self, surface):
        """ Draw the text input to a surface """
        text = self.font.render(self.prompt+self.value, 1, self.color)
        surface.blit(text, (self.x, self.y))
        
    def draw_pwd(self,surface):
        """ Draw the text input to a surface in mode pwd"""
        tmp = ""
        for i in self.value:
            tmp = tmp+"*"
        text = self.font.render(self.prompt+tmp, 1, self.color)
        surface.blit(text, (self.x, self.y))

    def reset_input(self):
        self.value = ""
        
    def update_prompt(self,msg):
        self.prompt = msg
        
    def getTxt(self):
        return self.value

    def update(self, events,sistemaop):
        """ Update the input based on passed events """
        pressed = pygame.key.get_pressed() #Add hability to hold down delete  key and delete text
        if self.pause == 3 and pressed[K_BACKSPACE]:
            self.pause = 0
            self.value = self.value[:-1]
        elif pressed[K_BACKSPACE]:
            self.pause += 1
        else:
            self.pause = 0 
            
        for event in events:
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: self.value = self.value[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
                elif event.key == K_SPACE: self.value += ' '
                else:
                    #print 'keydown', event.unicode, "Code", event.scancode
                    "Se tecleo cualquier otra tecla que no es TAB ni ENTER"
                    if sistemaop == "win32":
                        if event.scancode != 15 and event.scancode != 28:
                            self.value += u"" + event.unicode                            
                    elif sistemaop == "linux2":
                        if event.scancode != 23 and event.scancode != 36:
                            self.value += u"" + event.unicode

        if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]
