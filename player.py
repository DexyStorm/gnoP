import pygame
import screen
from screen import *

class Player:
   def __init__(self):

      display_size = get_display_size()

      self.posx = display_size.current_w*0.02
      self.posy = display_size.current_h/2
      self.width = display_size.current_w/100
      self.height = display_size.current_h/7
      self.score = 0
      self.color = (255, 255, 255)
      self.player_rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
      

   def increase_player_score(self):
      self.score = self.score + 1

   
   def draw(self, screen):
      pygame.draw.rect(screen, self.color, self.player_rect)

   def player_movement(self, screen_rect):
      key = pygame.key.get_pressed()
      if key[pygame.K_s] == True:
         self.player_rect.move_ip(0, 1)
      if key[pygame.K_w] == True:
         self.player_rect.move_ip(0, -1)
      
      #makes it so that the player cannot escape the screen
      self.player_rect.clamp_ip(screen_rect)

