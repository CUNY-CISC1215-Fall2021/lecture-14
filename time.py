# A class representing a unit of time.
#
# Demonstrates how to integrate a class with Python operators.
# This class implements string conversion, +, -, and the
# relational operators.


class Time:
    """A class representing a duration of time"""

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other

    def __add__(self, other):
        s1 = self.to_int()
        if isinstance(other, Time):
            s2 = other.to_int()
        else:
            s2 = int(other)
        return int_to_time(s1 + s2)

    def __sub__(self, other):
        s1 = self.to_int()
        if isinstance(other, Time):
            s2 = other.to_int()
        else:
            s2 = int(other)
        return int_to_time(s1 - s2)

    def to_int(self):
        seconds = self.seconds
        seconds += self.minutes * 60
        seconds += self.hours * 60 * 60
        return seconds

    # Python operators
    def __gt__(self, other):
        s1 = self.to_int()
        s2 = other.to_int()

        return s1 > s2

    def __ge__(self, other):
        s1 = self.to_int()
        s2 = other.to_int()

        return s1 >= s2

    def __lt__(self, other):
        s1 = self.to_int()
        s2 = other.to_int()

        return s1 < s2

    def __le__(self, other):
        s1 = self.to_int()
        s2 = other.to_int()

        return s1 <= s2

    def __eq__(self, other):
        s1 = self.to_int()
        s2 = other.to_int()

        return s1 == s2

    # Reverse Python operators
    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other

    def __rgt__(self, other):
        return self > other

    def __rge__(self, other):
        return self >= other

    def __rlt__(self, other):
        return self < other

    def __rle__(self, other):
        return self <= other

    def __req__(self, other):
        return self == other


def int_to_time(s):
    result = Time()
    result.seconds = s
    result.minutes = result.seconds // 60
    result.seconds = result.seconds % 60
    result.hours = result.minutes // 60
    result.minutes = result.minutes % 60

    return result


t1 = Time(1, 30, 15)
t2 = Time(7, 31, 59)

print("t1:", t1)
print("t2:", t2)
print("10 + t1:", 10 + t1)
print("t1 + 10:", t1 + 10)
print("t1 + t2:", t1 + t2)

if t2 > t1:
    print("t1 is less than t2")
else:
    print("t2 is larger than t1")