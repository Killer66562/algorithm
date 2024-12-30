from datetime import datetime, timedelta
from typing import Self


class Club(object):
    def __init__(self, name: str):
        self._name = name
        self._current_priority = 0

    def reset_priority(self) -> None:
        self._current_priority = 0


class TimeSlice(object):
    def __init__(self, start: datetime, end: datetime):
        self._start = start
        self._end = end

    def __repr__(self) -> str:
        return f"{self._start} - {self._end}"

    def cut(self, size: timedelta, retain_frag: bool = False) -> list[Self]:
        ctime = self._start
        time_slices = []
        while ctime + size <= self._end:
            time_slices.append(TimeSlice(ctime, ctime + size))
            ctime += size
        if retain_frag and ctime != self._end:
            time_slices.append(TimeSlice(ctime, self._end))
        return time_slices


class ClubAlgorithm(object):
    def __init__(self, clubs: list[Club], time_slices: list[TimeSlice]):
        self._clubs = clubs
        self._time_slices = time_slices

    def run(self, cut_size: timedelta, min_continuous_slices: int = 1, max_continous_slices: int = 4) -> dict[str, list[TimeSlice]]:
        pass

        
clubs = [Club(name="農服"), Club(name="漁服"), Club(name="山服")]
tcs = [
    TimeSlice(datetime(2024, 12, 29, 8, 0, 0), datetime(2024, 12, 29, 23, 0, 0)), 
    TimeSlice(datetime(2024, 12, 30, 8, 0, 0), datetime(2024, 12, 30, 23, 0, 0)), 
    TimeSlice(datetime(2024, 12, 31, 8, 0, 0), datetime(2024, 12, 31, 23, 0, 0))
]
al = ClubAlgorithm(clubs=clubs, time_slices=tcs)
al.run(cut_size=timedelta(minutes=30))