# -------------------
# tests/test_utils.py
# -------------------

import unittest
from gradebook.utils import mean, letter_grade

class TestUtils(unittest.TestCase):
    
    def test_mean(self):
        # 일반적인 평균 계산 테스트
        self.assertEqual(mean([10, 20, 30]), 20)
        # 빈 리스트의 평균은 0.0 인지 테스트
        self.assertEqual(mean([]), 0.0)
        
    def test_letter_grade(self):
        # 학점 부여 로직 테스트
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(75), "C")
        self.assertEqual(letter_grade(65), "D")
        self.assertEqual(letter_grade(50), "F")

if __name__ == "__main__":
    unittest.main()