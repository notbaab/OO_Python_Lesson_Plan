from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    answers_hints = [('def','You need to use a the keyword that lets you define a keyword'), (':','Check sweet function for what is missing'),
                     ('sweet_function()','Call the sweet function first'), ('sweeter_function()','Call the sweeter function next')]
    placeholder = placeholders[0]
    for idx, placeholder in enumerate(placeholders):
        if placeholder == answers_hints[idx][0]:  # TODO: your condition here
            passed()
        else:
            failed(answers_hints[idx][1])

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


