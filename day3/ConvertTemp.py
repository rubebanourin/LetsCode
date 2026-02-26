class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahren = celsius * 1.80 + 32.00
        ans=[kelvin, fahren]
        return ans
