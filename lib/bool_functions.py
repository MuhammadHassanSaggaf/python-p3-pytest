def return_true():
    return True

#Running Tests with Pytest
# running all tests we use pytest

# running all tests in the current directory
# pytest lib/testing

# running all tests in a file
# pytest lib/testing/test_bool_functions.py

#running one test in a file
# pytest lib/testing/test_bool_functions.py::test_return_true

#customizing the output
# -x excutes test until one fails then stops
# -pdb opens the debugger on failure
# -s tells pytest to show the full output for failed tests i.e # print statements
# -v verbose output
# -q quiet output
# -q shorten the output
# -h shows help