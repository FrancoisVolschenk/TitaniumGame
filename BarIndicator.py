from CONSTANTS import *


class BarIndicator(pygame.sprite.Sprite):
    """This class represents the GUI elements that appear as bars above 
    the heads of characters. Red indicates health, blue indicates energy
    Note to self: Use visitor design pattern to hook into Character's update function 
    to remove the necessity of calling draw for this class"""
    def __init__(self, entity):
        pygame.sprite.Sprite.__init__(self)
        self.entity = entity # attach to a character

        # 4 bars, 2 indicate the area that the full bar takes up
        # and 2 indicate the actual value
        self.healthtube = pygame.rect.Rect(entity.rect.left, entity.rect.top - 10, BLOCK_SIZE, 5)
        self.healthindicator = pygame.rect.Rect(entity.rect.left, entity.rect.top - 10, int(BLOCK_SIZE / entity.health), 5)
        self.energytube = pygame.rect.Rect(entity.rect.left, entity.rect.top - 5, BLOCK_SIZE, 5)
        self.energyindicator = pygame.rect.Rect(entity.rect.left, entity.rect.top - 5, int(BLOCK_SIZE / entity.energy), 5)

    def draw(self, screen):
        # update based on character's position and current health and energy status
        self.healthtube.topleft = (self.entity.rect.left, self.entity.rect.top - 10)
        self.healthindicator.topleft = (self.entity.rect.left, self.entity.rect.top - 10)
        self.energytube.topleft = (self.entity.rect.left, self.entity.rect.top - 5)
        self.energyindicator.topleft = (self.entity.rect.left, self.entity.rect.top - 5)

        self.healthindicator.width = int(BLOCK_SIZE * (self.entity.health / 100))
        self.energyindicator.width = int(BLOCK_SIZE * (self.entity.energy / 100))

        # Draw onto screen
        pygame.draw.rect(screen, TUBE, self.healthtube)
        pygame.draw.rect(screen, HEALTH, self.healthindicator)
        pygame.draw.rect(screen, TUBE, self.energytube)
        pygame.draw.rect(screen, ENERGY, self.energyindicator)