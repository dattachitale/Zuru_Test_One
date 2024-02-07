from pyls import format_time

def testformat_size():
    time_modified = 1699941437
    expected_formatted_time = "Nov 14 11:27"
    actual_formatted_time = format_time(time_modified)
    # Assert and validate
    assert actual_formatted_time == expected_formatted_time, f"Expected: {expected_formatted_time}, Actual: {actual_formatted_time}"

def testformat_time_two():
    time_modified = 1612682055
    expected_formatted_time = "Feb 07 10:40"
    actual_formatted_time = format_time(time_modified)
    # Assert and validate
    assert actual_formatted_time == expected_formatted_time, f"Expected: {expected_formatted_time}, Actual: {actual_formatted_time}"
