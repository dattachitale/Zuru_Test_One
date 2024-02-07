from pyls import main_function
import argparse


def testlist_format(capsys):
    args = argparse.Namespace(list_format=True, all_files=False, reverse=False, time_modify=False, filter=None,
                              path=None, human=None)
    output = main_function(args)
    # Test case for -l flag
    # main_function(filter==None, human==None, list_format=True)

    # Capture the printed output
    captured = capsys.readouterr()
    print(captured)

    # Add assertions to verify the printed output
    assert "Expected Output" in captured.out


# def testlist_format():
#     args = argparse.Namespace(list_format=True, all_files=False, reverse=False, time_modify=False, filter=None, path=None, human=None)
#     output = main_function(args)
#     # Assert the output against the expected result
#     print(output)
#     assert output == None
#
# def testlist_format_one():
#     args = argparse.Namespace(list_format=True, all_files=False, reverse=True, time_modify=False, filter=None, path=None, human=None)
#     output = main_function(args)
#
#     # Assert the output against the expected result
#     print(output)
#     assert output == None