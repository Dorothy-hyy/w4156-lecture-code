import unittest
from lectures.testing.theory.mood_calculator import MoodCalculator
from lectures.testing.theory.mood_calculator import Mood

class MyTestCase(unittest.TestCase):
    """
    Note - we have two methods beginning 'test'. Both these methods will be run
    """

    def setUp(self):
        self.mood_calculator = MoodCalculator()

    def test_out_of_range(self):
        caseserror1 = [
            (-1, 69),
            (-1, 70),
            (-1, 90),
            (-1, 91),
            (37, 69),
            (37, 70),
            (37, 76),
            (37, 91)
        ]
        caseserror2 = [
            (0, 69),
            (0, 91),
            (27, 69),
            (27, 91),
        ]
        for case in caseserror1:
            with self.assertRaises(ValueError):
                self.mood_calculator.calculate_mood(case[0], case[1])
        for case in caseserror2:
            with self.assertRaises(ValueError):
                self.mood_calculator.calculate_mood(case[0], case[1])

    def test_mood_calculator(self):
        """
        TODO - Exercise for the student to write and test the mood calculator
        :return:
        """
        caseIrri = [
            (0, 70),
        ]
        caseJoy = [
            (0, 76),
        ]
        caseMoo = [
            (27, 70),
        ]
        caseHul = [
            (27, 76),
        ]


        for case in caseIrri:
            mood = self.mood_calculator.calculate_mood(case[0], case[1])
            self.assertEqual(mood, Mood(3))
        for case in caseJoy:
            mood = self.mood_calculator.calculate_mood(case[0], case[1])
            self.assertEqual(mood, Mood(1))
        for case in caseMoo:
            mood = self.mood_calculator.calculate_mood(case[0], case[1])
            self.assertEqual(mood, Mood(2))
        for case in caseHul:
            mood = self.mood_calculator.calculate_mood(case[0], case[1])
            self.assertEqual(mood, Mood(4))

if __name__ == '__main__':
    unittest.main()
