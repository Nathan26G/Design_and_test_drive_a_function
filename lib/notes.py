def includes_todo(input):
    if type(input) != str:
        return "Please enter a string" 
    if '#TODO' in input:
      return True
    else:
      return False