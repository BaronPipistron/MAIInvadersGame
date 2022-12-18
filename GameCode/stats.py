class Stats:
    """game statistics tracking"""

    def __init__(self):
        """initializes statistics"""
        self.reset_stats()
        self.run_game = True
        with open('Scores/HighScore.txt', 'r') as fp:
            self.high_score = int(fp.readline())

    def reset_stats(self):
        """statistics that change during the game"""
        self.guns_loss = 3
        self.score = 0
