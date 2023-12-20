import pygame

pygame.init() # must be the first line of code that executes. This is achieved by importing CONSTANTS first in main.py

# World values
FPS = 60 # frames per second
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
BLOCK_SIZE = 60
GROUND = SCREEN_HEIGHT - BLOCK_SIZE 
GRAVITY = 0.75

# Projectile images
hot_projectile = pygame.image.load("img/icons/hot_projectile.png")
cold_projectile = pygame.image.load("img/icons/cold_projectile.png")
# consider scaling the images down
PROJ_IMG = {"hot": hot_projectile,
            "cold": cold_projectile}

# Character values
ACTION = {"IDLE": 0,
          "RUN": 1,
          "JUMP": 2,
          "SHOOT": 3}
# NB: If new actions are added, they must be added to this dict for animation purposes

RESTORE_RATE = 0.2 # rate at which energy restores
FULL = 100 # when to stop restoring health and energy
ANIM_COOLDOWN = 100 # cooldown timer between animation frames

# COLOURS
TUBE = (50, 50, 50)
HEALTH = (255, 0, 0)
ENERGY = (0, 0, 255)