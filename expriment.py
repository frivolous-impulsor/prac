#global vars
#Codes
institutionCode = {0: "McMaster"}
subjectCode = {0: "COMPSCI", 1: "PHYS"}
courseCode = {}
#vars
cidIterator = 0


class Course:
    def __init__(self, subject: int, code: str, inst = 0) -> None:
        self.cid = cidIterator
        self.subject = subject
        self.code = code
        self.inst = inst
        self.description = ""
        cidIterator +=1
    def addDescription(self, text: str):
        self.description = text
    #return a set of topics that the course introduces
    def topics(self):
        description = self.description
        "todo"


class CourseGraph:
    def __init__(self) -> None:
        self.vNum = 0
        self.eNum = 0
        self.adjDict = {}

    def addCourse(self, subject, code, inst=0):
        course = Course(subject, code, inst)
        cid = course.cid
        self.adjDict[cid] = set()
        courseCode = {cid: course}
        self.vNum +=1
    
    def addEquivalent(self, courseAid, courseBid):
        self.adjDict[courseAid].add(courseBid)
        self.adjDict[courseBid].add(courseAid)
        self.eNum +=2

    
