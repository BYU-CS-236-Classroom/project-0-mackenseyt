# Here is the starter code for Lab 0, Hello World. 

# This is going to be the structure for future projects. This function (project#()) will 
# serve as your main function. It takes in one parameter, input, which is the input string
# for the test cases. It should return a string with your answer.

# If you haven't seen this syntax before, the ": str" and "-> str" are type annotations for Python.
# They just give you a clue into what type the input variable should be and the return type of the 
# function respectivly. It is good practice to label your functions like this unless you need the type 
# to be variable. 

# FIXME: This code should return "Hello World" plus whatever the value of "input" is.
def project0(input: str) -> str:
    # YOUR CODE GOES HERE
    return "Hello World " + input

# When testing projects, it can be helpful to be able to test custom inputs. 
# You can do this by just calling the function project0() with whatever input you want
# as shown here:
print(project0("This is my test input!"))
