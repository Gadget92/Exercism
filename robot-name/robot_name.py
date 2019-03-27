import string
import random

robot_names = []


class Robot(object):
    def __init__(self):
        self.name = self.get_valid_name()

    def reset(self):
        self.name = self.get_valid_name()

    def get_valid_name(self):
        name_in_list = True
        robot_name = ''
        while name_in_list:
            robot_name = self.get_name()
            if robot_name not in robot_names:
                name_in_list = False
        return robot_name

    def get_name(self, char_length=3, number_length=3):
        res = ''.join(random.choice(string.ascii_uppercase) for i in range(char_length)) + \
               ''.join(random.choice(string.digits) for i in range(number_length))
        return res

