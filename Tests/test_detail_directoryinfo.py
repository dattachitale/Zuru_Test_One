from pyls import detail_directoryinfo

def testdetail_directoryinfo(capsys):
    # Call the top_directory function
    detail_directoryinfo()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output string
    expected_output = "This is detail directory information with additional information \n\n"
    expected_output += """\
-rw-r--r-- \t\t1071 \t\tNov 14 11:27 \t\tLICENSE
-rw-r--r-- \t\t83 \t\tNov 14 11:27 \t\tREADME.md
drwxr-xr-x \t\t4096 \t\tNov 14 15:58 \t\tast
-rw-r--r-- \t\t60 \t\tNov 14 13:51 \t\tgo.mod
drwxr-xr-x \t\t4096 \t\tNov 14 15:21 \t\tlexer
-rw-r--r-- \t\t74 \t\tNov 14 13:57 \t\tmain.go
drwxr-xr-x \t\t4096 \t\tNov 17 12:51 \t\tparser
drwxr-xr-x \t\t4096 \t\tNov 14 14:57 \t\ttoken
"""

    # Assert that the printed output matches the expected output
    assert captured.out == expected_output