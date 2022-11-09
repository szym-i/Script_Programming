from enum import Enum, unique


@unique
class Day(Enum):
    MON = 0; TUE = 1; WED = 2; THU = 3; FRI = 4; SAT = 5; SUN = 6
    def difference(self,day):
        dif = day.value - self.value
        if dif > -3:
            if dif > 3:
                return dif-7
            return dif
        return dif+7

def nthDayFrom(n, day):
    return Day(((day.value+n)%7)%7)
