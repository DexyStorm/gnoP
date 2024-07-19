import pygame

#sets the game to fullscreen
def create_window():
   return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#returns a rect of the whole screen
def get_display_rect(screen):
   return screen.get_rect()

def get_display_size():
   return pygame.display.Info()
