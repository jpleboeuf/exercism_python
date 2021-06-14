from __future__ import annotations


class Clock:
    def __init__(self, hour:int, minute:int):
        hour_carry, self.minute = divmod(minute, 60)
        day_carry, self.hour = divmod(hour + hour_carry, 24)

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other:Clock):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes:int):
        hour_carry, minute = divmod(self.minute + minutes, 60)
        day_carry, hour = divmod(self.hour + hour_carry, 24)
        return Clock(hour, minute)

    def __sub__(self, minutes:int):
        hour_uncarry, minute = divmod(self.minute - minutes, -60)
        day_uncarry, hour = divmod(self.hour - hour_uncarry, -24)
        return Clock(hour, minute)
