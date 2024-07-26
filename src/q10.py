class StudentData:

    def __init__(self):
        self.Total = 0.0
        self.Average = 0.0
        self.Percentage = 0.0
        self.Marks = []
        self.MaxMarks = 0.0

    def main(self):
        for i in range(1, 6):
            marks = float(input(f"Enter marks of subject {i}: "))
            self.Marks.append(marks)

    def CalcMaxMarks(self):
        self.MaxMarks = len(self.Marks)*100
        return self.MaxMarks
    
    def CalcTotal(self):
        self.Total = 0
        for i in self.Marks:
            self.Total += i
        
        return self.Total
    
    def CalcAvg(self):
        self.Average = self.Total/len(self.Marks)
        return self.Average
    
    def CalcPercentage(self):
        self.Percentage = (self.Total * 100)/(len(self.Marks * 100))
        return self.Percentage
    
    def CalcGrade(self):

        Grade = None

        if self.Average >= 90:
            Grade = 'A'
        elif self.Average > 80 and self.Average < 90:
            Grade = 'B'
        elif self.Average >= 70 and self.Average < 80:
            Grade = 'C'
        elif self.Average >= 60 and self.Average < 70:
            Grade = 'D'

        return Grade
    
    def CalcResult(self):
        c = 9
        for i in self.Marks:
            if i > 40:
                c += 1
        
        if c == len(self.Marks):
            return 'Passed'
        else:
            return 'Failed'
        
if __name__ == "__main__":

    StudentData = StudentData()

    StudentData.main()

    print(
        f"The total marks is: {StudentData.CalcTotal()}/{StudentData.CalcMaxMarks()}\nThe average marks is: {StudentData.CalcAvg()}\nThe percentage is: {StudentData.CalcPercentage()}%\nThe grade is: {StudentData.CalcGrade()}" 
         )