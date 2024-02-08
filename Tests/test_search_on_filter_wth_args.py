from pyls import search_on_filter_wth_args

def testsearch_on_filter_wth_args(capsys):
    # Call the top_directory function
    search_on_filter_wth_args('dir', reverse=True, time_modify=True)

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output string
    expected_output = "This is search result of a dir/file on specific filter options - file/dir \n\n"
    expected_output += """\
drwxr-xr-x 4.0 KB Nov 17 12:51 parser
drwxr-xr-x 4.0 KB Nov 14 15:21 lexer
drwxr-xr-x 60.0 B Nov 14 13:51 go.mod
drwxr-xr-x 1.0 KB Nov 14 11:27 LICENSE
drwxr-xr-x 83.0 B Nov 14 11:27 README.md
"""

    # Assert and validate
    assert captured.out == expected_output