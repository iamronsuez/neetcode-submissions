class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered = sorted(zip(position, speed), reverse=True)
        
        fleet_time = 0
        fleet_count = 0
        for pos, vel in ordered:
            current_time = (target - pos) / vel
            if current_time > fleet_time:
                fleet_time = current_time
                fleet_count += 1
        return fleet_count