class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        output = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while temps and temp > temps[-1][0]:
                output[temps[-1][1]] = index - temps[-1][1]
                temps.pop()
            temps.append((temp, index))
        
        return output