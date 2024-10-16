from dateutil import parser

class Workout(object):
    cal_per_hr = 200
    
    def __init__(self, start, end, calories = None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = '😊'
        self.kind = 'Work'
        
    def get_calories(self):
        if self.calories == None:
            return Workout.cal_per_hr*(self.end - self.start).total_seconds()/3600
        else:
            return self.calories
        
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_duration(self):
        return self.end -  self.start
    def set_calories(self, calories):
        self.calories = calories
    def set_start(self, start):
        self.start = parser.parse(start)
    def set_end(self, end):
        self.end = parser.parse(end)
    
    def __str__(self):
        width = 16
        retstr = f"|{'`'*width}|\n"
        retstr += f"|{' '*width}|\n"
        iconLen = 0
        retstr += f"| {self.icon}{' ' * (width - 3)}|\n"
        retstr += f"| {self.kind}{' ' * (width - len(self.kind) - 1)}|\n"
        retstr += f"|{' '*width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' ' * (width - len(duration_str) - 1)}|\n"
        calstr = f"{self.get_calories():.0f}"
        retstr += f"| {calstr} Calories{' '* (width - len(calstr)-10)}|\n"
        retstr += f"|{' '*width}|\n"
        retstr += f"|{'.'*width}|\n"
        return retstr



class RunWorkout(Workout):
    def __init__(self, start, end, elve=0, calories=None):
        super().__init__(start, end , calories)
        self.icon = '🏃'
        self.kind = 'Running'



def main():
    w1 = Workout('1/1/2024 at 2:00pm', '1/1/2024 at 2:30pm')
    w2 = RunWorkout('1/1/2024 at 2:00pm', '1/1/2024 at 2:30pm')
    print(w1)
    print(w2)
    
    
if __name__ == '__main__':
    main()
    
    