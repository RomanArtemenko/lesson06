from unittest import TestCase, mock
from lab2.string_calculator import StringCalculator

class StringCalculatorTestCase(TestCase):

    def test_add_empty(self):
        res = StringCalculator().add('')
        self.assertEqual(res, 0)

    def test_add_one_number(self):
        res = StringCalculator().add('2')
        self.assertEqual(res, 2)

    def test_add_two_number_with_comma(self):
        res = StringCalculator().add('1,2')
        self.assertEqual(res, 3)
    
    def test_add_two_number_with_linebreak(self):
        res = StringCalculator().add('5\n3')
        self.assertEqual(res, 8)
    
    def test_add_some_number_with_comma_linebreak(self):
        res = StringCalculator().add('1\n2,3\n4')
        self.assertEqual(res, 10)

    def test_add_negative_number(self):
        res = StringCalculator().add('-1,2,-3')
        self.assertEqual(res, 'отрицательные числа запрещены: -1,-3')

    def test_add_less_1000(self):
        res = StringCalculator().add('1\n2,3\n4,1001')
        self.assertEqual(res, 10)

    def test_add_one_delimeter(self):
        res = StringCalculator().add("//#\n1#2")
        self.assertEqual(res, 3)

    def test_add_some_delimeter(self):
        res = StringCalculator().add('//###\n1###2')
        self.assertEqual(res, 3)