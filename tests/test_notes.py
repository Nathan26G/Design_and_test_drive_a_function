from lib.notes import *

#- make sure argument is taken in, as a string, e.g. includes_todo("#TODO buy milk")

# def test_takes_in_string():
#     is_string = includes_todo('#TODO buy milk')
#     value = type('#TODO buy milk')

#     assert value == str

def test_when_not_a_string():
    output = includes_todo(5)
    assert output == "Please enter a string"
    
# output is true when #TODO is in string, e.g. includes_todo("#TODO buy milk") = True
def test_return_true_when_todo_is_in_string():
    output = includes_todo('#TODO buy milk')
    assert output == True
    
# output is fales when there is no #TODO, e.g. includes_todo("buy milk") = False
def test_return_false_when_no_todo_in_string():
    output = includes_todo('buy milk')
    assert output == False
     
# output is false when #TODO is almost in string e.g 
def test_return_false_when_todo_almost_in_string():
    output = includes_todo('TODO buy milk')
    assert output == False

# output is false when #TODO is almost in string e.g. includes_todo("#TO buy milk") == False 
def test_return_false_when_todo_almost_in_string1():
    output = includes_todo('#TO buy milk')
    assert output == False