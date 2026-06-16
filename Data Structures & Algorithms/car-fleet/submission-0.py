class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        stck = []

        for car in cars:
            time = (target - car[0]) / car[1]
            if not stck or time > stck[-1]:
                stck.append(time)

        return len(stck)