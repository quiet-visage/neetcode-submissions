from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position,speed), reverse=True)
        times = []
        for car in cars:
            t = (target - car[0]) / car[1]
            if not times or t > times[-1]:
                times.append(t)
        return len(times)