import pygame

import player
from player import *
import enemy
from enemy import*
import ball
from ball import *
from screen import *





def main():
   
   running = True

   pygame.init()
   pygame.font.init()

   pygame.display.set_caption("gnoP")

   #creates window. is in screen.py
   screen = create_window()


   #needed for initializing players
   #just returns the display height and width
   #display_size = get_display_size()
   
   #creates player
   player_obj = player.Player()

   #creates enemy
   enemy_obj = enemy.Enemy()

   #creates ball
   ball_obj = ball.Ball()

   #neede to keep the player on the screen
   screen_rect = get_display_rect(screen)

   top_border = pygame.Rect(0, 1, get_display_size().current_w, 1)
   bottom_border = pygame.Rect(0, get_display_size().current_h, get_display_size().current_w, 1)
   left_border = pygame.Rect(0, 0, 1, get_display_size().current_h)
   right_border = pygame.Rect(get_display_size().current_w-1, 0, 1, get_display_size().current_h)

   score_font = pygame.font.SysFont('Comic Sans', 60)

   #main gameplay loop
   while(running):

      #needs to be done on every iteration
      #thats why its in the gameplay loop
      screen.fill((0, 0, 0))

      player_obj.draw(screen)

      enemy_obj.draw(screen)

      ball_obj.draw(screen)

      player_obj.player_movement(screen_rect)

      enemy_obj.enemy_movement(screen_rect, ball_obj.ball_rect)

      ball_obj.movement(top_border, bottom_border, left_border, right_border,  player_obj, enemy_obj)


      player_score = score_font.render(str(player_obj.score), False, (0, 255, 0))
      enemy_score = score_font.render(str(enemy_obj.score), False, (0, 255, 0))
      screen.blit(player_score, (get_display_size().current_w/4, get_display_size().current_h/100))
      screen.blit(enemy_score, (get_display_size().current_w/4*3, get_display_size().current_h/100))


      for event in pygame.event.get():
         if(event.type == pygame.QUIT):
            running = False

      pygame.display.update()





















if (__name__ == "__main__"):
   main()
   pygame.quit()