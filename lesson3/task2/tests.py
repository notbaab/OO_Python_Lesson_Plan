from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    var_components = ['message_var', '=']
    for comp in var_components:
        if comp in placeholder:
            passed()
        else:
            failed("You need to reasign message_var")
    placeholder = placeholders[1]
    if "print" not in placeholder:
        failed("Needs a print statment")
    else:
        passed("Printing")
    if "message_var" not in placeholder:
        failed("Need to print message_var")
    else:
        passed()

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


