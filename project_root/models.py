#-------------------------
# models.py : 클래스 정의
#-------------------------

from utils import mean, letter_grade


# 한 명의 학생 정보를 저장하는 클래스
class Student:
    """학생 한 명의 이름과 점수를 관리하는 클래스입니다."""
    # 이름과 점수를 저장
    def __init__(self, name, scores):
        self.name = name      # 학생 이름
        self.scores = scores  # 학생의 점수 리스트

    # 평균 계산
    def average(self):
        """학생의 평균 점수를 계산합니다."""
        return mean(self.scores)

    # 학점 계산
    def grade(self):
        """학생의 평균 점수에 따른 학점을 계산합니다."""
        return letter_grade(self.average())

# 여러 학생의 성적을 관리하는 클래스
class GradeBook:
    def __init__(self):
        self.students = []  # 학생들을 저장할 리스트

    # 학생 추가
    def add_student(self, student):
        self.students.append(student)

    # 전체 반 평균 계산
    def class_average(self):
        # 학생이 없는 경우 ZeroDivisionError를 방지하기 위해 0을 반환
        if not self.students:
            return 0
            
        total = 0
        for s in self.students:
            total += s.average()
        return total / len(self.students)
