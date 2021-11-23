# Alternate Time class that stores the time in seconds
#
# We can do this because we can choose how to implement the Time class.
# Data can be stored any way we want, not just how we want to present it.


class Time:
    """A class representing a duration of time"""

    def __init__(self, hours=0, minutes=0, seconds=0):
        # Convert the input time to seconds
        self.seconds = seconds
        self.seconds += minutes * 60
        self.seconds += hours * 60 * 60
        print(self.seconds)

    def __str__(self):
        # Convert the seconds attribute to hours, minutes, and seconds for display
        seconds = self.seconds % 60
        minutes = self.seconds // 60
        hours = minutes // 60
        minutes = minutes % 60

        return f"{hours}:{minutes}:{seconds}"

    # Python operators
    def __add__(self, other):
        s1 = self.seconds
        if isinstance(other, Time):
            s2 = other.seconds
        else:
            s2 = int(other)
        return Time(seconds=s1 + s2)

    def __sub__(self, other):
        s1 = self.seconds
        if isinstance(other, Time):
            s2 = other.seconds
        else:
            s2 = int(other)
        return Time(seconds=s1 - s2)

    def __gt__(self, other):
        s1 = self.seconds
        if isinstance(other, Time):
            s2 = other.seconds
        else:
            s2 = int(other)
        return s1 > s2

    def __ge__(self, other):
        s1 = self.seconds
        if isinstance(other, Time):
            s2 = other.seconds
        else:
            s2 = int(other)
        return s1 >= s2

    def __lt__(self, other):
        s1 = self.seconds
        if isinstance(other, Time):
            s2 = other.seconds
        else:
            s2 = int(other)
        return s1 < s2

    def __le__(self, other):
        s1 = self.seconds
        if isinstance(other, Time):
            s2 = other.seconds
        else:
            s2 = int(other)
        return s1 <= s2

    def __eq__(self, other):
        s1 = self.seconds
        if isinstance(other, Time):
            s2 = other.seconds
        else:
            s2 = int(other)
        return s1 == s2

    # Reverse python operators
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