from enum import Enum, unique


@unique
class Action(Enum):
    DAY_EARLIER = "d-"; DAY_LATER = "d+"; TIME_EARLIER = "t-"; TIME_LATER = "t+"


if __name__ == '__main__':
    a = Action("t-")
    print(a)
