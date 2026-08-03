class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        min_radius = 0
        heater_ptr = 0
        num_heaters = len(heaters)
        for house in houses:
            while (heater_ptr + 1 < num_heaters and 
               abs(heaters[heater_ptr + 1] - house) <= abs(heaters[heater_ptr] - house)):
                heater_ptr += 1
            closest_dist = abs(heaters[heater_ptr] - house)
            if closest_dist > min_radius:
                min_radius = closest_dist
        return min_radius
        