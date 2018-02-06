from typing import Dict, Tuple, List
from enum import Enum, auto


class FriendFoe(Enum):
    Friend = auto()
    Foe = auto()


class RadarSignature:

    def __init__(self, x: float, y: float, friend_foe: FriendFoe):
        """
        :param x: in coordinate system relative to our plane
        :param y: in coordinate system relative to our plane
        :param friend_foe: is the plane friendly or foe
        """
        self.x = x
        self.y = y
        self.friend_foe = friend_foe


class NearestEnemyFinder:

    def detect_nearest_enemy(self, number_targets, signatures: List[RadarSignature]) -> List[Tuple[RadarSignature]]:
        """
        Detect the nearest N enemy targets
        :param number_targets: the number of enemy targets to return
        :param signatures: a list of radar signatures of planes. Coordinate system based around our plane being (0,0)
        :return: the N nearest enemy targets. If there are less than N enemy radar then return the
        """
        if number_targets == 0:
            return []
        elif number_targets < 0:
            return "Error"
        cache = []
        for target in signatures:
            if target.friend_foe == FriendFoe(2):
                cache.append([self.distance_from_orig(target.x, target.y), target])
        if len(cache) <= number_targets:
            return "Error"
        else:
            cache.sort()
            return [cache[i][1] for i in range(number_targets)]

    def distance_from_orig(self, x,y):
        return (x**2 + y**2)**0.5




