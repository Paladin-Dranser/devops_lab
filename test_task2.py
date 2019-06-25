from unittest import TestCase
import task2


class TestEquation(TestCase):
    """Test task2.py"""
    def test_calculate(self):
        """Test calculate"""
        self.assertEqual(task2.calculate(3, 4, '+'), 7)
        self.assertEqual(task2.calculate(3, 4, '-'), -1)
        self.assertEqual(task2.calculate(3, 4, '*'), 12)
        self.assertEqual(task2.calculate(8, 4, '/'), 2)

    def test_is_correct_equation(self):
        self.assertEqual(task2.is_correct_equation('3+5=8'), 'YES')
        self.assertEqual(task2.is_correct_equation('3*5=8'), 'NO')
        self.assertEqual(task2.is_correct_equation('335=8'), 'ERROR')
