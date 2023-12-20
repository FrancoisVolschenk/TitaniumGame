from CONSTANTS import *               # All constant values (Indicated by all caps)
from Character import Commet, Enemy   # The character classes (Needs a lot of cleaning up and propper OOP practices)
from Projectile import *              # Used to let Commet Shoot
from BarIndicator import BarIndicator # Used for the health and energy bars

# This determines how fast the game loop runs
clock = pygame.time.Clock()

# Surface for displaying graphics
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Titanium")

# Right now the last argument simply acts as a skin, but this will change later on to ensure seperation of abilities between heroes
player = Commet(200, 200, 3, "commet")
p_moving_L = False # Used to check if the player is moving.
p_moving_R = False
shoot = False      # Used to trigger the shoot action. This will change when I clean up the character class to trigger each hero's own ability
p_indicator = BarIndicator(player) # Link a bar indicator to this character

# Dummy character created for testing
red = Enemy(200, 250, 3, "red")
e_indicator = BarIndicator(red)
entities = [red] # when adding more characters, add them to this list to have them appear on screen

indicators = [p_indicator, e_indicator] # all bar indicators must be added here to work properly. Will improve on this later. (Note to self: Use visitor design pattern to hook bar indicator into entity's update function)

run = True

while run:
    clock.tick(FPS)
    screen.fill((255, 255, 255)) # clean the screen of current state
    pygame.draw.line(screen, (0, 0, 0), (0, GROUND), (SCREEN_WIDTH, GROUND)) # draw ground

    # Player actions
    if player.alive:
        # Determine which animation should be shown (If more animations are added, they must be added in CONSTANTS-> ACTION)
        if shoot:
            player.update_action(ACTION["SHOOT"])
            player.do_action()
        elif player.airborne:
            player.update_action(ACTION["JUMP"])
        elif p_moving_L or p_moving_R:
            player.update_action(ACTION["RUN"])
        else:
            player.update_action(ACTION["IDLE"])
        player.move(p_moving_L, p_moving_R)

        player.draw(screen)
        player.update()
    
    # Update all other entities
    for e in entities:
        e.move()
        e.update()
        e.draw(screen)

    # Update bar indicators
    for i in indicators:
        i.draw(screen)

    # Update all projectiles using built in mechanism from pygame
    projectile_group.update()
    projectile_group.draw(screen)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Window is closed
            run = False
        
        if event.type == pygame.KEYDOWN: # keys are pressed
            if event.key == pygame.K_a:
                p_moving_L = True
            if event.key == pygame.K_d:
                p_moving_R = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key == pygame.K_SPACE:
                shoot = True

        if event.type == pygame.KEYUP: # keys are released
            if event.key == pygame.K_a:
                p_moving_L = False
            if event.key == pygame.K_d:
                p_moving_R = False
            if event.key == pygame.K_SPACE:
                shoot = False

    pygame.display.update() # Refresh the screen to show new content

pygame.quit() # release system resources properly