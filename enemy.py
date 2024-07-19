import pygame
import screen
from screen import *

class Enemy:
   def __init__(self):

      display_size = get_display_size()

      self.posx = display_size.current_w*0.98-30
      self.posy = display_size.current_h/2
      self.width = display_size.current_w/100
      self.height = display_size.current_h/7
      self.score = 0
      self.color = (255, 255, 255)
      self.enemy_rect = pygame.Rect(self.posx, self.posy, self.width, self.height)


   def increase_enemy_score(self):
      self.score = self.score + 1


   def draw(self, screen):
      pygame.draw.rect(screen, self.color, self.enemy_rect)


   def enemy_movement(self, screen_rect, ball_rect):
      if(ball_rect.x >= get_display_size().current_w/1.5):
         #print(ball_rect.x)
         if(ball_rect.y > self.enemy_rect.y): #if the ball is above the enemy
            self.enemy_rect.move_ip(0, 1)
         elif(ball_rect.y < self.enemy_rect.y): #if the ball is under the enemy
            self.enemy_rect.move_ip(0, -1)

      #makes it so that the enemy cannot escape the screen
      self.enemy_rect.clamp_ip(screen_rect)


