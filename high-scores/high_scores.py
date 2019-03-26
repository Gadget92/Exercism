class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        res = sorted(self.scores)
        return res[-1::-1] if len(res) <= 3 else res[-1:-4:-1]
