import string
import random

robot_names = []


class Robot(object):
    def __init__(self):
        self.name = self.get_robot_name()

    def get_robot_name(self, char_length=3, number_length=3):
        res = ''.join(random.choice(string.ascii_uppercase) for i in range(char_length)) + \
               ''.join(random.choice(string.digits) for i in range(number_length))
        return res

    def reset(self):
        self.name = self.get_robot_name()
