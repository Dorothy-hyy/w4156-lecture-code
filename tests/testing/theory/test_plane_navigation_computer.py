import unittest
from lectures.testing.theory.plane_navigation_computer import FriendFoe, NearestEnemyFinder, RadarSignature
import tests.helper as helper


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.nearest_enemy = NearestEnemyFinder()

    @helper.skip_intentionally_failing()
    def test_todo(self):
        """
        Exercise for the student
        :return:
        """

        casesempty = [
            [0,[RadarSignature(0, 0, FriendFoe(2))] ]

        ]
        caseserror = [
            [-1, [RadarSignature(0, 0, FriendFoe(2))]],
            [1, [RadarSignature(0, 0, FriendFoe(1)), RadarSignature(1, 1, FriendFoe(1))]]
        ]
        cases = [[1, [RadarSignature(0, 0,FriendFoe(1)),RadarSignature(1,1,FriendFoe(2))]],
                 [1, [RadarSignature(0, 0, FriendFoe(2)), RadarSignature(1, 1, FriendFoe(2))]],
                 [5, [RadarSignature(0, 0, FriendFoe(1)), RadarSignature(1, 1, FriendFoe(2)),RadarSignature(2, 2, FriendFoe(1)), RadarSignature(3, 3, FriendFoe(2)),
                      RadarSignature(4, 4, FriendFoe(2)), RadarSignature(5, 5, FriendFoe(2)),RadarSignature(6, 6, FriendFoe(1)), RadarSignature(7, 7, FriendFoe(2))]],
                 [1, [RadarSignature(0, 0, FriendFoe(1)), RadarSignature(9999999999999999, 99999999999999999999, FriendFoe(2))]]
                 ]
        for case in caseserror:
            res = self.nearest_enemy.detect_nearest_enemy(case[0], case[1])
            self.assertEqual(res,"Error")
        for case in casesempty:
            res = self.nearest_enemy.detect_nearest_enemy(case[0], case[1])
            self.assertEqual(res,[])


if __name__ == '__main__':
    unittest.main()
