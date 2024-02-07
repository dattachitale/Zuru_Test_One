from pyls import handle_path


def testhandle_path_existing_file(capsys):
    handle_path("parser/parser.go")

    # Capture the printed output
    captured = capsys.readouterr()

    expected_output = "This handles a path of a file or directory also \n\n"
    expected_output += '-rw-r--r-- 1622 Nov 17 12:05 parser/parser.go\n'

    # Assert and validate
    assert captured.out == expected_output


def testhandle_path_existing_file_two(capsys):
    handle_path("lexer/lexer_test.go")

    # Capture the printed output
    captured = capsys.readouterr()

    expected_output = "This handles a path of a file or directory also \n\n"
    expected_output += 'drwxr-xr-x 1729 Nov 14 15:15 lexer/lexer_test.go\n'

    # Assert and validate
    assert captured.out == expected_output


def testhandle_path_existing_file_three(capsys):
    handle_path("parser")

    # Capture the printed output
    captured = capsys.readouterr()

    expected_output = "This handles a path of a file or directory also \n\n"
    expected_output +="""\
drwxr-xr-x 1342 Nov 17 12:51 parser_test.go
-rw-r--r-- 1622 Nov 17 12:05 parser.go
drwxr-xr-x 533 Nov 14 16:03 go.mod\n"""

    # Assert and validate
    assert captured.out == expected_output


def testhandle_path_existing_file_four(capsys):
    handle_path("pars")

    # Capture the printed output
    captured = capsys.readouterr()

    expected_output = "This handles a path of a file or directory also \n\n"
    expected_output +="error: cannot access 'pars': No such file or directory\n"

    # Assert and validate
    assert captured.out == expected_output