import pygame
import consoleHandling
import tilemap
from player import Player

class Game:
    def __init__(self):
        """
            State 0: Menu
            State 1: Game
            State 2: Pause
        """
        self.state = 1

        # Load spritesheet
        consoleHandling.printToGameConsole("Loading sprites.")
        try:
            self.spritesheet = pygame.image.load("spritesheet.png").convert_alpha()
        except pygame.error:
            consoleHandling.printToGameConsole("Error loading sprites.")

        # Cut spritesheet
        self.sprites = {}

        def appendSprite(spriteName, rects):
            sprite = []
            for r in rects:
                image = pygame.Surface(pygame.Rect(r).size, pygame.SRCALPHA).convert_alpha()
                image.blit(self.spritesheet, (0, 0), pygame.Rect(r))
                sprite.append(image)
            self.sprites[spriteName] = sprite

        # Tiles.
        tiles = (
            (0, 0, 32, 32),    # Standard tile.
        )
        appendSprite("tiles", tiles)
        # Player passive.
        playerPassive = (
            (0, 32, 32, 32),
            (0, 0, 0, 0)    # To remove error.
        )
        appendSprite("playerPassive", playerPassive)

        # Camera
        self.cameraX = 0
        self.cameraY = 0

        # Player
        self.player = Player()

    def updateGame(self, pg, pressed):
        # Update input.
        if pressed[pg.K_w]:
                self.player.y -= 5
        if pressed[pg.K_s]:
                self.player.y += 5
        if pressed[pg.K_a]:
                self.player.x -= 5
        if pressed[pg.K_d]:
                self.player.x += 5

        # Update camera. Camera will never view things out of the screen, so it will only be within the tilemap.
        # X value.
        if (self.player.x + (self.player.width / 2)) - (tilemap.gameWidth / 2) < 0:
            self.cameraX = 0
        elif (self.player.x + (self.player.width / 2)) + (tilemap.gameWidth / 2) > tilemap.columns * tilemap.tileWidth:
            self.cameraX = tilemap.columns * tilemap.tileWidth - tilemap.gameWidth
        else:
            self.cameraX = self.player.x + (self.player.width / 2) - (tilemap.gameWidth / 2)
        # Y value.
        if (self.player.y + (self.player.height / 2)) - (tilemap.gameHeight / 2) < 0:
            self.cameraY = 0
        elif (self.player.y + (self.player.height / 2)) + (tilemap.gameHeight / 2) > tilemap.rows * tilemap.tileHeight:
            self.cameraY = tilemap.rows * tilemap.tileHeight - tilemap.gameHeight
        else:
            self.cameraY = self.player.y + (self.player.height / 2) - (tilemap.gameHeight / 2)
