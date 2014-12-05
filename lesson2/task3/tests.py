from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    function_components = ["def", ":", "my_sweet_function()", "print"]  # a lazy way to see if they made the function right.
    for comp in function_components:
        if comp in placeholder:
            passed("Has " + comp)
        else:
            failed("Needs a " + comp + " somewhere")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


