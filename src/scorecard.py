

class Scorecard:

    def __init__(self, scorecard):
        self.score = []
        self.scorecard = scorecard
        self.total_score = 0
        self.last_frame_size = 0

    def create_list_of_numeric_scores(self):
        for throw in range(len(self.scorecard)):
            if self.scorecard[throw] == 'X':
                self.score.append(10)
            elif self.scorecard[throw] == '/' and self.scorecard[throw-1] == '-':
                self.score.append(10)
            elif self.scorecard[throw] == '/':
                self.score.append(10 - int(self.scorecard[throw-1]))
            elif self.scorecard[throw] == '-':
                self.score.append(0)
            else:
                self.score.append(int(self.scorecard[throw]))

    def calculate_last_frame_size(self):
        x = 0
        for throw in range(len(self.scorecard)):
            if self.scorecard[throw] == 'X':
                x += 2
            else:
                x += 1
            if x == 18:
                self.last_frame_size = len(self.scorecard) - throw - 1
    

    def add_spare_and_strike(self):
        for throw in range(len(self.scorecard)):
            if self.scorecard[throw] == 'X' and throw < len(self.scorecard) - self.last_frame_size:
                self.score[throw] += self.score[throw + 1] + self.score[throw + 2]
            elif self.scorecard[throw] == '/' and throw < len(self.scorecard) - self.last_frame_size:
                self.score[throw] += self.score[throw + 1]
            else:
                pass

    def calculate_total_score(self):
        for throw in range(len(self.score)):
            self.total_score += self.score[throw]
        return self.total_score
    
    def get_total_score(self):
        self.create_list_of_numeric_scores()
        self.calculate_last_frame_size()
        self.add_spare_and_strike()
        return self.calculate_total_score()



if __name__ == '__main__':


    ejemplo = Scorecard('XXXXXXXXXXXX')
    print(ejemplo.get_total_score())
