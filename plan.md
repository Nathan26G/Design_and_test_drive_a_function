
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## requirments:
- define a function that will take a string
- output will true or false 

## examples
>>> includes_todo("#TODO buy milk")
True
>>> includes_todo("drink tea")
False
>>> includes_todo("learn to test-drive my code #TODO")
True

## mock tests:

- make sure argument is taken in, as a string, e.g. includes_todo("#TODO buy milk")

- error message is given as output when argumentr is not a string, e.g. includes_todo(5) = 'Please enter a string'

- output is true when #TODO is in string, e.g. includes_todo("#TODO buy milk") = True

- output is fales when there is no #TODO, e.g. includes_todo("buy milk") = False

- output is false when #TODO is almost in string e.g 
includes_todo("TODO buy milk") == False

- output is false when #TODO is almost in string e.g. 
includes_todo("#TO buy milk") == False 

- output is false when #TODO is almost in string e.g. 
includes_todo("#todo buy milk") == False 