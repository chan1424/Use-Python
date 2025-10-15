#-------------------------
# gradebook/cli.py
#-------------------------

"""명령행 실행 인터페이스 (CLI)"""

from .models import Student, Gradebook
from .io.csvio import load_students_from_csv

def run_cli():
    """명령형 실행을 실행할 간단한 CLI"""
    print("Gradebook CLI 실행 중 ...")

    # CSV 파일로부터 데이터 불러오기 예시
    try:
        students = load_students_from_csv("students.csv")
    except FileNotFoundError:
        print(f"경고: students.csv 파일이 없습니다. (기본 데이터 사용)")
        students = [
            Student("Alice", [100, 85, 92]),
            Student("Bob", [78, 75, 68]),
        ]

    # Gradebook에 학생 추가
    gb = Gradebook()
    for s in students:
        gb.add_student(s)

    # 출력
    print(f"\n[전체 학생 평균 점수: {gb.class_average():.2f}\n")
    for s in gb.students:
        print(f"학번: {s.name:7s} 평균:{s.average():5.1f} 학점:{s.grade():1s}")