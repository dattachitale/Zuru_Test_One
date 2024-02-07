from pyls import all_directory



def testall_directory(capsys):
    all_directory()
    captured = capsys.readouterr()
    # Define the expected output
    expected_output = "This is top directory including '.gitignore' \n"
    expected_output += "\n.gitignore\t\tLICENSE\t\tREADME.md\t\tast\t\tgo.mod\t\tlexer\t\tmain.go\t\tparser\t\ttoken\t\t"

    # Assert and validate
    assert captured.out == expected_output