from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output
import sys

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] == placeholders[1]:  # TODO: your condition here
        passed("Varibles are the same name")
    else:
        failed("Make sure you use the exact same name when using a varible")


def test_output():
    x = get_file_output()

    output = x.split('\n')
    if len(output) != 2:
        failed("There needs to be 2 print statments")
    else:
        if output[1] != "Erik is the best":
            failed("You have to print Erik is the best, cause he is")
        else:
            passed("Erik is indeed the best")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call
    test_output()


