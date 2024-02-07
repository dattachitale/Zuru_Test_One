import time
import pytest
from pyls import format_time

def test_format_time():
    time_modified = 1699941437
    expected_formatted_time = "Nov 14 11:27"
    actual_formatted_time = format_time(time_modified)
    assert actual_formatted_time == expected_formatted_time, f"Expected: {expected_formatted_time}, Actual: {actual_formatted_time}"

def test_format_time_two():
    time_modified = 1612682055
    expected_formatted_time = "Feb 07 10:40"
    actual_formatted_time = format_time(time_modified)
    assert actual_formatted_time == expected_formatted_time, f"Expected: {expected_formatted_time}, Actual: {actual_formatted_time}"
