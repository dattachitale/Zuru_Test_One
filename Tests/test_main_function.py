"""This is not implemented fully"""


from pyls import decision_function
import argparse

def testdecision_function(capsys):
    # test cases to check the functionality of decision_function

    args = argparse.Namespace(list_format=True, all_files=False, reverse=False, time_modify=False, filter=None,
                              path=None, human=None)
    output = decision_function(args)

    # Capture the printed output
    captured = capsys.readouterr()
    print(output)

    # Add assertions to verify the printed output
    # assert "Expected Output" in captured.out



