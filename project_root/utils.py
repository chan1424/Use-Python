#-------------------------
# utils.py : 계산 관련 함수
#-------------------------

# 평균을 계산하는 함수
def mean(scores):
    """점수 리스트의 평균을 계산합니다."""
    # 점수가 없는 경우 0으로 처리
    if not scores:
        return 0
    return sum(scores) / len(scores)

# 평균 점수에 따라 학점을 정하는 함수
def letter_grade(score):
    """점수에 따라 학점을 반환합니다."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"