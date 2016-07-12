class NonSprite(object):

    screen = None

    def __init__(self):
        super(NonSprite, self).__init__()

    def draw(self, screen):
        pass

    def update_data(self, data):
        pass