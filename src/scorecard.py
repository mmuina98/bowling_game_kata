

class ScoreCard:

    def __init__(self, scorecard):
        self.numeric_score = []
        self.scorecard = scorecard
        self.total_score = 0
        self.last_frame_size = 0

    def get_numeric_score(self, position = None):
        if position == None:
            return self.numeric_score
        else:
            return self.numeric_score[position]

    def create_list_of_numeric_scores(self):
        for throw in range(len(self.scorecard)):
            if self.scorecard[throw] == 'X':
                self.get_numeric_score().append(10)
            elif self.scorecard[throw] == '/' and self.scorecard[throw-1] == '-':
                self.get_numeric_score().append(10)
            elif self.scorecard[throw] == '/':
                self.get_numeric_score().append(10 - int(self.scorecard[throw-1]))
            elif self.scorecard[throw] == '-':
                self.get_numeric_score().append(0)
            else:
                self.get_numeric_score().append(int(self.scorecard[throw]))

    def calculate_last_frame_size(self):
        frame = 0
        for throw in range(len(self.scorecard)):
            if self.scorecard[throw] == 'X':
                frame += 1
            else:
                frame += 0.5
            if frame == 9:
                self.last_frame_size = len(self.scorecard) - throw - 1
    
    def add_to_numeric_scores(self, position, addition):
        self.numeric_score[position] += addition

    def add_spare_and_strike(self):
        for throw in range(len(self.scorecard)):
            if self.scorecard[throw] == 'X' and throw < len(self.scorecard) - self.last_frame_size:
                self.add_to_numeric_scores(throw, self.get_numeric_score(throw + 1) + self.get_numeric_score(throw + 2)) 
            elif self.scorecard[throw] == '/' and throw < len(self.scorecard) - self.last_frame_size:
                self.add_to_numeric_scores(throw, self.get_numeric_score(throw + 1))  
            else:
                pass

    def calculate_total_score(self):
        for throw in range(len(self.get_numeric_score())):
            self.total_score += self.get_numeric_score()[throw]
        return self.total_score
    
    def get_total_score(self):
        self.create_list_of_numeric_scores()
        self.calculate_last_frame_size()
        self.add_spare_and_strike()
        return self.calculate_total_score()



if __name__ == '__main__':


    ejemplo = ScoreCard('XXXXXXXXXXXX')
    print(ejemplo.get_total_score())
