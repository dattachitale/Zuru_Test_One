from pyls import print_dict_info
from unittest.mock import patch

def testprint_dict_info(capsys):
    # Define sample file_info dictionary
    file_info = {
        'permissions': 'rw-r--r--',
        'size': '1024',
        'time_modified': 1612682055,
        'name': 'example.txt'
    }

    expected_output = "rw-r--r--       1024      Feb 07 10:40         example.txt\n"

    # Patching format_time to return a fixed value
    with patch('pyls.format_time') as mock_time:
        mock_time.return_value = "Feb 07 10:40"

        print_dict_info(file_info)

    # Capture printed output
    captured = capsys.readouterr()

    # Assert and validate
    assert captured.out == expected_output


def testprint_dict_info_two(capsys):
    file_info = {
        'permissions': 'rw-r--r--',
        'size': '1024',
        'time_modified': 1612682055,
        'name': 'example.txt'
    }
    expected_output = "rw-r--r--       1024      Feb 07 10:40         example.txt\n"

    with patch('pyls.format_time') as mock_time:
        mock_time.return_value = "Feb 07 10:40"
        print_dict_info(file_info)
    captured = capsys.readouterr()
    # Assert and validate
    assert captured.out == expected_output


def testprint_dict_info_three(capsys):
    # Negative test case: Missing required fields
    invalid_file_info = {
        'permissions': 'rw-r--r--',
        'size': '1024'
        # Missing 'time_modified' and 'name' fields
    }
    expected_error = "Error: Missing required fields\n"

    with patch('pyls.format_time') as mock_format_time:
        mock_format_time.return_value = "Feb 07 10:40"
        print_dict_info(invalid_file_info)
    captured = capsys.readouterr()
    assert captured.out == expected_error



def testprint_dict_info_four(capsys):
    # Additional positive test case: Empty file info
    empty_file_info = {}
    expected_empty_output = "         \n"

    with patch('pyls.format_time') as mock_format_time:
        mock_format_time.return_value = ""
        print_dict_info(empty_file_info)
    captured = capsys.readouterr()
    assert captured.out == expected_empty_output