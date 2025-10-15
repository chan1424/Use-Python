#----------------------
# gradebook/models.py
#----------------------


"""Student / Gradebook 클래스 정의"""

from .utils import mean, letter_grade

class Student:
    """한 명의 학생 정보를 저장"""
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def average(self):
        return mean(self.scores)
        
    def grade(self):
        return letter_grade(self.average())
        
    def __repr__(self):
        return f"Student(name={self.name!r}, avg={self.average():.2f}, grade={self.grade()!r})"

class Gradebook:
    """여려 학생의 성적을 관리"""
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def student_count(self):
        return len(self.students)
        
    def class_average(self):
        if not self.students:
            return 0.0
        
        # 전체 학생들의 평균 점수의 평균
        return mean([s.average() for s in self.students])
        
    def __repr__(self):
        return f"Gradebook({len(self.students)} students)"
        
    def __str__(self):
        return repr(self)