import pygame
from constants import *
import pickle


class GameData(object):

    screen = None
    font = None
    distance_between = 0
    high_score = 0

    def __init__(self, screen):
        super(GameData, self).__init__()

        self.screen = screen
        self.score = Score()
        self.font = pygame.font.Font(None, 30)

    def update(self):
        high_score_str = "high score: {: >10d}".format(self.score.high_total)

        high_score_text = self.font.render(
            high_score_str,
            True,
            (255, 255, 255))

        pos = (WINDOW_WIDTH -
               high_score_text.get_width() -
               10,
               10)

        self.screen.blit(high_score_text, pos)

        score_str = "score: {: >10d}".format(self.score.total)
        score_text = self.font.render(
            score_str,
            True,
            (255, 255, 255))

        pos = (WINDOW_WIDTH -
               score_text.get_width() -
               high_score_text.get_width() -
               100,
               10)

        self.screen.blit(score_text, pos)


class Score(object):
    total = 0
    high_total = 0
    filename = 'data.dat'

    def __init__(self):
        super(Score, self).__init__()
        try:
            self.load_from_disk()
        except IOError:
            self.save_to_disk(0)

    def modify_score(self, amount, increase=True):
        if increase:
            self.total += amount
            if self.total > self.high_total:
                self.high_total = self.total
                self.save_to_disk()
        else:
            self.total -= amount

    def load_from_disk(self):
        file_obj = open(self.filename, 'r')
        self.high_total = pickle.load(file_obj)

    def save_to_disk(self):
        file_obj = open(self.filename, 'wb')
        pickle.dump(self.high_total, file_obj)