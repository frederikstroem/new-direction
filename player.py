from character import Character
import tilemap

# Player inherits Character class.
class Player(Character):
    def __init__(self):
        super().__init__()

        # Reset to default values when class i constructed.
        self.reset()

    def reset(self):    # Reset player to standard values.
        self.x = 32 * 15
        self.y = 32 * 15
        self.movementSpeed = 5

    def collidingWithTilemap(self):
        row = 1
        column = 1
        tileX = 0
        tileY = 0
        for i in range(len(tilemap.tilemap)):
            tile = tilemap.tilemap[i]
            
            # Inspired by https://developer.mozilla.org/kab/docs/Games/Techniques/2D_collision_detection.
            if (self.x <= tileX + tilemap.tileWidth and
            self.x + self.width >= tileX and
            self.y <= tileY + tilemap.tileHeight and
            self.height + self.y >= tileY):
                # Collide only with empty space or borders.
                if tile == 0:
                    return True

            # Go to next tile.
            if column != tilemap.columns:
                column += 1
                tileX += tilemap.tileWidth
            else:
                column = 1
                tileX = 0
                tileY += tilemap.tileHeight
                row += 1
        
        # Collide only with empty space or borders.
        if (self.x <= 0 or
        self.x + self.width >= tilemap.gameWidth or
        self.y <= 0 or
        self.y + self.height >= tilemap.gameHeight):
            return True

        # If not colliding, return False.
        return False
