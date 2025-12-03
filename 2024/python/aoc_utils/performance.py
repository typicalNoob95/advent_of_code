import time
import datetime
import typing

def print_duration(part: typing.Callable, number: str) -> None:
    start = time.perf_counter()
    part()
    end = time.perf_counter()
    print(f"[PART {number.upper()}] - Duration: {str(datetime.timedelta(seconds=end - start))}")