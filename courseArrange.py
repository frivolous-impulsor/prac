class Course:
    def __init__(self, title: str, code: str, timeSlots: list[int], description:str = None) -> None:  #[1,2]
        self.title: str = title
        self.code: str = code
        for time in timeSlots:
            if time < 1 or time > 4:
                raise ValueError("timeSlot within 1 to 4 inclusive")
        if len(timeSlots) == 1:
            self.isBlock = True
        elif len(timeSlots) == 2 and abs(timeSlots[1]-timeSlots[0]) == 1 and timeSlots[1] % 2 == 0:
            self.isBlock == False
        else:
            raise ValueError("timeSlot either a block(1) or semester(2) with 2 consecutive first or second 2 blocks")
        self.timeSlots = timeSlots 
        self.desciption = description

    def editDescription(self, desc: str) -> None:
        self.desciption = desc


class CourseGroup:
    def __init__(self) -> None:
        self.group: list[Course] = []
        self.timeSheet: dict = {}
    def addCourse(self, course: Course) -> None:
        self.group.append(course)
        timeSlots = course.timeSlots
        isBlock = course.isBlock
        if isBlock:
            block = course.timeSlots[0]
            self.timeSheet[block] = course
        else:
            block1 = course.timeSlots[0]
            block2 = course.timeSlots[1]
            self.timeSheet[block1] = course
            self.timeSheet[block2] = course
    
    def printTimeSheet(self):
        