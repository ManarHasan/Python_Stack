class ninja:
    def __init__(self, username, x, y):
        self.username = username
        self.x = x
        self.y = y
        self.snowball = snowball(x=x, y=y)  # click s for snowball
        self.experience = 0
        if self.experience == 10:
            # if you click w:
            self = wizard()
            # if you click q:
            self = warrior()

    def level(self):
        # everytime you throw a snowball(click s)
        self.experience += 1

    def moveRight(self):
        self.x = self.x + 1

    def moveLeft(self):
        self.x = self.x - 1

    def moveUp(self):
        self.y = self.y - 1

    def moveDown(self):
        self.y = self.y + 1


class snowball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x = 10


class fireball:
    def __init__(self, x, y):  # like snowball but with a different color
        self.x = x
        self.y = y
        self.color = red

    def move(self):
        self.x = 10


class wizard(ninja):
    def __init__(self):
        self.fireball = fireball(x=x, y=y)  # click f for fireball


class warrior(ninja):
    def __init__(self):
        self.sword = sword(x=x, y=y)  # click a for sword


moh = ninja("mohammad", 50, 50)
moh.moveRight()
print(moh.x)
moh.snowball.move()
print(moh.snowball.x)
