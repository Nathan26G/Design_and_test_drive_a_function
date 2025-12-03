from lib.notes import *

#- make sure argument is taken in, as a string, e.g. includes_todo("#TODO buy milk")

# def test_takes_in_string():
#     is_string = includes_todo('#TODO buy milk')
#     value = type('#TODO buy milk')

#     assert value == str

def test_when_not_a_string():
    output = includes_todo(5)
    assert output == "Please enter a string"