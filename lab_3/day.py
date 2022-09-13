from enum import Enum, unique

@unique
class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6
    def difference(self,day):
        return day.value-self.value

def nthDayFrom(n, day):
    return Day((day.value+n%7)%7)

if __name__ == '__main__':
    day = Day.MON
    print(day.name)
    print(day.difference(Day.SUN))
    n = int(input())
    print(nthDayFrom(n,day).name)
