gameVersion = "v0.0.4"

#######################################
############ New Direction ############
#######################################

# Avoid displaying pygame standard start message.
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import math
from game import Game
import consoleHandling
import tilemap

def renderTilemap(offsetX, offsetY):
    row = 1
    column = 1
    tileX = 0
    tileY = 0
    for i in range(len(tilemap.tilemap)):
        # Tile to render.
        renderTile = tilemap.tilemap[i]

        # Draw tile (but only those inside of the screen).
        if ((tileX + tilemap.tileWidth) >= offsetX and tileX <= (offsetX + tilemap.gameWidth) and   # X values.
        (tileY + tilemap.tileHeight) >= offsetY and tileY <= (offsetY + tilemap.gameHeight)):       # Y values.
            # Do not draw anything if it is an empty tile.
            if renderTile > 0:
                sprite = game.sprites['tiles'][renderTile - 1]
                screen.blit(sprite, (tileX - offsetX, tileY - offsetY))

        # Go to next tile.
        if column != tilemap.columns:
            column += 1
            tileX += tilemap.tileWidth
        else:
            column = 1
            tileX = 0
            tileY += tilemap.tileHeight
            row += 1

def renderGame():
    # Clear screen.
    screen.fill((0,0,0))
    # Render tilemap.
    renderTilemap(game.cameraX, game.cameraY)
    # Render player.
    screen.blit(game.sprites['playerPassive'][0], (game.player.x - game.cameraX, game.player.y - game.cameraY))
    # Render FPS counter in top right corner.
    FPSFont = pygame.font.SysFont("helvetica", 10)
    currentFPS = "FPS: {}".format(round(clock.get_fps()))
    renderFPS = FPSFont.render(currentFPS, 1, (255,255,0))
    screen.blit(renderFPS, (tilemap.gameWidth - renderFPS.get_width(), 0))

# Init game.
pygame.init()
consoleHandling.printToGameConsole("Starting game.")
try:
    pygame.display.set_icon(pygame.image.load("icon.gif"))   # Set icon, before set_mode to avoid errors.
except pygame.error:
    consoleHandling.printToGameConsole('Could not load "icon.gif".')
pygame.display.set_caption('New Direction ' + gameVersion)
screen = pygame.display.set_mode((tilemap.gameWidth, tilemap.gameHeight))
# Initialize font. Called after 'pygame.init()' to avoid 'Font not Initialized' error.
standardGameFont = pygame.font.SysFont("helvetica", 15)
# Make game object.
game = Game()
# Init clock to handle timing.
clock = pygame.time.Clock()

# When gameRunning is False, game will end and exit.
gameRunning = True

# Game loop.
while gameRunning:
    for event in pygame.event.get():
        # Quitting game.
        if event.type == pygame.QUIT:
            consoleHandling.printToGameConsole("Exiting game.")
            gameRunning = False
        # Pause game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game.togglePause()

    # Key handling.
    pressed = pygame.key.get_pressed()

    # Update game.
    game.updateGame(pygame, pressed)

    # Render game.
    renderGame()
    pygame.display.flip()

    # Cap max FPS.
    clock.tick(60)
