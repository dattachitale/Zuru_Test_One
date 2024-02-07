from pyls import top_directory



def testtop_directory(capsys):
    top_directory()
    captured = capsys.readouterr()
    # Define the expected output
    expected_output = "This is top directory excluding '.gitignore' \n"
    expected_output += "\nLICENSE\t\tREADME.md\t\tast\t\tgo.mod\t\tlexer\t\tmain.go\t\tparser\t\ttoken\t\t"

    # Assert and validate
    assert captured.out == expected_output