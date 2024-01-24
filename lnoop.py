import random

Colors = ["white", "yellow", "purple", "red"]


class Ghost(object):
    color = None

    def __init__(self):
        self.color = random.choice(Colors)


ghosts = [Ghost().color for _ in range(10)]
print(ghosts.count("white"))
