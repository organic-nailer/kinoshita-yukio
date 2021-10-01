from Responder import *
from Dictionary import *

class Emotion:

    MOOD_MIN = -20
    MOOD_MAX = 10

    MOOD_RECOVERY = 0.5

    def __init__(self, dictionary):

        self.dictionary = dictionary

        self.mood = 0

    def update(self,input):

        for ptn_item in self.dictionary.pattern:

            if ptn_item.match(input):

                self.adjust_mood(ptn_item.modify)
                break


        if self.mood < 0:

            self.mood += Emotion.MOOD_RECOVERY

        else:

            self.mood -= Emotion.MOOD_RECOVERY

    def adjust_mood(self,val):

        self.mood += int(val)

        if self.mood > Emotion.MOOD_MAX:

            self.mood = Emotion.MOOD_MAX

        elif self.mood < Emotion.MOOD_MIN:

            self.mood = Emotion.MOOD_MIN







