import pygame
from screen import *
import random

class Ball():
   def __init__(self):

      display_size = get_display_size()

      self.posx = display_size.current_w/2
      self.posy = display_size.current_h/2
      self.width = display_size.current_h/30
      self.height = display_size.current_h/30
      self.direction = random.randint(1, 4) #determins the direction
      #self.direction = 4 #for debugging
      self.color = (255, 255, 255)
      self.ball_rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

   
   def draw(self, screen):
      pygame.draw.rect(screen, self.color, self.ball_rect)


   #movement for the ball
   def movement(self, top_border, bottom_border, left_border, right_border,  player_obj, enemy_obj):
      

      if(self.ball_rect.colliderect(player_obj.player_rect)):
         #print("collided with player")
         if(self.direction == 3):
            self.direction = 2
         if(self.direction == 4):
            self.direction = 1


      if(self.ball_rect.colliderect(enemy_obj.enemy_rect)):
         #print("collided with enemy")
         if(self.direction == 1):
            self.direction = 4
         if(self.direction == 2):
            self.direction = 3 

      
      if(self.ball_rect.colliderect(top_border)):
         #print("COLIDED WITH TOP")
         if(self.direction == 1):
            self.direction = 2
         if(self.direction == 4):
            self.direction = 3


      if(self.ball_rect.colliderect(bottom_border)):
         #print("COLIDED WITH BOTTOM")
         if(self.direction == 2):
            self.direction = 1
         if(self.direction == 3):
            self.direction = 4


      if(self.ball_rect.colliderect(left_border)):
         #print("collided with left border")
         #print("old enemy score is:", enemy_obj.score)
         enemy_obj.score = enemy_obj.score + 1
         #print("new enemy score is:", enemy_obj.score)
         self.reset()

      if(self.ball_rect.colliderect(right_border)):
         #print("collided with right border")
         #print("old player score is:", player_obj.score)
         player_obj.score = player_obj.score + 1
         #print("new player score is:", player_obj.score)
         self.reset()



      if(self.direction == 1):
         self.ball_rect.move_ip(1, -1)
      elif(self.direction == 2):
         self.ball_rect.move_ip(1, 1)
      elif(self.direction == 3):
         self.ball_rect.move_ip(-1, 1)
      elif(self.direction == 4):
         self.ball_rect.move_ip(-1, -1)


   def reset(self):
      self.direction = random.randint(1,4)
      self.ball_rect.x = get_display_size().current_w/2
      self.ball_rect.y = get_display_size().current_h/2


