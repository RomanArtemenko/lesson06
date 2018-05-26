from unittest import TestCase, mock
from lab1.greeter import Greeter

class GreeterTestCase(TestCase):
    
    @mock.patch("lab1.greeter.datetime")
    def test_greet(self, mock_datetime):
        mock_datetime.now.return_value.hour = 13
        res = Greeter().greet("Roman")
        self.assertEqual(res, "Привет Roman")

    @mock.patch("lab1.greeter.datetime")    
    def test_greet_deleting_whitespace(self, mock_datetime):
        mock_datetime.now.return_value.hour = 13
        res = Greeter().greet("  Roman  ")
        self.assertEqual(res, "Привет Roman")
    
    @mock.patch("lab1.greeter.datetime")
    def test_greet_capitalize(self, mock_datetime):
        mock_datetime.now.return_value.hour = 13
        res = Greeter().greet("roman")
        self.assertEqual(res, "Привет Roman")

    @mock.patch("lab1.greeter.datetime")
    def test_greet_morning(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        res = Greeter().greet("Roman")
        self.assertEqual(res, "Доброе утро Roman")
    
    @mock.patch("lab1.greeter.datetime")
    def test_greet_evening(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20
        res = Greeter().greet("Roman")
        self.assertEqual(res, "Доброе вечер Roman")
 
    @mock.patch("lab1.greeter.datetime")
    def test_greet_night(self, mock_datetime):
        mock_datetime.now.return_value.hour = 23
        res = Greeter().greet("Roman")
        self.assertEqual(res, "Доброй ночи Roman")

    @mock.patch("lab1.greeter.logging")    
    def test_greet_log(self, mock_log):
        res = Greeter().greet("Roman")
        self.assertTrue(mock_log.info.called)