# The character class is used as a super class in the enemy and player class.
class Character:
    def __init__(self, x=0, y=0, movementSpeed=0):  # Arguments are optinal.
        self.x = x
        self.y = y
        self.movementSpeed = movementSpeed

        self.width = 32
        self.height = 32
        self.xVelocity = 0
        self.yVelocity = 0
        self.diagonalVelocityMultiplier = 0.7071    # Constant x and y velocity is multiplied with when moving diagonal (45 degrees).

    def collisionWithObject(self, object):  # Check collision with other class object with Character as super class.
        pass
