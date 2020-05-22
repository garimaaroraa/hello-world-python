from dataclasses import dataclass
from datetime import datetime
from functools import reduce
from typing import List

import pytz


@dataclass
class VehicleTripStats:
    start_count: int
    end_count: int

    def __add__(self, other):
        return VehicleTripStats(
            start_count=self.start_count + other.start_count,
            end_count=self.end_count + other.end_count,
        )

    def __eq__(self, other):
        return (
            self.start_count == other.start_count and self.end_count == other.end_count
        )


def hello_world(name: str):
    return f"Hello World {name}"


def functools_reduce_test(vehicle_stats: List):
    return reduce((lambda x, y: x + y), vehicle_stats)


def time_now() -> datetime:
    return pytz.utc.localize(datetime.utcnow())
